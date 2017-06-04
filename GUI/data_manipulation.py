from algorithms.factorization import fermat, pollard_rho, trial_division
from algorithms.math import approx_cdf, extended_gcd, lcm, primality_test, sieve_atkin, sieve_eratosthenes, \
    std_normal_pdf
from algorithms.random import mersenne_twister
from algorithms.searching import binary_search, bmh_search, depth_first_search, kmp_search,\
    rabinkarp_search, breadth_first_search
from algorithms.sorting import bogo_sort, bubble_sort, cocktail_sort, comb_sort, gnome_sort, heap_sort,\
    insertion_sort, merge_sort, quick_sort, quick_sort_in_place, selection_sort, shell_sort
from algorithms.shuffling import knuth


def fct_operations(f_code, v):
    if f_code == 1:
        res = fermat.fermat(v)
        return res
    elif f_code == 2:
        res = pollard_rho.pollard_rho(v)
        return res
    elif f_code == 3:
        res = trial_division.trial_division(v)
        return res


def mth_operations_1_input(f_code, v):
    if f_code == 1:
        res = approx_cdf.cdf(v)
        return res
    elif f_code == 4:
        res = primality_test.is_prime(v)
        return res
    elif f_code == 5:
        res = sieve_atkin.atkin(v)
        return res
    elif f_code == 6:
        res = sieve_eratosthenes.eratosthenes(v)
        return res
    elif f_code == 7:
        res = std_normal_pdf.pdf(v)
        return res


def mth_operations_2_inputs(f_code, v1, v2):
    if f_code == 2:
        res = extended_gcd.extended_gcd(v1, v2)
        return res
    elif f_code == 3:
        res = lcm.lcm(v1, v2)
        return res


def rnd_operations(seed):
    obj = mersenne_twister.MersenneTwister()
    obj.seed(seed)
    res = obj.randint()
    return res


def src_operations(f_code, v1, v2):
    if f_code == 1:
        res = binary_search.search(v1, v2)
        return res
    elif f_code == 2:
        try:
            res = bmh_search.search(v1, v2)
            return res
        except IndexError:
            res = "Your key either occurs throughout the string, or more than 1 time."
            return res
    elif f_code == 3:
        try:
            res = depth_first_search.dfs(v1, v2)
            return res
        except TypeError:
            res = "Enter all edges for all nodes for the DFS algorithm to work correctly."
            return res
    elif f_code == 4:
        res = kmp_search.search(v1, v2)
        return res
    elif f_code == 5:
        res = rabinkarp_search.search(v1, v2)
        return res
    elif f_code == 6:
        try:
            res = breadth_first_search.bfs(v1, v2)
            return res
        except TypeError:
            res = "Enter all edges for all nodes for the BFS algorithm to work correctly."
            return res


def srt_operations(f_code, v):
    if f_code == 1:
        res = bogo_sort.sort(v)
        return res
    elif f_code == 2:
        res = bubble_sort.sort(v)
        return res
    elif f_code == 3:
        res = cocktail_sort.sort(v)
        return res
    elif f_code == 4:
        res = comb_sort.sort(v)
        return res
    elif f_code == 5:
        res = gnome_sort.sort(v)
        return res
    elif f_code == 6:
        res = heap_sort.sort(v)
        return res
    elif f_code == 7:
        res = insertion_sort.sort(v)
        return res
    elif f_code == 8:
        res = merge_sort.sort(v)
        return res
    elif f_code == 9:
        res = quick_sort.sort(v)
        return res
    elif f_code == 10:
        res = quick_sort_in_place.sort(v, 0, len(v)-1)
        return res
    elif f_code == 11:
        res = selection_sort.sort(v)
        return res
    elif f_code == 12:
        res = shell_sort.sort(v)
        return res


def shf_operations(v):
    res = knuth.shuffle(v)
    return res
