import random 
import warnings

import tables

import pandas as pd

from sklearn import preprocessing
#Is this appropriate?


def get_offspring_range(my_parents, samples):
    my_index = samples.index(my_parents[1])
    start = my_index + 1
    parents_position = parents.index(my_parents)
    if  parents_position == len(parents) - 1:
        end = len(samples)
    else:
        end = samples.index(parents[parents_position + 1][0])
    return start, end


def compute_medelian_errors(parents, offspring):
    #autosome only
    mo_alleles = set(parents[0])
    fa_alleles = set(parents[1])
    if set([-1]) in [mo_alleles, fa_alleles]:
        return
    if len(mo_alleles) == 2 and len(fa_alleles) == 2:
        #Both HZ, this case it not trivial
        return
    cnt = cnt_mo = cnt_fa = total = 0
    for ofs in offspring:
        my_alleles = set(ofs)
        if set(ofs) == set([-1]):
            continue
        total += 1
        if len(my_alleles & mo_alleles) == 0:
            cnt += 1
            cnt_mo += 1
        if len(my_alleles & fa_alleles) == 0:
            cnt += 1
            cnt_fa += 1
        # Ofspring has more alleles (hz) than parents
        if len(my_alleles) > len(fa_alleles | mo_alleles):
            cnt += 1
    return total, cnt, cnt_mo, cnt_fa
#discuss probs of 01 01 01 01 01 if both parents hz

def get_mendel_results():
    my_parents = parents[0]
    ofs_mo = samples.index(my_parents[0])
    ofs_fa = samples.index(my_parents[1])
    ofs_start, ofs_end = get_offspring_range(my_parents, samples)

    i = 0
    mendel_results = {}
    has_errors = []
    for pos, na, genotype in zip(poses, num_alleles, genotypes):
        i += 1
        if random.randint(0, 100) < 90:
            continue
        if na != 2:
            continue
        mo_alleles = genotype[ofs_mo,:]
        fa_alleles = genotype[ofs_fa,:]
        ofs_alleles = genotype[ofs_start:ofs_end,:]
        errors = compute_medelian_errors([mo_alleles, fa_alleles], ofs_alleles)
        if errors is None:
            continue
        if errors[1] > 0:
            has_errors.append(pos)
        mendel_results[pos] = i, errors
    return mendel_results, has_errors


def get_train(annotations, return_scaler=False, normalize=True, scale=True):
    warnings.warn('use get_dataset_with_outcome', DeprecationWarning)
    return get_dataset_with_outcome(annotations, return_scaler,
                                    normalize, scale)

def get_dataset_with_outcome(annotations, return_scaler=False,
                             normalize=True, scale=True):
    train_X = []
    train_Y = []
    scaler = preprocessing.StandardScaler()
    #This is silly (memory-wise)
    annot_dict = {}
    for annotation in annotations:
        annot_dict[annotation] = store_3L.get_node('/3L/variants/%s' % annotation).read()

    for i, pos in enumerate(poses):
        try:
            if pos not in mendel_results:
                continue
        except IndexError:
            continue
        #if pos not in has_errors:
        #    # We throw away 90% of good positions
        #    if random.randint(0, 100) > 10:
        #        continue
        my_entry = []
        for annotation in annotations:
            my_entry.append(annot_dict[annotation][i])
        train_X.append(my_entry)
        train_Y.append(0 if pos in has_errors else 1)

    #train_pre = preprocessing.normalize(preprocessing.scale(train_X))
    if normalize:
        pre_pre = preprocessing.normalize(train_X)
    else:
        pre_pre = train_X
    if scale:
        train_pre = scaler.fit_transform(pre_pre)
    else:
        train_pre = pre_pre
    #train_pre = preprocessing.scale(train_X)
    train_pre = pd.DataFrame(train_pre, columns=annotations)
    train_pre['OK'] = pd.Series(train_Y, index=train_pre.index)
    if return_scaler:
        return train_pre, scaler
    else:
        return train_pre



parents = [['AD0231-C', 'AD0232-C'], ['AD0254-C', 'AD0255-C'],
           ['AD0305-C', 'AD0306-C'], ['AD0347-C', 'AD0348-C']]

L3_h5 = '../../raw/crosses-3L.h5'

store_3L = tables.open_file(L3_h5, 'r')
samples = [x.decode('utf-8') for x in store_3L.get_node('/3L/samples').read()]
poses = store_3L.get_node('/3L/variants/POS').read()
num_alleles = store_3L.get_node('/3L/variants/num_alleles').read()
genotypes = store_3L.get_node('/3L/calldata/genotype').read() #
mendel_results, has_errors = get_mendel_results()

