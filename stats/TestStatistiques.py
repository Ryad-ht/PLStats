from scipy import stats
import frofromscipy import stats
import numpy
from typing import Tuple
import pandas as pd


class TestStatistiques:

    def __init__(self) -> None:
        pass

    @staticmethod
    def t_test_independant(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.ttest_ind(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def mann_and_whitney_test(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.mannwhitneyu(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def normality_test(variable) -> Tuple[float, float]:
        stat_value, p_value = stats.shapiro(variable)
        return stat_value, p_value

    @staticmethod
    def anova(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.f_oneway(*sample)
        return stat_value, p_value

    @staticmethod
    def kruskal_wallis(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.kruskal(*sample)
        return stat_value, p_value

    @staticmethod
    def post_hoc_tukey(*sample):
        tukey_instance = stats.tukey_hsd(*sample)
        return tukey_instance

    @staticmethod
    def t_test_apparie(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.ttest_rel(variable_1, variable_2)
            return stat_value, p_value

    @staticmethod
    def wilcoxon_apparai_rang_signe(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.wilcoxon(variable_1, variable_2)
            return stat_value, p_value


class DataType:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.clean = None

    def _change_comma_to_point(self) -> pd.DataFrame:
        for i in self.df.columns:
            for idx, j in enumerate(self.df[i]):
                try:
                    new = j.replace(',', '.')
                    self.df[i][idx] = new
                except:
                    pass
        return self.df

    def _change_type(self) -> pd.DataFrame:
        for i in self.df.columns:
            if isinstance(self.df[i].dtype, object):
                try:
                    self.df[i] = self.df[i].astype(float)
                except:
                    pass
        new = self.df.copy()
        return new

    @staticmethod
    def _search_modalite(df, col):
        if isinstance(df[col][0], str):
            modalite = df[col].unique()
        else:
            modalite = []
        return modalite, len(modalite)

    def colonne_setter(self) -> list:
        self._change_comma_to_point()
        df = self._change_type()
        colonne = df.columns
        collone_liste = []
        for col in colonne:
            if isinstance(df[col][0], (int, float)):
                modalite, nb_modalite = self._search_modalite(df, col)
                collone_liste.append({
                    'name': col,
                    'type': 'numeric',
                    'modalite': modalite,
                    'nb_modalite': nb_modalite
                })
            elif isinstance(self.df[col][0], str):
                modalite, nb_modalite = self._search_modalite(df, col)
                collone_liste.append({
                    'name': col,
                    'type': 'qualitative',
                    'modalite': modalite,
                    'nb_modalite': nb_modalite
                })
        return collone_listefrom scipy import stats


import numpy
from typing import Tuple
import pandas as pd


class TestStatistiques:

    def __init__(self) -> None:
        pass

    @staticmethod
    def t_test_independant(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.ttest_ind(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def mann_and_whitney_test(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.mannwhitneyu(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def normality_test(variable) -> Tuple[float, float]:
        stat_value, p_value = stats.shapiro(variable)
        return stat_value, p_value

    @staticmethod
    def anova(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.f_oneway(*sample)
        return stat_value, p_value

    @staticmethod
    def kruskal_wallis(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.kruskal(*sample)
        return stat_value, p_value

    @staticmethod
    def post_hoc_tukey(*sample):
        tukey_instance = stats.tukey_hsd(*sample)
        return tukey_instance

    @staticmethod
    def t_test_apparie(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.ttest_rel(variable_1, variable_2)
            return stat_value, p_value

    @staticmethod
    def wilcoxon_apparai_rang_signe(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.wilcoxon(variable_1, variable_2)
            return stat_value, p_value


class DataType:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.clean = None

    def _change_comma_to_point(self) -> pd.DataFrame:
        for i in self.df.columns:
            for idx, j in enumerate(self.df[i]):
                try:
                    new = j.replace(',', '.')
                    self.df[i][idx] = new
                except:
                    pass
        return self.df

    def _change_type(self) -> pd.DataFrame:
        for i in self.df.columns:
            if isinstance(self.df[i].dtype, object):
                try:
                    self.df[i] = self.df[i].astype(float)
                except:
                    pass
        new = self.df.copy()
        return new

    @staticmethod
    def _search_modalite(df, col):
        if isinstance(df[col][0], str):
            modalite = df[col].unique()
        else:
            modalite = []
        return modalite, len(modalite)

    def colonne_setter(self) -> list:
        self._change_comma_to_point()
        df = self._change_type()
        colonne = df.columns
        collone_liste = []
        for col in colonne:
            collone_liste.append({
                'name': col,
                'type': 'numeric',
                'modalite': modalite,
                'nb_modalite': nb_modalite
            })
            elif isinstance(self.df[col][0], str):
            modalite, nb_modalite = self._search_modalite(df, col)
            collone_liste.append({
                'name': col,
                'type': 'qualitative',
                'modalite': modalite,
                'nb_modalite': nb_modalite
            })


return collone_listem
scipy
import stats

import numpy
from typing import Tuple
import pandas as pd


class TestStatistiques:

    def __init__(self) -> None:
        pass

    @staticmethod
    def t_test_independant(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.ttest_ind(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def mann_and_whitney_test(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.mannwhitneyu(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def normality_test(variable) -> Tuple[float, float]:
        stat_value, p_value = stats.shapiro(variable)
        return stat_value, p_value

    @staticmethod
    def anova(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.f_oneway(*sample)
        return stat_value, p_value

    @staticmethod
    def kruskal_wallis(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.kruskal(*sample)
        return stat_value, p_value

    @staticmethod
    def post_hoc_tukey(*sample):
        tukey_instance = stats.tukey_hsd(*sample)
        return tukey_instance

    @staticmethod
    def t_test_apparie(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.ttest_rel(variable_1, variable_2)
            return stat_value, p_value

    @staticmethod
    def wilcoxon_apparai_rang_signe(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.wilcoxon(variable_1, variable_2)
            return stat_value, p_value


class DataType:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.clean = None

    def _change_comma_to_point(self) -> pd.DataFrame:
        for i in self.df.columns:
            for idx, j in enumerate(self.df[i]):
                try:
                    new = j.replace(',', '.')
                    self.df[i][idx] = new
                except:
                    pass
        return self.df

    def _change_type(self) -> pd.DataFrame:
        for i in self.df.columns:
            if isinstance(self.df[i].dtype, object):
                try:
                    self.df[i] = self.df[i].astype(float)
                except:
                    pass
        new = self.df.copy()
        return new

    @staticmethod
    def _search_modalite(df, col):
        if isinstance(df[col][0], str):
            modalite = df[col].unique()
        else:
            modalite = []
        return modalite, len(modalite)

    def colonne_setter(self) -> list:
        self._change_comma_to_point()
        df = self._change_type()
        colonne = df.columns
        collone_liste = []
        for col in colonne:
            if isinstance(df[col][0], (int, float)):
                modalite, nb_modalite = self._search_modalite(df, col)
                collone_liste.append({
                    'name': col,
                    'type': 'numeric',
                    'modalite': modalite,
                    'nb_modalite': nb_modalite
                })
            elif isinstance(self.df[col][0], str):
                modalite, nb_modalite = self._search_modalite(df, col)
                collone_liste.append({
                    'name': col,
                    'type': 'qualitative',
                    'modalite': modalite,
                    'nb_modalite': nb_modalite
                })
        return collone_listenumpy


from typing import Tuple
import pandas as pd


class TestStatistiques:

    def __init__(self) -> None:
        pass

    @staticmethod
    def t_test_independant(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.ttest_ind(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def mann_and_whitney_test(
            variable_1: numpy.ndarray,
            variable_2: numpy.ndarray
    ) -> Tuple[float, float]:
        stat_value, p_value = stats.mannwhitneyu(
            variable_1,
            variable_2
        )
        return stat_value, p_value

    @staticmethod
    def normality_test(variable) -> Tuple[float, float]:
        stat_value, p_value = stats.shapiro(variable)
        return stat_value, p_value

    @staticmethod
    def anova(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.f_oneway(*sample)
        return stat_value, p_value

    @staticmethod
    def kruskal_wallis(*sample) -> Tuple[float, float]:
        stat_value, p_value = stats.kruskal(*sample)
        return stat_value, p_value

    @staticmethod
    def post_hoc_tukey(*sample):
        tukey_instance = stats.tukey_hsd(*sample)
        return tukey_instance

    @staticmethod
    def t_test_apparie(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.ttest_rel(variable_1, variable_2)
            return stat_value, p_value

    @staticmethod
    def wilcoxon_apparai_rang_signe(variable_1, variable_2, raise_error: bool = False) -> Tuple[float, float]:
        if raise_error:
            if len(variable_1) != len(variable_2):
                raise ValueError("Les longeurs des echantillons doivent être identiques")
        else:
            stat_value, p_value = stats.wilcoxon(variable_1, variable_2)
            return stat_value, p_value


class DataType:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.clean = None

    def _change_comma_to_point(self) -> pd.DataFrame:
        for i in self.df.columns:
            for idx, j in enumerate(self.df[i]):
                try:
                    new = j.replace(',', '.')
                    self.df[i][idx] = new
                except:
                    pass
        return self.df

    def _change_type(self) -> pd.DataFrame:
        for i in self.df.columns:
            if isinstance(self.df[i].dtype, object):
                try:
                    self.df[i] = self.df[i].astype(float)
                except:
                    pass
        new = self.df.copy()
        return new

    @staticmethod
    def _search_modalite(df, col):
        if isinstance(df[col][0], str):
            modalite = df[col].unique()
        else:
            modalite = []
        return modalite, len(modalite)

    def colonne_setter(self) -> list:
        self._change_comma_to_point()
        df = self._change_type()
        colonne = df.columns
        collone_liste = []
        for col in colonne:
            if isinstance(df[col][0], (int, float)):
                modalite, nb_modalite = self._search_modalite(df, col)
                collone_liste.append({
                    'name': col,
                    'type': 'numeric',
                    'modalite': modalite,
                    'nb_modalite': nb_modalite
                })
            elif isinstance(self.df[col][0], str):
                modalite, nb_modalite = self._search_modalite(df, col)
                collone_liste.append({
                    'name': col,
                    'type': 'qualitative',
                    'modalite': modalite,
                    'nb_modalite': nb_modalite
                })
        return collone_liste
        if isinstance(df[col][0], (int, float)):
                modalite, nb_modalite = self._search_modalite(df, col)
