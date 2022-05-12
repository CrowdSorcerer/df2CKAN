import pandas as pd
from io import BytesIO


def df_to_xml(data_frame: pd.DataFrame):
    return data_frame.to_xml(path_or_buffer=None, index=True, root_name='data', row_name='row', na_rep=None,
                             attr_cols=None,
                             elem_cols=None, namespaces=None, prefix=None, encoding='utf-8', xml_declaration=True,
                             pretty_print=True, parser='etree', stylesheet=None, compression='infer',
                             storage_options=None)


def df_to_csv(data_frame: pd.DataFrame):
    return data_frame.to_csv(index=False)


def df_to_json(data_frame: pd.DataFrame):
    return data_frame.to_json(orient='records')


def df_to_excel(data_frame: pd.DataFrame):
    # Create an in memory binary file object, and write the dataframe to it.
    in_memory_fp = BytesIO()
    data_frame.to_excel(in_memory_fp)
    return in_memory_fp
