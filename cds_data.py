# import cdsapi

# c = cdsapi.Client()

# c.retrieve(
#     'sis-biodiversity-cmip5-global',
#     {
#         'version': '1.0',
#         'format': 'zip',
#         'temporal_aggregation': 'monthly',
#         'experiment': 'rcp4_5',
#         'ensemble_member': 'r1i1p1',
#         'model': 'bcc_csm1_1_m',
#         'derived_variable': 'monthly_mean',
#         'variable': [
#             '2m_temperature', 'precipitation',
#         ],
#     },
#     'raw_data/download_temp_precip.zip')


import cdsapi

c = cdsapi.Client()

c.retrieve(
    'sis-biodiversity-cmip5-global',
    {
        'version': '1.0',
        'format': 'zip',
        'variable': [
            'cloud_cover', 'water_vapor_pressure',
        ],
        'derived_variable': 'monthly_mean',
        'model': 'bcc_csm1_1_m',
        'ensemble_member': 'r1i1p1',
        'experiment': 'rcp4_5',
        'temporal_aggregation': 'monthly',
    },
    'download_cloud_water.zip')
