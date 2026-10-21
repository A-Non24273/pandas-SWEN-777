"""
Core eval alignment algorithms.
"""

from __future__ import annotations

from functools import (
    partial,
    wraps,
)
from typing import TYPE_CHECKING
import warnings

import numpy as np

from pandas._config.config import _global_config as config

from pandas.errors import PerformanceWarning
from pandas.util._exceptions import find_stack_level

from pandas.core.dtypes.generic import (
    ABCDataFrame,
    ABCSeries,
)

from pandas.core.base import PandasObject
import pandas.core.common as com
from pandas.core.computation.common import result_type_many

if TYPE_CHECKING:
    from collections.abc import (
        Callable,
        Sequence,
    )

    from pandas._typing import F

    from pandas.core.generic import NDFrame
    from pandas.core.indexes.api import Index


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__align_core_single_unary_op__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__align_core_single_unary_op__mutmut)
def _align_core_single_unary_op(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_orig(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_1(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = ""

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_2(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = None
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_3(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(None, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_4(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=None)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_5(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_6(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, )
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_7(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = None
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_8(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(None)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_9(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(None, "axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_10(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, None):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_11(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr("axes"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_12(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, ):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_13(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "XXaxesXX"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_14(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "AXES"):
            axes = _zip_axes_from_type(typ, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_15(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = None

    return typ, axes


def x__align_core_single_unary_op__mutmut_16(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(None, term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_17(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, None)

    return typ, axes


def x__align_core_single_unary_op__mutmut_18(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(term.value.axes)

    return typ, axes


def x__align_core_single_unary_op__mutmut_19(
    term,
) -> tuple[partial | type[NDFrame], dict[str, Index] | None]:
    typ: partial | type[NDFrame]
    axes: dict[str, Index] | None = None

    if isinstance(term.value, np.ndarray):
        typ = partial(np.asanyarray, dtype=term.value.dtype)
    else:
        typ = type(term.value)
        if hasattr(term.value, "axes"):
            axes = _zip_axes_from_type(typ, )

    return typ, axes

mutants_x__align_core_single_unary_op__mutmut['_mutmut_orig'] = x__align_core_single_unary_op__mutmut_orig # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_1'] = x__align_core_single_unary_op__mutmut_1 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_2'] = x__align_core_single_unary_op__mutmut_2 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_3'] = x__align_core_single_unary_op__mutmut_3 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_4'] = x__align_core_single_unary_op__mutmut_4 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_5'] = x__align_core_single_unary_op__mutmut_5 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_6'] = x__align_core_single_unary_op__mutmut_6 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_7'] = x__align_core_single_unary_op__mutmut_7 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_8'] = x__align_core_single_unary_op__mutmut_8 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_9'] = x__align_core_single_unary_op__mutmut_9 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_10'] = x__align_core_single_unary_op__mutmut_10 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_11'] = x__align_core_single_unary_op__mutmut_11 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_12'] = x__align_core_single_unary_op__mutmut_12 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_13'] = x__align_core_single_unary_op__mutmut_13 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_14'] = x__align_core_single_unary_op__mutmut_14 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_15'] = x__align_core_single_unary_op__mutmut_15 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_16'] = x__align_core_single_unary_op__mutmut_16 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_17'] = x__align_core_single_unary_op__mutmut_17 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_18'] = x__align_core_single_unary_op__mutmut_18 # type: ignore # mutmut generated
mutants_x__align_core_single_unary_op__mutmut['x__align_core_single_unary_op__mutmut_19'] = x__align_core_single_unary_op__mutmut_19 # type: ignore # mutmut generated
mutants_x__zip_axes_from_type__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__zip_axes_from_type__mutmut)
def _zip_axes_from_type(
    typ: type[NDFrame], new_axes: Sequence[Index]
) -> dict[str, Index]:
    return {name: new_axes[i] for i, name in enumerate(typ._AXIS_ORDERS)}


def x__zip_axes_from_type__mutmut_orig(
    typ: type[NDFrame], new_axes: Sequence[Index]
) -> dict[str, Index]:
    return {name: new_axes[i] for i, name in enumerate(typ._AXIS_ORDERS)}


def x__zip_axes_from_type__mutmut_1(
    typ: type[NDFrame], new_axes: Sequence[Index]
) -> dict[str, Index]:
    return {name: new_axes[i] for i, name in enumerate(None)}

mutants_x__zip_axes_from_type__mutmut['_mutmut_orig'] = x__zip_axes_from_type__mutmut_orig # type: ignore # mutmut generated
mutants_x__zip_axes_from_type__mutmut['x__zip_axes_from_type__mutmut_1'] = x__zip_axes_from_type__mutmut_1 # type: ignore # mutmut generated
mutants_x__any_pandas_objects__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__any_pandas_objects__mutmut)
def _any_pandas_objects(terms) -> bool:
    """
    Check a sequence of terms for instances of PandasObject.
    """
    return any(isinstance(term.value, PandasObject) for term in terms)


def x__any_pandas_objects__mutmut_orig(terms) -> bool:
    """
    Check a sequence of terms for instances of PandasObject.
    """
    return any(isinstance(term.value, PandasObject) for term in terms)


def x__any_pandas_objects__mutmut_1(terms) -> bool:
    """
    Check a sequence of terms for instances of PandasObject.
    """
    return any(None)

mutants_x__any_pandas_objects__mutmut['_mutmut_orig'] = x__any_pandas_objects__mutmut_orig # type: ignore # mutmut generated
mutants_x__any_pandas_objects__mutmut['x__any_pandas_objects__mutmut_1'] = x__any_pandas_objects__mutmut_1 # type: ignore # mutmut generated


def _filter_special_cases(f) -> Callable[[F], F]:
    @wraps(f)
    def wrapper(terms):
        # single unary operand
        if len(terms) == 1:
            return _align_core_single_unary_op(terms[0])

        term_values = (term.value for term in terms)

        # we don't have any pandas objects
        if not _any_pandas_objects(terms):
            return result_type_many(*term_values), None

        return f(terms)

    return wrapper


@_filter_special_cases
def _align_core(terms):
    term_index = [i for i, term in enumerate(terms) if hasattr(term.value, "axes")]
    term_dims = [terms[i].value.ndim for i in term_index]

    from pandas import Series

    ndims = Series(dict(zip(term_index, term_dims, strict=True)))

    # initial axes are the axes of the largest-axis'd term
    biggest = terms[ndims.idxmax()].value
    typ = biggest._constructor
    axes = biggest.axes
    naxes = len(axes)
    gt_than_one_axis = naxes > 1

    for value in (terms[i].value for i in term_index):
        is_series = isinstance(value, ABCSeries)
        is_series_and_gt_one_axis = is_series and gt_than_one_axis

        for axis, items in enumerate(value.axes):
            if is_series_and_gt_one_axis:
                ax, itm = naxes - 1, value.index
            else:
                ax, itm = axis, items

            if not axes[ax].is_(itm):
                axes[ax] = axes[ax].union(itm)

    for i, ndim in ndims.items():
        for axis, items in zip(range(ndim), axes, strict=False):
            ti = terms[i].value

            if hasattr(ti, "reindex"):
                transpose = isinstance(ti, ABCSeries) and naxes > 1
                reindexer = axes[naxes - 1] if transpose else items

                term_axis_size = len(ti.axes[axis])
                reindexer_size = len(reindexer)

                ordm = np.log10(max(1, abs(reindexer_size - term_axis_size)))
                if (
                    config["mode"]["performance_warnings"]
                    and ordm >= 1
                    and reindexer_size >= 10000
                ):
                    w = (
                        f"Alignment difference on axis {axis} is larger "
                        f"than an order of magnitude on term {terms[i].name!r}, "
                        f"by more than {ordm:.4g}; performance may suffer."
                    )
                    warnings.warn(
                        w, category=PerformanceWarning, stacklevel=find_stack_level()
                    )

                obj = ti.reindex(reindexer, axis=axis)
                terms[i].update(obj)

        terms[i].update(terms[i].value._values)

    return typ, _zip_axes_from_type(typ, axes)
mutants_x_align_terms__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_align_terms__mutmut)
def align_terms(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_orig(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_1(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = None
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_2(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(None)
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_3(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(None))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_4(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = None
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_5(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(None)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_6(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_7(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if (isinstance(terms.value, ABCSeries)) and False else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_8(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if (isinstance(terms.value, ABCSeries)) or True else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_9(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(None, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_10(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, None), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_11(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_12(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, ), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_13(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(None), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_14(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(None):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_15(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = None
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_16(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_17(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if (len(names) == 1) and False else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_18(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if (len(names) == 1) or True else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_19(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) != 1 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_20(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 2 else None

    # perform the main alignment
    typ, axes = _align_core(terms)
    return typ, axes, name


def x_align_terms__mutmut_21(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = None
    return typ, axes, name


def x_align_terms__mutmut_22(terms):
    """
    Align a set of terms.
    """
    try:
        # flatten the parse tree (a nested list, really)
        terms = list(com.flatten(terms))
    except TypeError:
        # can't iterate so it must just be a constant or single variable
        if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
            typ = type(terms.value)
            name = terms.value.name if isinstance(terms.value, ABCSeries) else None
            return typ, _zip_axes_from_type(typ, terms.value.axes), name
        return np.result_type(terms.type), None, None

    # if all resolved variables are numeric scalars
    if all(term.is_scalar for term in terms):
        return result_type_many(*(term.value for term in terms)).type, None, None

    # if all input series have a common name, propagate it to the returned series
    names = {term.value.name for term in terms if isinstance(term.value, ABCSeries)}
    name = names.pop() if len(names) == 1 else None

    # perform the main alignment
    typ, axes = _align_core(None)
    return typ, axes, name

mutants_x_align_terms__mutmut['_mutmut_orig'] = x_align_terms__mutmut_orig # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_1'] = x_align_terms__mutmut_1 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_2'] = x_align_terms__mutmut_2 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_3'] = x_align_terms__mutmut_3 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_4'] = x_align_terms__mutmut_4 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_5'] = x_align_terms__mutmut_5 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_6'] = x_align_terms__mutmut_6 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_7'] = x_align_terms__mutmut_7 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_8'] = x_align_terms__mutmut_8 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_9'] = x_align_terms__mutmut_9 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_10'] = x_align_terms__mutmut_10 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_11'] = x_align_terms__mutmut_11 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_12'] = x_align_terms__mutmut_12 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_13'] = x_align_terms__mutmut_13 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_14'] = x_align_terms__mutmut_14 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_15'] = x_align_terms__mutmut_15 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_16'] = x_align_terms__mutmut_16 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_17'] = x_align_terms__mutmut_17 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_18'] = x_align_terms__mutmut_18 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_19'] = x_align_terms__mutmut_19 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_20'] = x_align_terms__mutmut_20 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_21'] = x_align_terms__mutmut_21 # type: ignore # mutmut generated
mutants_x_align_terms__mutmut['x_align_terms__mutmut_22'] = x_align_terms__mutmut_22 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_reconstruct_object__mutmut)
def reconstruct_object(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_orig(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_1(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = None
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_2(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = None

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_3(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(None, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_4(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, None)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_5(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_6(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, )

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_7(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) or issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_8(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_9(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(None, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_10(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, None):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_11(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_12(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, ):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_13(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is not None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_14(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(None, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_15(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=None, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_16(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_17(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_18(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, )
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_19(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(None, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_20(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=None, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_21(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=None, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_22(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_23(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_24(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_25(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, )

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_26(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ or res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_27(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") or typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_28(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(None, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_29(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, None) and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_30(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr("type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_31(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, ) and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_32(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "XXtypeXX") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_33(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "TYPE") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_34(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ != np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_35(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t == np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_36(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = None
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_37(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(None)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_38(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = None
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_39(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(None)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_40(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1 or not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_41(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1 or len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_42(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) != 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_43(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 2
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_44(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) != 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_45(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 2
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_46(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(res_t)

    return ret_value


def x_reconstruct_object__mutmut_47(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = None

    return ret_value


def x_reconstruct_object__mutmut_48(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array([ret_value]).astype(None)

    return ret_value


def x_reconstruct_object__mutmut_49(typ, obj, axes, dtype, name):
    """
    Reconstruct an object given its type, raw value, and possibly empty
    (None) axes.

    Parameters
    ----------
    typ : object
        A type
    obj : object
        The value to use in the type constructor
    axes : dict
        The axes to use to construct the resulting pandas object

    Returns
    -------
    ret : typ
        An object of type ``typ`` with the value `obj` and possible axes
        `axes`.
    """
    try:
        typ = typ.type
    except AttributeError:
        pass

    res_t = np.result_type(obj.dtype, dtype)

    if not isinstance(typ, partial) and issubclass(typ, PandasObject):
        if name is None:
            return typ(obj, dtype=res_t, **axes)
        return typ(obj, dtype=res_t, name=name, **axes)

    # special case for pathological things like ~True/~False
    if hasattr(res_t, "type") and typ == np.bool_ and res_t != np.bool_:
        ret_value = res_t.type(obj)
    else:
        ret_value = res_t.type(obj)
        # The condition is to distinguish 0-dim array (returned in case of
        # scalar) and 1 element array
        # e.g. np.array(0) and np.array([0])
        if (
            len(obj.shape) == 1
            and len(obj) == 1
            and not isinstance(ret_value, np.ndarray)
        ):
            ret_value = np.array(None).astype(res_t)

    return ret_value

mutants_x_reconstruct_object__mutmut['_mutmut_orig'] = x_reconstruct_object__mutmut_orig # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_1'] = x_reconstruct_object__mutmut_1 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_2'] = x_reconstruct_object__mutmut_2 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_3'] = x_reconstruct_object__mutmut_3 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_4'] = x_reconstruct_object__mutmut_4 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_5'] = x_reconstruct_object__mutmut_5 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_6'] = x_reconstruct_object__mutmut_6 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_7'] = x_reconstruct_object__mutmut_7 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_8'] = x_reconstruct_object__mutmut_8 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_9'] = x_reconstruct_object__mutmut_9 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_10'] = x_reconstruct_object__mutmut_10 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_11'] = x_reconstruct_object__mutmut_11 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_12'] = x_reconstruct_object__mutmut_12 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_13'] = x_reconstruct_object__mutmut_13 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_14'] = x_reconstruct_object__mutmut_14 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_15'] = x_reconstruct_object__mutmut_15 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_16'] = x_reconstruct_object__mutmut_16 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_17'] = x_reconstruct_object__mutmut_17 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_18'] = x_reconstruct_object__mutmut_18 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_19'] = x_reconstruct_object__mutmut_19 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_20'] = x_reconstruct_object__mutmut_20 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_21'] = x_reconstruct_object__mutmut_21 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_22'] = x_reconstruct_object__mutmut_22 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_23'] = x_reconstruct_object__mutmut_23 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_24'] = x_reconstruct_object__mutmut_24 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_25'] = x_reconstruct_object__mutmut_25 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_26'] = x_reconstruct_object__mutmut_26 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_27'] = x_reconstruct_object__mutmut_27 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_28'] = x_reconstruct_object__mutmut_28 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_29'] = x_reconstruct_object__mutmut_29 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_30'] = x_reconstruct_object__mutmut_30 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_31'] = x_reconstruct_object__mutmut_31 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_32'] = x_reconstruct_object__mutmut_32 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_33'] = x_reconstruct_object__mutmut_33 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_34'] = x_reconstruct_object__mutmut_34 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_35'] = x_reconstruct_object__mutmut_35 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_36'] = x_reconstruct_object__mutmut_36 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_37'] = x_reconstruct_object__mutmut_37 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_38'] = x_reconstruct_object__mutmut_38 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_39'] = x_reconstruct_object__mutmut_39 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_40'] = x_reconstruct_object__mutmut_40 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_41'] = x_reconstruct_object__mutmut_41 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_42'] = x_reconstruct_object__mutmut_42 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_43'] = x_reconstruct_object__mutmut_43 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_44'] = x_reconstruct_object__mutmut_44 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_45'] = x_reconstruct_object__mutmut_45 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_46'] = x_reconstruct_object__mutmut_46 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_47'] = x_reconstruct_object__mutmut_47 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_48'] = x_reconstruct_object__mutmut_48 # type: ignore # mutmut generated
mutants_x_reconstruct_object__mutmut['x_reconstruct_object__mutmut_49'] = x_reconstruct_object__mutmut_49 # type: ignore # mutmut generated
