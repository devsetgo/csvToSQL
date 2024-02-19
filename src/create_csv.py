# -*- coding: utf-8 -*-
from tqdm import tqdm
import random
from datetime import datetime, timedelta
import csv

login_names = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6', 'user7', 'user8', 'user9', 'user10', 'user11', 'user12', 'user13', 'user14', 'user15', 'user16', 'user17', 'user18', 'user19', 'user20', 'user21', 'user22', 'user23', 'user24', 'user25', 'user26', 'user27', 'user28', 'user29', 'user30', 'user31', 'user32', 'user33', 'user34', 'user35', 'user36', 'user37', 'user38', 'user39', 'user40', 'user41', 'user42', 'user43', 'user44', 'user45', 'user46', 'user47', 'user48', 'user49', 'user50', 'user51', 'user52', 'user53', 'user54', 'user55', 'user56', 'user57', 'user58', 'user59', 'user60', 'user61', 'user62', 'user63', 'user64', 'user65', 'user66', 'user67', 'user68', 'user69', 'user70', 'user71', 'user72', 'user73', 'user74', 'user75', 'user76', 'user77', 'user78', 'user79', 'user80', 'user81', 'user82', 'user83', 'user84', 'user85', 'user86', 'user87', 'user88', 'user89', 'user90', 'user91', 'user92', 'user93', 'user94', 'user95', 'user96', 'user97', 'user98', 'user99', 'user100']
host_name = ['host1', 'host2', 'host3', 'host4', 'host5', 'host6', 'host7', 'host8', 'host9', 'host10', 'host11', 'host12', 'host13', 'host14', 'host15', 'host16', 'host17', 'host18', 'host19', 'host20', 'host21', 'host22', 'host23', 'host24', 'host25', 'host26', 'host27', 'host28', 'host29', 'host30', 'host31', 'host32', 'host33', 'host34', 'host35', 'host36', 'host37', 'host38', 'host39', 'host40', 'host41', 'host42', 'host43', 'host44', 'host45', 'host46', 'host47', 'host48', 'host49', 'host50', 'host51', 'host52', 'host53', 'host54', 'host55', 'host56', 'host57', 'host58', 'host59', 'host60', 'host61', 'host62', 'host63', 'host64', 'host65', 'host66', 'host67', 'host68', 'host69', 'host70', 'host71', 'host72', 'host73', 'host74', 'host75', 'host76', 'host77', 'host78', 'host79', 'host80', 'host81', 'host82', 'host83', 'host84', 'host85', 'host86', 'host87', 'host88', 'host89', 'host90', 'host91', 'host92', 'host93', 'host94', 'host95', 'host96', 'host97', 'host98', 'host99', 'host100']
database_name = ['database_1', 'database_2', 'database_3', 'database_4', 'database_5', 'database_6', 'database_7', 'database_8', 'database_9', 'database_10', 'database_11', 'database_12', 'database_13', 'database_14', 'database_15', 'database_16', 'database_17', 'database_18', 'database_19', 'database_20', 'database_21', 'database_22', 'database_23', 'database_24', 'database_25', 'database_26', 'database_27', 'database_28', 'database_29', 'database_30', 'database_31', 'database_32', 'database_33', 'database_34', 'database_35', 'database_36', 'database_37', 'database_38', 'database_39', 'database_40', 'database_41', 'database_42', 'database_43', 'database_44', 'database_45', 'database_46', 'database_47', 'database_48', 'database_49', 'database_50', 'database_51', 'database_52', 'database_53', 'database_54', 'database_55', 'database_56', 'database_57', 'database_58', 'database_59', 'database_60', 'database_61', 'database_62', 'database_63', 'database_64', 'database_65', 'database_66', 'database_67', 'database_68', 'database_69', 'database_70', 'database_71', 'database_72', 'database_73', 'database_74', 'database_75', 'database_76', 'database_77', 'database_78', 'database_79', 'database_80', 'database_81', 'database_82', 'database_83', 'database_84', 'database_85', 'database_86', 'database_87', 'database_88', 'database_89', 'database_90', 'database_91', 'database_92', 'database_93', 'database_94', 'database_95', 'database_96', 'database_97', 'database_98', 'database_99', 'database_100', 'database_101', 'database_102', 'database_103', 'database_104', 'database_105', 'database_106', 'database_107', 'database_108', 'database_109', 'database_110', 'database_111', 'database_112', 'database_113', 'database_114', 'database_115', 'database_116', 'database_117', 'database_118', 'database_119', 'database_120', 'database_121', 'database_122', 'database_123', 'database_124', 'database_125', 'database_126', 'database_127', 'database_128', 'database_129', 'database_130', 'database_131', 'database_132', 'database_133', 'database_134', 'database_135', 'database_136', 'database_137', 'database_138', 'database_139', 'database_140', 'database_141', 'database_142', 'database_143', 'database_144', 'database_145', 'database_146', 'database_147', 'database_148', 'database_149', 'database_150', 'database_151', 'database_152', 'database_153', 'database_154', 'database_155', 'database_156', 'database_157', 'database_158', 'database_159', 'database_160', 'database_161', 'database_162', 'database_163', 'database_164', 'database_165', 'database_166', 'database_167', 'database_168', 'database_169', 'database_170', 'database_171', 'database_172', 'database_173', 'database_174', 'database_175', 'database_176', 'database_177', 'database_178', 'database_179', 'database_180', 'database_181', 'database_182', 'database_183', 'database_184', 'database_185', 'database_186', 'database_187', 'database_188', 'database_189', 'database_190', 'database_191', 'database_192', 'database_193', 'database_194', 'database_195', 'database_196', 'database_197', 'database_198', 'database_199', 'database_200']
program_name = ['program1', 'program2', 'program3', 'program4', 'program5', 'program6', 'program7', 'program8', 'program9', 'program10', 'program11', 'program12', 'program13', 'program14', 'program15', 'program16', 'program17', 'program18', 'program19', 'program20', 'program21', 'program22', 'program23', 'program24', 'program25', 'program26', 'program27', 'program28', 'program29', 'program30', 'program31', 'program32', 'program33', 'program34', 'program35', 'program36', 'program37', 'program38', 'program39', 'program40', 'program41', 'program42', 'program43', 'program44', 'program45', 'program46', 'program47', 'program48', 'program49', 'program50', 'program51', 'program52', 'program53', 'program54', 'program55', 'program56', 'program57', 'program58', 'program59', 'program60', 'program61', 'program62', 'program63', 'program64', 'program65', 'program66', 'program67', 'program68', 'program69', 'program70', 'program71', 'program72', 'program73', 'program74', 'program75', 'program76', 'program77', 'program78', 'program79', 'program80', 'program81', 'program82', 'program83', 'program84', 'program85', 'program86', 'program87', 'program88', 'program89', 'program90', 'program91', 'program92', 'program93', 'program94', 'program95', 'program96', 'program97', 'program98', 'program99', 'program100', 'program101', 'program102', 'program103', 'program104', 'program105', 'program106', 'program107', 'program108', 'program109', 'program110', 'program111', 'program112', 'program113', 'program114', 'program115', 'program116', 'program117', 'program118', 'program119', 'program120', 'program121', 'program122', 'program123', 'program124', 'program125', 'program126', 'program127', 'program128', 'program129', 'program130', 'program131', 'program132', 'program133', 'program134', 'program135', 'program136', 'program137', 'program138', 'program139', 'program140', 'program141', 'program142', 'program143', 'program144', 'program145', 'program146', 'program147', 'program148', 'program149', 'program150']
keywords = ['keyword_1', 'keyword_2', 'keyword_3', 'keyword_4', 'keyword_5', 'keyword_6', 'keyword_7', 'keyword_8', 'keyword_9', 'keyword_10', 'keyword_11', 'keyword_12', 'keyword_13', 'keyword_14', 'keyword_15', 'keyword_16', 'keyword_17', 'keyword_18', 'keyword_19', 'keyword_20', 'keyword_21', 'keyword_22', 'keyword_23', 'keyword_24', 'keyword_25', 'keyword_26', 'keyword_27', 'keyword_28', 'keyword_29', 'keyword_30', 'keyword_31', 'keyword_32', 'keyword_33', 'keyword_34', 'keyword_35', 'keyword_36', 'keyword_37', 'keyword_38', 'keyword_39', 'keyword_40', 'keyword_41', 'keyword_42', 'keyword_43', 'keyword_44', 'keyword_45', 'keyword_46', 'keyword_47', 'keyword_48', 'keyword_49', 'keyword_50', 'keyword_51', 'keyword_52', 'keyword_53', 'keyword_54', 'keyword_55', 'keyword_56', 'keyword_57', 'keyword_58', 'keyword_59', 'keyword_60', 'keyword_61', 'keyword_62', 'keyword_63', 'keyword_64', 'keyword_65', 'keyword_66', 'keyword_67', 'keyword_68', 'keyword_69', 'keyword_70', 'keyword_71', 'keyword_72', 'keyword_73', 'keyword_74', 'keyword_75', 'keyword_76', 'keyword_77', 'keyword_78', 'keyword_79', 'keyword_80', 'keyword_81', 'keyword_82', 'keyword_83', 'keyword_84', 'keyword_85', 'keyword_86', 'keyword_87', 'keyword_88', 'keyword_89', 'keyword_90', 'keyword_91', 'keyword_92', 'keyword_93', 'keyword_94', 'keyword_95', 'keyword_96', 'keyword_97', 'keyword_98', 'keyword_99', 'keyword_100', 'keyword_101', 'keyword_102', 'keyword_103', 'keyword_104', 'keyword_105', 'keyword_106', 'keyword_107', 'keyword_108', 'keyword_109', 'keyword_110', 'keyword_111', 'keyword_112', 'keyword_113', 'keyword_114', 'keyword_115', 'keyword_116', 'keyword_117', 'keyword_118', 'keyword_119', 'keyword_120', 'keyword_121', 'keyword_122', 'keyword_123', 'keyword_124', 'keyword_125', 'keyword_126', 'keyword_127', 'keyword_128', 'keyword_129', 'keyword_130', 'keyword_131', 'keyword_132', 'keyword_133', 'keyword_134', 'keyword_135', 'keyword_136', 'keyword_137', 'keyword_138', 'keyword_139', 'keyword_140', 'keyword_141', 'keyword_142', 'keyword_143', 'keyword_144', 'keyword_145', 'keyword_146', 'keyword_147', 'keyword_148', 'keyword_149', 'keyword_150', 'keyword_151', 'keyword_152', 'keyword_153', 'keyword_154', 'keyword_155', 'keyword_156', 'keyword_157', 'keyword_158', 'keyword_159', 'keyword_160', 'keyword_161', 'keyword_162', 'keyword_163', 'keyword_164', 'keyword_165', 'keyword_166', 'keyword_167', 'keyword_168', 'keyword_169', 'keyword_170', 'keyword_171', 'keyword_172', 'keyword_173', 'keyword_174', 'keyword_175', 'keyword_176', 'keyword_177', 'keyword_178', 'keyword_179', 'keyword_180', 'keyword_181', 'keyword_182', 'keyword_183', 'keyword_184', 'keyword_185', 'keyword_186', 'keyword_187', 'keyword_188', 'keyword_189', 'keyword_190', 'keyword_191', 'keyword_192', 'keyword_193', 'keyword_194', 'keyword_195', 'keyword_196', 'keyword_197', 'keyword_198', 'keyword_199', 'keyword_200']

import random
from datetime import datetime, timedelta
import string


def create_list(qty=100):
    session_list = []
    headers = ['session_id', 'sql_text', 'login_name', 'host_name', 'database_name', 'program_name', 'start_time', 'login_time', 'request_id', 'collection_time', 'sql_text_unique_id', 'released_to_css', 'keywords']
    session_list.append(headers)
    
    count = 10
    for _ in tqdm(range(qty), desc="Creating list"):
        start_time = datetime(2023, 9, 1) + timedelta(days=random.randint(0, 154))  # random date between 2023-09-01 and 2024-02-01
        count += 1
        session = [
            count,  # assuming session_id is a 4-digit number
            generate_random_string(random.randint(100, 3000)),  # random number of characters between 100 and 4000
            random.choice(login_names),
            random.choice(host_name),
            random.choice(database_name),
            random.choice(program_name),
            start_time,
            start_time,  # same as start_time
            str(random.randint(1000, 9999)),  # assuming request_id is a 4-digit number
            start_time,  # same as start_time
            str(random.randint(1000, 9999)),  # assuming sql_text_unique_id is a 4-digit number
            'Y',
            random.sample(keywords, random.randint(1, 30)),  # select between 1 and 30 keywords
        ]
        session_list.append(session)
    return session_list

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))



def save_csv(data, filename="sessions.csv"):
    import csv
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    print(f"File saved as {filename}")

# def create_list(qty=100):
#     # session_id: The unique identifier for the session
#     # sql_text: The SQL query text should contain select, insert, update, delete, create, alter, drop, or truncate and be between 100 and 4000 characters
#     # login_name: The username used for login (randomly selected from the list of login_names)
#     # host_name: The name of the host machine selected from the list of host_names
#     # database_name: The name of the database selected from the list of database_names
#     # program_name: The name of the program selected from the list of program_names
#     # start_time: The time when the session started random date between 2023-09-01 and 2024-02-01
#     # login_time: The time when the user logged in should be the same as the start_time
#     # request_id: The unique identifier for the request
#     # collection_time: The time when the data was collected should be the same as the start_time
#     # sql_text_unique_id: The unique identifier for the SQL text
#     # released_to_css: should always be 'Y'
#     # keywords: Should contain between 1 and 30 keywords selected from the list of keywords


def create_login_names(qty=150):
    return [f"program{i}" for i in range(1, qty + 1)]




if __name__ == "__main__":
    data = create_list(qty=10640000) #10640000
    print(len(data))
    save_csv(data, filename="sessions.csv")
#     login_names = create_login_names()
#     print(login_names)