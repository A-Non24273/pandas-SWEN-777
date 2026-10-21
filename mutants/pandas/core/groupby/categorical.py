from __future__ import annotations

import numpy as np

from pandas.core.algorithms import unique1d
from pandas.core.arrays.categorical import (
    Categorical,
    CategoricalDtype,
    recode_for_categories,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_recode_for_groupby__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_recode_for_groupby__mutmut)
def recode_for_groupby(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_orig(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_1(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = None

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_2(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(None)

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_3(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes == -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_4(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != +1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_5(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -2])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_6(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = None

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_7(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(None)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_8(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = None
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_9(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(None)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_10(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = None

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_11(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(None, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_12(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, None, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_13(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, None, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_14(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=None)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_15(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_16(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_17(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_18(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, )

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_19(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=True)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_20(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = None
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_21(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(None, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_22(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=None)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_23(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_24(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, )
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_25(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(None, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_26(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=None)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_27(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_28(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, )

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_29(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = None
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_30(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(None)
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_31(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes == -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_32(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != +1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_33(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -2])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_34(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) >= len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_35(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = None
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_36(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            None, unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_37(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), None, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_38(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=None
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_39(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_40(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_41(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_42(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(None), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_43(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=False
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_44(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = None
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_45(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate(None)
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_46(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = None

    return Categorical(c, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_47(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(None, c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_48(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, None)


def x_recode_for_groupby__mutmut_49(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c.categories.take(take_codes))


def x_recode_for_groupby__mutmut_50(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, )


def x_recode_for_groupby__mutmut_51(c: Categorical, sort: bool, observed: bool) -> Categorical:
    """
    Code the categories to ensure we can groupby for categoricals.

    If observed=True, we return a new Categorical with the observed
    categories only.

    If sort=False, return a copy of self, coded with categories as
    returned by .unique(), followed by any categories not appearing in
    the data. If sort=True, return self.

    This method is needed solely to ensure the categorical index of the
    GroupBy result has categories in the order of appearance in the data
    (GH-8868).

    Parameters
    ----------
    c : Categorical
    sort : bool
        The value of the sort parameter groupby was called with.
    observed : bool
        Account only for the observed values

    Returns
    -------
    Categorical
        If sort=False, the new categories are set to the order of
        appearance in codes (unless ordered=True, in which case the
        original order is preserved), followed by any unrepresented
        categories in the original order.
    """
    # we only care about observed values
    if observed:
        # In cases with c.ordered, this is equivalent to
        #  return c.remove_unused_categories(), c

        take_codes = unique1d(c.codes[c.codes != -1])

        if sort:
            take_codes = np.sort(take_codes)

        # we recode according to the uniques
        categories = c.categories.take(take_codes)
        codes = recode_for_categories(c.codes, c.categories, categories, copy=False)

        # return a new categorical that maps our new codes
        # and categories
        dtype = CategoricalDtype(categories, ordered=c.ordered)
        return Categorical._simple_new(codes, dtype=dtype)

    # Already sorted according to c.categories; all is fine
    if sort:
        return c

    # sort=False should order groups in as-encountered order (GH-8868)

    # GH:46909: Re-ordering codes faster than using (set|add|reorder)_categories
    # GH 38140: exclude nan from indexer for categories
    unique_notnan_codes = unique1d(c.codes[c.codes != -1])
    if (num_cat := len(c.categories)) > len(unique_notnan_codes):
        # GH 13179: All categories need to be present, even if missing from the data
        missing_codes = np.setdiff1d(
            np.arange(num_cat), unique_notnan_codes, assume_unique=True
        )
        take_codes = np.concatenate((unique_notnan_codes, missing_codes))
    else:
        take_codes = unique_notnan_codes

    return Categorical(c, c.categories.take(None))

mutants_x_recode_for_groupby__mutmut['_mutmut_orig'] = x_recode_for_groupby__mutmut_orig # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_1'] = x_recode_for_groupby__mutmut_1 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_2'] = x_recode_for_groupby__mutmut_2 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_3'] = x_recode_for_groupby__mutmut_3 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_4'] = x_recode_for_groupby__mutmut_4 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_5'] = x_recode_for_groupby__mutmut_5 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_6'] = x_recode_for_groupby__mutmut_6 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_7'] = x_recode_for_groupby__mutmut_7 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_8'] = x_recode_for_groupby__mutmut_8 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_9'] = x_recode_for_groupby__mutmut_9 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_10'] = x_recode_for_groupby__mutmut_10 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_11'] = x_recode_for_groupby__mutmut_11 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_12'] = x_recode_for_groupby__mutmut_12 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_13'] = x_recode_for_groupby__mutmut_13 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_14'] = x_recode_for_groupby__mutmut_14 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_15'] = x_recode_for_groupby__mutmut_15 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_16'] = x_recode_for_groupby__mutmut_16 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_17'] = x_recode_for_groupby__mutmut_17 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_18'] = x_recode_for_groupby__mutmut_18 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_19'] = x_recode_for_groupby__mutmut_19 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_20'] = x_recode_for_groupby__mutmut_20 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_21'] = x_recode_for_groupby__mutmut_21 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_22'] = x_recode_for_groupby__mutmut_22 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_23'] = x_recode_for_groupby__mutmut_23 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_24'] = x_recode_for_groupby__mutmut_24 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_25'] = x_recode_for_groupby__mutmut_25 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_26'] = x_recode_for_groupby__mutmut_26 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_27'] = x_recode_for_groupby__mutmut_27 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_28'] = x_recode_for_groupby__mutmut_28 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_29'] = x_recode_for_groupby__mutmut_29 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_30'] = x_recode_for_groupby__mutmut_30 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_31'] = x_recode_for_groupby__mutmut_31 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_32'] = x_recode_for_groupby__mutmut_32 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_33'] = x_recode_for_groupby__mutmut_33 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_34'] = x_recode_for_groupby__mutmut_34 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_35'] = x_recode_for_groupby__mutmut_35 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_36'] = x_recode_for_groupby__mutmut_36 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_37'] = x_recode_for_groupby__mutmut_37 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_38'] = x_recode_for_groupby__mutmut_38 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_39'] = x_recode_for_groupby__mutmut_39 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_40'] = x_recode_for_groupby__mutmut_40 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_41'] = x_recode_for_groupby__mutmut_41 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_42'] = x_recode_for_groupby__mutmut_42 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_43'] = x_recode_for_groupby__mutmut_43 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_44'] = x_recode_for_groupby__mutmut_44 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_45'] = x_recode_for_groupby__mutmut_45 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_46'] = x_recode_for_groupby__mutmut_46 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_47'] = x_recode_for_groupby__mutmut_47 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_48'] = x_recode_for_groupby__mutmut_48 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_49'] = x_recode_for_groupby__mutmut_49 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_50'] = x_recode_for_groupby__mutmut_50 # type: ignore # mutmut generated
mutants_x_recode_for_groupby__mutmut['x_recode_for_groupby__mutmut_51'] = x_recode_for_groupby__mutmut_51 # type: ignore # mutmut generated
