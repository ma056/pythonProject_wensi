# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : 22.py
@Author : wenjing
@Date : 2022/12/7 11:22
"""
# SELECT contact_id, environment, background, greetingplayed, oneforma_id, call_type, mobile_type, voip, system_phone_number, customer_phone_number, disconnect_timestamp, contact_duration, country, call_center, audio_length, speech_length FROM contact_info where is_upload = 0 and is_attr_get = 1 and is_search_get =1 and is_calculated = 1;
#
# SELECT contact_id, attr_json, contact_attr_dict, country, call_center, audio_length, speech_length FROM call_center where is_upload = 0 and is_attr_get = 1 and is_search_get =1 and is_calculated = 1;
[{'contact_id': '428db625-316b-4d1f-8149-e70ed24f9270',
  'contact_info': {'contactid': '428db625-316b-4d1f-8149-e70ed24f9270', 'environment': '', 'background': '1',
                   'greetingplayed': 'true', 'oneforma_id': '98882', 'call_type': '2', 'mobile_type': '2', 'voip': '1',
                   'date': '2022-11-25 05:26:31', 'telephone_number': 'Anonymous', 'System_phone_number': '14158396178',
                   'Contact_duration': ''},
  'country': 'VMIDENSP',
  'call_center': 'US',
  'audio_length': 0.91,
  'speech_length': 0.0},
 {'contact_id': '61ccfcba-61c6-4962-a8a8-49a899f8a56e',
  'contact_info': {'contactid': '61ccfcba-61c6-4962-a8a8-49a899f8a56e', 'environment': '',
                   'background': '', 'greetingplayed': 'true', 'oneforma_id': '62',
                   'call_type': 'Timeout', 'mobile_type': '666666', 'voip': '',
                   'date': '2022-11-25 05:30:36', 'telephone_number': 'Anonymous',
                   'System_phone_number': '12053642572', 'Contact_duration': '0'},
  'country': 'Default',
  'call_center': 'US',
  'audio_length': 23.04,
  'speech_length': 14.28}]
