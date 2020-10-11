from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import os, re
import argparse, json, platform, time
from urllib.parse import unquote
import hashlib
server_url = '103.208.222.5:23456'

try:
    import file_split_merge
    import requests_cache
except:
    os.system('pip install file_split_merge')
    os.system('pip install requests-cache')
    os.system('pip3 install file_split_merge')
    os.system('pip3 install requests-cache')
    import file_split_merge
    import requests_cache

requests_cache.install_cache()
requests_cache.clear()
requests_cache.core.install_cache(cache_name='ani-dl.cache' , expire_after=3600 , allowable_codes=[200] )

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

try:
    from pyfiglet import Figlet

    f = Figlet(font='banner3-D', width=259)
    print(f.renderText('ANI - DL . py'))
except:
    os.system('pip install pyfiglet')
    os.system('pip3 install pyfiglet')
    from pyfiglet import Figlet

    f = Figlet(font='banner3-D', width=259)
    print(f.renderText('ANI - DL . py'))

try:
    import requests
    from sqlitedict import SqliteDict
    from bs4 import BeautifulSoup
    import pickle
    from sqlitedict import SqliteDict
    from tqdm import tqdm
except:
    os.system("pip install requests")
    os.system("pip install sqlitedict")
    os.system("pip install beautifulsoup4")
    os.system("pip install sqlitedict")
    os.system('pip install file-split-merge')
    os.system('pip install tqdm')
    os.system("pip3 install requests")
    os.system("pip3 install sqlitedict")
    os.system("pip3 install beautifulsoup4")
    os.system("pip3 install sqlitedict")
    os.system('pip3 install file-split-merge')
    os.system('pip3 install tqdm')
    import requests
    from sqlitedict import SqliteDict
    from bs4 import BeautifulSoup
    import pickle
    from tqdm import tqdm


def replace_name_for_window(text):
    text = text.replace('&', ' ')
    text = text.replace('|', ' ')
    text = text.replace('<', ' ')
    text = text.replace('>', ' ')
    text = text.replace('~', ' ')
    text = text.replace('/', ' ')
    text = text.replace('?', ' ')
    text = text.replace(':', ' ')
    text = text.replace('\\', ' ')
    text = text.replace('*', ' ')
    text = text.replace('"', ' ')
    text = text.replace("'", ' ')
    text = text.replace('&', ' ')
    text = text.replace('&', ' ')
    text = text.replace('&', ' ')
    text = text.replace('&', ' ')
    text = text.replace('&', ' ')
    return text


def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def config_save(config, config_path):
    try:
        os.remove(config_path)
    except:
        pass
    pickle.dump(config, open(config_path, 'wb'))


def config_load(config_path):
    return pickle.load(open(config_path, 'rb'))


kor = re.compile('[가-힇]')


def isKorean(text):
    if re.findall(kor, text): return True


def showRename(show):
    # show = item['data']['title'].replace('\n','   |   ')
    tmp = show.split('\n')
    for index, item in enumerate(tmp):
        if isKorean(item):
            result = item + "  "
            for index2, item in enumerate(tmp):
                if index != index2:
                    result = result + "|  " + item + '  '
            return result
    return show.replace('\n', '   |   ')


def main_cycle(j=None):
    clear()
    print("이제 무엇을 하시겠습니까?\n"
          "1. 최신 애니메이션 조회\n"
          "2. 저장 경로 변경\n"
          "3. 자동 다운로드 설정(특정 키워드 다운)\n"
          "4. 자동 다운로드 설정법에 대해서 알아보기\n"
          "5. 불러올 최신 에피소드 숫자 재지정\n"
          "6. 최신 애니메이션 조회(1)시 리스트에 뜨는 애니메이션 숫자 조절\n"
          "7. 불러온 리스트에서 키워드로 찾기\n"
          "8. 최신 애니메이션 N 개 다운로드\n"
          "9. 자동 다운로드 시작하기\n"
          "10. 다운로드 완료 후 리네이밍 설정하기\n"
          "11. 네트워크 설정\n"
          "12. 다운완료 DB 수정\n"
          "13. 리네이밍(파일처리)\n")
    select = input()
    if select == "1":
        clear()
        for index, item in enumerate(j):
            # show = item['data']['title'].replace('\n','   |   ')
            show = showRename(item['data']['title'])
            print(index, '\t:\t', show)
            if index % int(config['list_count']) == 0 and index > 0:
                print("다음 페이지로 진행하려면 1키를 누르시고 메인 페이지로 돌아가려면 2키를 누르세요. 아무 키나 누르면 그냥 진행됩니다.")
                try:
                    tmp = int(input())
                except:
                    clear()
                    continue
                if tmp == 2:
                    clear()
                    return main_cycle(j=j)

                clear()
        input('진행하려면 아무 키나 누르세요.')
    elif select == "2":
        clear()
        print("자동 저장 경로를 설정합니다. 기본값은 현재위치입니다.")
        config['save_path'] = input()
        config_save(config, config_path)
        print("자동 저장 경로가 설정되었습니다.")
        input('진행하려면 아무 키나 누르세요.')

    elif select == "3":
        clear()
        print("자동 다운로드 조건들을 설정합니다.\n"
              "1. 특정 키워드 포함시 다운로드\n"
              "2. 특정 해상도 다운로드 설정 (화이트리스트 / 블랙리스트)")
        select = input()
        if select == "1":
            while True:
                keyword_obj = open(keyword_path, 'a+', encoding='utf-8')
                clear()
                print(keyword_obj.read())
                print(
                    '\n\n추가로 넣을 키워드를 설정하세요. 해당 키워드가 들어있는 항목이 리스트에 있다면 다운받습니다. 수동 혹은 대량으로 추가하고 싶으면 keywords.txt 를 편집하세요. 구분자는 엔터입니다.')
                keyword = input('나가려면 x 키를 입력하세요 : ')
                if keyword == 'x': return main_cycle(j=j)
                if len(keyword.strip()) > 0:  # 빈칸은 안 됨
                    keyword_obj.write(keyword + '\n')
                    keyword_obj.close()
                    print(f'키워드 [{keyword}] (이)가 추가되었습니다.')
                    input('진행하려면 아무 키나 누르세요.')
                else:
                    return main_cycle(j=j)
        elif select == "2":
            clear()
            print('해상도에 관한 설정은 다음 두 가지가 있습니다. 화이트리스트와 블랙리스트로, 블랙리스트에 넣으면 아예 그 해상도는 다운받지 않고,\n'
                  '화이트리스트에 넣으면 해당 해상도는 왼쪽 우선순위로 다운받습니다. 아래는 기본값입니다.\n\n')
            print('화이트리스트\t', config['resolution_whitelist'])
            print('블랙리스트\t', config['resolution_blacklist'])
            print('\n\n')
            print('무엇을 수정하겠습니까?\n\n\n'
                  '1. 화이트리스트\n'
                  '2. 블랙리스트')
            keyword = input()
            if keyword == "1":
                print("어떻게 수정하겠습니까? 구분자는 쉼표( , ) 입니다.")
                config['resolution_whitelist'] = input()
                print("수정하였습니다.")
                config_save(config, config_path)
                input('진행하려면 아무 키나 누르세요.')
            if keyword == "1":
                print("어떻게 수정하겠습니까? 구분자는 쉼표( , ) 입니다.")
                config['resolution_blacklist'] = input()
                print("수정하였습니다.")
                config_save(config, config_path)
                input('진행하려면 아무 키나 누르세요.')

    elif select == "5":
        clear()
        print(f'현재 값은 {config["count"]} 입니다. 너무 큰 숫자는 불러올 때 렉이 걸릴 수 있지만 오래 전 애니메이션을 찾기에는 좋습니다. 숫자로 입력하시기 바랍니다.')
        config['count'] = int(input())
        config_save(config, config_path)
        print('저장 완료')
        input('진행하려면 아무 키나 누르세요.')
        return main_cycle()

    elif select == "6":
        clear()
        print(f"현재 값은 {config['list_count']} 개가 리스트 하나에 보여집니다. 몇 개로 수정하겠습니까?")
        config['list_count'] = int(input("숫자만 입력 : "))
        config_save(config, config_path)
        return main_cycle()

    elif select == "7":
        clear()
        print(f"찾고자 하는 문자열을 입력하세요. 만약 결과가 만족스럽지 않다면, 불러올 최신 에피소드 숫자 재지정(4) 옵션을 좀 더 큰 값으로 설정하세요.")
        tar = input("키워드 입력(대소문자 구분) : ")
        for index, item in enumerate(j):
            show = item['data']['title'].replace('\n', '   |   ')
            # print(index,'\t:\t',show)
            if show.lower().count(tar.lower()) > 0:
                print(index, '\t:\t', show)
        input('진행하려면 아무 키나 누르세요.')

    elif select == "8":
        clear()
        print('여기서 최신 애니메이션 기준은 리스트 기준입니다.\n리스트의 번호가 낮은 순서대로 우선순위를 갖습니다.')
        c = input('몇 개를 다운받겠습니까?(숫자 입력) : ')
        start_number_download(config, config_path, c)

    elif select == "9":
        clear()
        print('자동 다운로드가 시작됩니다. 이 창을 끄지 마십시오.')
        strar_auto_download(config, config_path)

    elif select == "10":
        clear()
        print('이 설정은, 원피스나 코난 등의 Absolute Number를 따르는 애니메이션을 처리하기 위한 용도입니다.\n'
              '즉, 코난 975화를 S28E06 등으로 변환해줍니다.\n'
              '"키워드"위주로 체크합니다. 예를들면, [Erai-raws] Detective Conan - 975 [1080p].mkv 를 변환하고 싶으면 detective conan을 입력하면 됩니다.'
              '코난과 원피스는 기본적으로 추가되어있으니 자유롭게 추가하세요.\n\n'
              '어떤 설정을 하겠습니까?\n\n'
              '1. 키워드 추가\n'
              '2. 현재 키워드 보기')
        select = input('입력 : ')
        if select == "1":
            while True:
                clear()
                keyword = input('추가할 키워드 입력 , 나가려면 x 입력 : ')
                if keyword == 'x': break
                open(sort_keyword_path, 'a+', encoding='utf-8').write(keyword + '\n')
        elif select == "2":
            print([item.strip() for item in open(sort_keyword_path, 'r', encoding='utf-8').readlines()])
            input('진행하려면 아무 키나 누르세요.')
    elif select == "11":
        clear()
        print('이 설정들은 네트워크 설정으로, 잘 모르면 건들지 마시기 바랍니다.\n\n'
              '1. 멀티쓰레딩 설정(다운로드 가속)\n'
              '2. 멀티 네트워크 인터페이스 설정(토렌트랑 유사)\n')
        select = input('입력 : ')
        if select == "1":
            clear()
            print(f"현재 멀티쓰레딩 값 : {config['multi_threading']}")
            keyword = input('멀티쓰레딩 값 (x = 나가기) : ')
            if keyword == 'x': return main_cycle()
            try: int(keyword)
            except:
                input("숫자만 입력하십시오. 아무키나 누르면 넘어갑니다.")
                return main_cycle()
            config['multi_threading'] = int(keyword)
            config_save(config , config_path)

        elif select == "2":
            clear()
            print("이 설정은 토렌트와 유사합니다. 여러 개의 네트워크 인터페이스를 지정해주면 자동으로 분배해줍니다.\n"
                  "여러 개의 네트워크 인터페이스를 지정할 때, 구분자는 | 로 합니다.\n"
                  "현재값이 None이면 자동으로 설정되니까 건들지 마세요.")
            print(f"현재 멀티 네트워크 인터페이스 값 : {config['network_interface']}")
            keyword = input('멀티쓰레딩 값 (x = 나가기 , auto = a 키 입력) : ')
            if keyword == 'x': return main_cycle()
            if keyword == 'a' :
                try:
                    ips = get_bind_ips()
                except:
                    try:
                        import psutil
                    except:
                        os.system('pip install psutil')
                        os.system('pip3 install psutil')
                        import psutil
                        try:
                            ips = get_bind_ips()
                        except:
                            import traceback
                            traceback.print_exc()
                            print("psutil을 설치할 수 없습니다. 처음으로 돌아갑니다.\n")
                            input('아무 키나 누르십시오')
                            return main_cycle(j=j)
                reuslt = []
                from requests.exceptions import ConnectionError
                for ip in ips:
                    session = session_for_src_addr(ip)
                    try:req = session.get('http://httpbin.org/ip' , timeout=10)
                    except ConnectionError:
                        continue
                    if req.status_code == 200:
                        reuslt.append(ip)
                keyword = "|".join(reuslt)
            config['network_interface'] = keyword
            config_save(config, config_path)
    elif select == "12" :
        clear()
        db = SqliteDict('K-ani 다운로드 완료.db')
        db_keys = [item for item in db if db[item] == True]
        db_added_magnet = [item for item in j if item['data']['magnets'][0]['magnet'] in db_keys]
        for index, item in enumerate(db_added_magnet):
            # show = item['data']['title'].replace('\n','   |   ')
            show = showRename(item['data']['title'])
            print(index, '\t:\t', show)
            if index % int(config['list_count']) == 0 and index > 0:
                select = input('특정 번호 지우기(재다운로드 가능) -> 번호 입력 / 특정 키워드 모두 지우기 -> 키워드 입력 / 다음 페이지 -> z 입력 / 나가기 -> x 입력')
                if select == "x":
                    clear()
                    return main_cycle()
                if select == "z":
                    clear()
                    continue
                try:
                    tmp = int(select) # 특정 번호 지우기
                    remove_title = db_added_magnet[tmp]['data']['title']
                    for item in j:
                        if item['data']['title'] == remove_title:
                            print("DELETE\t\t" , item['data']['title'])
                            try:
                                for mg in item['data']['magnets']:
                                    try:
                                        del db[mg['magnet']]
                                        break
                                    except :
                                        print("ERROR")
                                        continue
                                db.commit()
                            except:
                                pass
                    clear()
                    return main_cycle()
                    
                except:
                    for item in j:
                        if item['data']['title'].count(select) > 0:
                            print("DELETE\t\t" , item['data']['title'])
                            try:
                                for mg in item['data']['magnets']:
                                    try:
                                        del db[mg['magnet']]
                                        break
                                    except :
                                        print("ERROR")
                                        continue
                                db.commit()
                            except:
                                pass
                    clear()
                    return main_cycle()


                clear()
        input('특정 번호 지우기(재다운로드 가능) -> 번호 입력 / 특정 키워드 지우기 -> 키워드 입력 / 다음 페이지 -> z 입력 / 나가기 -> x 입력')
    elif select == "13":
        clear()
        print("원하는 기능을 고르세요.\n"
              "1. 구글 시트 리네이밍 (시트에 키워드가 있는 파일만 리네이밍 및 파일 이동)\n"
              "2. 자동 리네이밍 (시트 제외)\n"
              "3. Absolute Numbering 리네이밍 (원피스, 코난같은 작품 파일 처리)\n")
        select = input("번호 입력 : ")
        if select == "1":
            clear()
            print("구글 시트 리네이밍 | 해당 모드는 recursive(내부 폴더 속에 있는 파일까지 리네이밍)하게 작동합니다. 폴더 위치를 입력해주세요.\n"
                  "위치를 입력하지 않으면 현재폴더를 기준으로 잡습니다.")
            select = input("폴더 위치 : ")
            if select == "": select = os.getcwd()
            with requests_cache.disabled():
                res = requests.get(f'http://{server_url}/ani_mapping_keyword_all')
                j = res.json()['result']
                sheet_renaming(select , j)

        elif select == "2":
            clear()
            print("자동 리네이밍 (시트 제외) | 해당 모드는 recursive(내부 폴더 속에 있는 파일까지 리네이밍)하게 작동합니다. 폴더 위치를 입력해주세요.\n"
                  "위치를 입력하지 않으면 현재폴더를 기준으로 잡습니다. 파일의 이름을 바꾸지는 않습니다.\n")
            select = input("폴더 위치 : ")
            if select == "": select = os.getcwd()
            rename_log = SqliteDict("rename_Log.db")
            for (path, dir, files) in os.walk(select):
                for filename in files:
                    full = os.path.join(path , filename)
                    info = renameing_tools(filename)
                    if info == None : continue
                    folder_name = f"{info['tvdb_title']} ({info['year']})"
                    season = info['season']
                    new_path = os.path.join(config['save_path'], folder_name, f"S0{season}", Useless_Rename(filename))
                    mkdirs(os.path.split(new_path)[0])
                    print(f"RENAME\t\t{full}  -->>  {new_path}")
                    try:
                        os.renames(full, new_path)
                        rename_log[new_path] = full
                        rename_log.commit()
                    except FileExistsError:
                        os.remove(new_path)
                        os.renames(full, new_path)
                        rename_log[new_path] = full
                        rename_log.commit()
                    except FileNotFoundError:
                        pass

        elif select == "3":
            clear()
            print("Absolute Numbering 리네이밍 | 해당 모드는 recursive(내부 폴더 속에 있는 파일까지 리네이밍)하게 작동합니다. 폴더 위치를 입력해주세요.\n"
                  "위치를 입력하지 않으면 현재폴더를 기준으로 잡습니다. 파일의 이름을 바꾸지는 않습니다.\n")
            select = input("폴더 위치 : ")
            rename_log = SqliteDict("rename_Log.db")
            if select == "": select = os.getcwd()
            for (path, dir, files) in os.walk(select):
                for filename in files:
                    rename_absolute_to_aired(os.path.join(path , filename))
                    
    return main_cycle(j=j)

def mkdirs(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        return
    except:
        mkdirs(os.path.split(path)[0])
        os.mkdir(path)

def sheet_renaming(directory , j , is_file=False):
    rename_log = SqliteDict("rename_Log.db")
    if is_file :
        full = directory
        filename = os.path.split(directory)[1]
        ff = [item for item in j if item in filename]
        if ff:
            ff = [ff[-1]]
            url = j[ff[0]][2]
            res = requests.get(url)
            s = BeautifulSoup(res.text, 'html.parser')
            tmps = s.select('div.change_translation_text')
            title = None
            if not title:
                for tmp in tmps:
                    if tmp['data-language'] == 'kor':
                        title = tmp['data-title']
                        break
            if not title:
                for tmp in tmps:
                    if tmp['data-language'] == 'eng':
                        title = tmp['data-title']
                        break

            year = None
            tmps = s.select('ul.list-group > li')
            for tmp in tmps:
                try:
                    if tmp['data-number'] == "1":
                        tmp_text = tmp.select_one('p.list-group-item-text').text
                        year = re.findall('\d{4}', tmp_text)[0]
                except:
                    continue
            folder_name = f"{replace_name_for_window(title)} ({year})"
            season = f"S0{j[ff[0]][3]}"
            if j[ff[0]][4] == "":
                new_path = os.path.join(config['save_path'], folder_name, season, filename)
            elif j[ff[0]][4] != "":  # 강제지정
                ext = os.path.splitext(filename)[1]
                resolution = "Unknown"
                if [item for item in ['1080', 'fhd', '1920'] if item in filename]:
                    resolution = "1080p"
                if [item for item in ['720', '1280'] if item in filename]:
                    resolution = "720p"
                new_filename = f"{folder_name} S0{season}E{j[ff[0]][4]} [{resolution}]{ext}"
                new_path = os.path.join(config['save_path'], folder_name, season, new_filename)
            if not os.path.exists(os.path.join(config['save_path'], folder_name)): os.mkdir(
                os.path.join(config['save_path'], folder_name))
            if not os.path.exists(os.path.join(config['save_path'], folder_name, season)): os.mkdir(
                os.path.join(config['save_path'], folder_name, season))
            print(f"RENAME\t\t{full}  -->>  {new_path}")
            try:
                os.renames(full, new_path)
                rename_log[new_path] = full
                rename_log.commit()
            except FileExistsError:
                os.remove(new_path)
                os.renames(full, new_path)
                rename_log[new_path] = full
                rename_log.commit()
            except FileNotFoundError:
                pass
            if j[ff[0]][5] == "ABS": # Absolute Numbering 후처리
                rename_absolute_to_aired(full)
            return
        
    for (path, dir, files) in os.walk(directory):
        for filename in files:
            ff = [item for item in j if item in filename]
            if ff:
                ff = [ff[-1]]
                full = os.path.join(path, filename)
                url = j[ff[0]][2]
                res = requests.get(url)
                s = BeautifulSoup(res.text, 'html.parser')
                tmps = s.select('div.change_translation_text')
                title = None
                if not title:
                    for tmp in tmps:
                        if tmp['data-language'] == 'kor':
                            title = tmp['data-title']
                            break
                if not title:
                    for tmp in tmps:
                        if tmp['data-language'] == 'eng':
                            title = tmp['data-title']
                            break

                year = None
                tmps = s.select('ul.list-group > li')
                for tmp in tmps:
                    try:
                        if tmp['data-number'] == "1":
                            tmp_text = tmp.select_one('p.list-group-item-text').text
                            year = re.findall('\d{4}', tmp_text)[0]
                    except:
                        continue
                folder_name = f"{replace_name_for_window(title)} ({year})"
                season = f"S0{j[ff[0]][3]}"
                if j[ff[0]][4] == "":
                    new_path = os.path.join(config['save_path'], folder_name, season, filename)
                elif j[ff[0]][4] != "":  # 강제지정
                    ext = os.path.splitext(filename)[1]
                    resolution = "Unknown"
                    if [item for item in ['1080', 'fhd', '1920'] if item in filename]:
                        resolution = "1080p"
                    if [item for item in ['720', '1280'] if item in filename]:
                        resolution = "720p"
                    new_filename = f"{folder_name} S0{season}E{j[ff[0]][4]} [{resolution}]{ext}"
                    new_path = os.path.join(config['save_path'], folder_name, season, new_filename)
                if not os.path.exists(os.path.join(config['save_path'], folder_name)): os.mkdir(
                    os.path.join(config['save_path'], folder_name))
                if not os.path.exists(os.path.join(config['save_path'], folder_name, season)): os.mkdir(
                    os.path.join(config['save_path'], folder_name, season))
                print(f"RENAME\t\t{full}  -->>  {new_path}")
                try:
                    os.renames(full, new_path)
                    rename_log[new_path] = full
                    rename_log.commit()
                except FileExistsError:
                    os.remove(new_path)
                    os.renames(full, new_path)
                    rename_log[new_path] = full
                    rename_log.commit()
                except FileNotFoundError:
                    pass
                if j[ff[0]][5] == "ABS": # Absolute Numbering 후처리
                    rename_absolute_to_aired(full)

def rename_absolute_to_aired(path):
    rename_log = SqliteDict("rename_Log.db")
    full , filename= path , os.path.split(path)[1]
    info = renameing_tools(filename)
    if info == None: return

    tvdb_info = info['tvdb_search_info']
    official_url = tvdb_info['url']  # seasons/absolute/1
    url = f'https://www.thetvdb.com{official_url}/seasons/absolute/1'
    tvdb_res = requests.get(url, headers=headers)
    s = BeautifulSoup(tvdb_res.text, 'html.parser')
    tbls = s.select('table.table > tbody > tr')
    folder_name = replace_name_for_window(f"{info['tvdb_title']} ({info['year']})")
    new_filename = False
    for tbl in tbls:
        tbl_tds = tbl.select('td')
        S_E_info = tbl_tds[0].text
        tmp = re.compile('s\d+', re.I)
        tvdb_season = re.findall(tmp, S_E_info)[0]
        tvdb_season = re.findall('\d+', tvdb_season)[0]

        tmp = re.compile('e\d+', re.I)
        tvdb_episode = re.findall(tmp, S_E_info)[0]
        tvdb_episode = re.findall('\d+', tvdb_episode)[0]
        if int(info['episode'][0]) == int(tvdb_episode) and int(info['season'][0]) == int(
                tvdb_season):  # 보수적으로 잡는다.
            link = 'https://thetvdb.com' + tbl_tds[1].select_one('a')['href']
            res = requests.get(link, headers=headers)
            s = BeautifulSoup(res.text, 'html.parser')
            tmp = s.select('div.crumbs')[0].text
            com = re.compile('Season \d+')
            season = re.findall(com, tmp)[0]
            season = re.findall('\d+', season)[0]

            com = re.compile('Episode \d+')
            episode = re.findall(com, tmp)[0]
            episode = re.findall('\d+', episode)[0]

            ext = os.path.splitext(filename)[1]
            resolution = "Unknown"
            if [item for item in ['1080', 'fhd', '1920'] if item in filename]:
                resolution = "1080p"
            if [item for item in ['720', '1280'] if item in filename]:
                resolution = "720p"
            new_filename = f"{folder_name} S{season}E{episode} [{resolution}]{ext}"
            new_path = os.path.join(config['save_path'], folder_name, f'S0{season}', new_filename)
            mkdirs(os.path.split(new_path)[0])
            print(f"RENAME\t\t{full}  -->>  {new_path}")
            try:
                os.renames(full, new_path)
                rename_log[new_path] = full
                rename_log.commit()
            except FileExistsError:
                os.remove(new_path)
                os.renames(full, new_path)
                rename_log[new_path] = full
                rename_log.commit()
            except FileNotFoundError:
                pass
            break

def get_bind_ips(except_ip_list=[] , except_ip_word_list=[] , except_keyword_list=[]):
    ips = psutil.net_if_addrs()
    result = []
    for name in ips:
        skip = False
        for blackkeyword in except_keyword_list:
            if blackkeyword in name:
                skip = True
                break
        if skip == True:continue

        for black_ip_keyword in except_ip_word_list:
            if black_ip_keyword in ips[name][1].address:
                skip = True
                break
        if skip == True:continue

        for black_ip in except_ip_list:
            if black_ip == ips[name][1].address:
                skip = True
                break
        if skip == True:continue

        result.append(ips[name][1].address)
    return result



def word_hash(word):
    h = hashlib.sha256()
    h.update(word.encode('utf-8'))
    result = h.hexdigest()
    return result


def delete_tmp_files(final_save_path):
    if not os.path.exists(final_save_path): return
    for file in os.listdir(final_save_path):
        f = os.path.join(final_save_path, file)
        if file == 'tmp': os.remove(f)
        if file.count('.ros') == 0: continue
        if file.count('tmp') == 0: continue
        try:
            os.remove(f)
        except:
            pass

def session_for_src_addr(addr: str) -> requests.Session:
    """
    Create `Session` which will bind to the specified local address
    rather than auto-selecting it.
    """
    session = requests.Session()
    for prefix in ('http://', 'https://'):
        session.get_adapter(prefix).init_poolmanager(
            # those are default values from HTTPAdapter's constructor
            connections=requests.adapters.DEFAULT_POOLSIZE,
            maxsize=requests.adapters.DEFAULT_POOLSIZE,
            # This should be a tuple of (address, port). Port 0 means auto-selection.
            source_address=(addr, 0),
        )

    return session

import multiprocessing
def get_download(config, config_path, magnet, myanime_title, sub_url, episode_file_name):
    if episode_file_name:
        for black in config['resolution_blacklist'].split(','):
            if black in episode_file_name:
                return
    _j = requests.get(f'http://{server_url}/ani_magnet', data={'magnet': magnet, 'apikey': config['apikey']})
    if _j.status_code != 200:
        return
    _j = _j.json()['result']
    if _j in [{} , []]: return
    final_save_path = os.path.join(config['save_path'], 'tmp_folder')
    if not os.path.exists(final_save_path): os.mkdir(final_save_path)
    delete_tmp_files(final_save_path)
    tmps = []
    tmp = re.compile(
        '-[\d]+\.ros')  # '[HorribleSubs] Yahari Ore no Seishun Love Come wa Machigatteiru Kan - 10 [1080p].mkv-CRC.ros'
    tmp2 = re.compile('-CRC\.ros')
    pbar = tqdm(_j, bar_format="{desc:<5}{percentage:3.0f}%|{bar}{r_bar}")
    with ThreadPoolExecutor(max_workers=config['multi_threading']) as ex:
        # for item in pbar:
        def download_file(item, pbar , number):
            filename = item['filename']
            tmps.append(filename)
            url = item['attachments'][0]['url']
            # 이름을 바꿔준다
            if len(re.findall(tmp, filename)):
                filename = 'tmp' + re.findall(tmp, filename)[0]
            elif len(re.findall(tmp2, filename)):
                filename = 'tmp' + re.findall(tmp2, filename)[0]
            if not os.path.exists(final_save_path): os.mkdir(final_save_path)
            st_time = time.time()
            size = item['attachments'][0]['size']
            if not config['network_interface'] :
                open(os.path.join(final_save_path, filename), 'wb').write(requests.get(url, headers=headers).content)
            else :
                session = net_interfaces_session[number % len(net_interfaces_session)]
                open(os.path.join(final_save_path, filename), 'wb').write(session.get(url, headers=headers).content)
            mbps = (float(size) / 1000 / 1000) / (time.time() - st_time)
            #text = f'chunk name : {filename} | {round(time.time() - st_time, 2)} SEC | \tavg {round(mbps * config["multi_threading"], 2)} MB/s | {round(size / 1024 / 1024, 2)}MB'
            # pbar.set_description(text)
            #pbar.set_postfix_str(text)
            pbar.update(1)
            pbar.refresh()

        if config['network_interface']:
            net_list = [item.strip() for item in config['network_interface'].split('|') if item.count('.') == 3]
            net_interfaces_session = [session_for_src_addr(item) for item in net_list]
        futures = [ex.submit(download_file, item[1], pbar , item[0]) for item in enumerate(_j)]
        for future in as_completed(futures):
            result = future.result()

    filename = 'tmp-CRC.ros'
    tmp_filepath = os.path.join(final_save_path, filename)
    tmp_filepath = re.sub(tmp, '', tmp_filepath)
    output_name = tmp_filepath.replace('-CRC.ros', '')
    output_name = re.sub(tmp, '', output_name).strip()
    os.system(f'file_split_merge -m -i "{output_name}"')
    # command = (['file_split_merge', '-m', '-i', '"%s"' % output_name])
    # result = subprocess.Popen(command , stdin=subprocess.PIPE , stdout=subprocess.PIPE)
    # j = subprocess.run(command, capture_output=True)

    t = tmps[0]
    t = t.replace('-CRC.ros', '')
    t = re.sub(tmp, '', t).strip()
    t = Useless_Rename(t)
    try:
        os.rename(output_name, os.path.join(final_save_path, t))
    except FileExistsError:
        os.remove(os.path.join(final_save_path, t))
        os.rename(output_name, os.path.join(final_save_path, t))
    delete_tmp_files(final_save_path)

    # post process
    name_info = renameing_tools(t)
    folder_name = name_info['tvdb_title'] + '%s' % (' (%s)' % name_info['year'] if name_info['year'] != None else "")
    folder_name = folder_name.strip()

    season = str(int(name_info['season']))  # or..
    episode = None
    convert_season_and_titles_showNames = [item.strip() for item in open(sort_keyword_path, 'r').readlines() if
                                           len(item) > 0]
    if [item for item in convert_season_and_titles_showNames if item.lower() in t.lower()]:  # 키워드가 하나라도 겹친다면,
        tvdb_info = name_info['tvdb_search_info']
        official_url = tvdb_info['url']  # seasons/absolute/1
        url = f'https://www.thetvdb.com{official_url}/seasons/absolute/1'
        tvdb_res = requests.get(url, headers=headers)
        s = BeautifulSoup(tvdb_res.text, 'html.parser')
        tbls = s.select('table.table > tbody > tr')
        for tbl in tbls:
            tbl_tds = tbl.select('td')
            S_E_info = tbl_tds[0].text
            tmp = re.compile('s\d+', re.I)
            tvdb_season = re.findall(tmp, S_E_info)[0]
            tvdb_season = re.findall('\d+', tvdb_season)[0]

            tmp = re.compile('e\d+', re.I)
            tvdb_episode = re.findall(tmp, S_E_info)[0]
            tvdb_episode = re.findall('\d+', tvdb_episode)[0]
            if int(name_info['episode'][0]) == int(tvdb_episode) and int(name_info['season'][0]) == int(
                    tvdb_season):  # 보수적으로 잡는다.
                link = 'https://thetvdb.com' + tbl_tds[1].select_one('a')['href']
                res = requests.get(link, headers=headers)
                s = BeautifulSoup(res.text, 'html.parser')
                tmp = s.select('div.crumbs')[0].text
                com = re.compile('Season \d+')
                season = re.findall(com, tmp)[0]
                season = re.findall('\d+', season)[0]

                com = re.compile('Episode \d+')
                episode = re.findall(com, tmp)[0]
                episode = re.findall('\d+', episode)[0]
                break

    base_dir_path = os.path.join(config['save_path'], replace_name_for_window(folder_name))
    if int(season) < 10:
        season = "S0" + season
    else:
        season = "S" + season
    if not os.path.exists(base_dir_path): os.mkdir(base_dir_path)
    season_path = os.path.join(base_dir_path, season)
    if not os.path.exists(season_path): os.mkdir(season_path)
    try:
        os.renames(
            os.path.join(final_save_path, t),
            os.path.join(season_path, t)
        )
    except FileExistsError:
        os.remove(os.path.join(season_path, t))
        os.renames(
            os.path.join(final_save_path, t),
            os.path.join(season_path, t)
        )
    # also subtitle will be processed
    ext = sub_url.split('.')[-1]
    if episode:  # 에피소드 넘버가 정해진다면...
        before = os.path.join(season_path, t)
        after = os.path.join(season_path, modify_by_season_and_episode(t, season, episode, name_info))
        t = os.path.split(after)[1]
        os.renames(before, after)
        sub_path = os.path.splitext(after)[0] + '.' + ext
    else:
        sub_path = os.path.join(season_path, os.path.splitext(t)[0] + '.' + ext)
    # subtitle
    open(sub_path, 'wb').write(requests.get(sub_url).content)
    print(
        f'{os.path.join(season_path, t)} 다운로드 완료. 용량 {round(os.path.getsize(os.path.join(season_path, t)) / 1024 / 1024 / 1024, 2)} GB')

    with requests_cache.disabled():
        res = requests.get(f'http://{server_url}/ani_mapping_keyword_all')
        j = res.json()['result']
        sheet_renaming(os.path.join(season_path, t), j, is_file=True)
        sheet_renaming(sub_path, j, is_file=True)

    return True


def modify_by_season_and_episode(filename, season, episode, name_info):
    # {'tvdb_title': showName_tvdb, 'season': info['season'], 'episode': info['episode'], 'year': year,
    #                         'tvdb_search_info': tv, 'filename_info': info}
    # season, episode, name_info
    orig_episode_number = name_info['episode'][0]

    def twice(num):
        if num <= 9:
            num = '0' + str(num)
            return num
        return num

    season = twice(int(season.replace('S', '')))
    episode = twice(int(episode))
    filename = filename.replace(orig_episode_number, 'S%sE%s' % (season, episode), 1)
    return filename


def strar_auto_download(config, config_path):
    able_files = \
    requests.get(f'http://{server_url}/magnet_hash_able_list', data={'apikey': config['apikey']}).json()['result']
    keywords = open(keyword_path, 'r', encoding='utf-8').readlines()
    keywords = [item.strip() for item in keywords if len(item) > 0]  # 오류 검증
    download_db = SqliteDict('K-ani 다운로드 완료.db')
    for index, item in enumerate(j):
        # if item['data']['sub_url'] in download_db: continue # 이미 다운
        title = item['data']['title']
        check = [item for item in keywords if item.lower() in title.lower()]
        sub_url = item['data']['sub_url']
        if check:
            myanime_title = replace_name_for_window(item['data']['myanime']['name'])
            for tmp in item['data']['magnets']:  # 여러 개 있을 수 있다.
                magnet = tmp['magnet']
                # magnet = "magnet:?xt=urn:btih:0d4060cf38a86d889cca3d99e12a3180b90ae13e"
                if magnet in download_db: continue
                tes = word_hash(magnet)
                if word_hash(magnet) not in able_files: continue
                if get_download(config, config_path, magnet, myanime_title, sub_url, tmp['title']):
                    download_db[magnet] = True
                    download_db.commit()
                else:
                    tmp_title = title.replace("\n", " | ")
                    # print(f'[{tmp_title}] 에 속하는 토렌트 주소 {magnet} 가 아직 작업이 덜 되어서 다운로드가 불가능합니다. 다음에 다운받습니다.')

    return


def start_number_download(config, config_path, count):
    able_files = \
    requests.get(f'http://{server_url}/magnet_hash_able_list', data={'apikey': config['apikey']}).json()['result']
    download_db = SqliteDict('K-ani 다운로드 완료.db')
    for index, item in enumerate(j):
        if index >= int(count): return
        # if item['data']['sub_url'] in download_db: continue # 이미 다운
        title = item['data']['title']
        sub_url = item['data']['sub_url']
        myanime_title = replace_name_for_window(item['data']['myanime']['name'])
        for tmp in item['data']['magnets']:  # 여러 개 있을 수 있다.
            magnet = tmp['magnet']
            # magnet = "magnet:?xt=urn:btih:0d4060cf38a86d889cca3d99e12a3180b90ae13e"
            if magnet in download_db: continue
            if word_hash(magnet) not in able_files: continue
            if get_download(config, config_path, magnet, myanime_title, sub_url, tmp['title']):
                download_db[magnet] = True
                download_db.commit()
            else:
                tmp_title = title.replace("\n", " | ")
                # print(f'[{tmp_title}] 에 속하는 토렌트 주소 {word_hash(magnet)} 가 아직 작업이 덜 되어서 다운로드가 불가능합니다. 다음에 다운받습니다.')

    return


def remove_bracket(text, style="["):
    if style.count('[') > 0:
        tmp = re.compile('\[[\w\d\s\-]+\]')
        text = re.sub(tmp, '', text).strip()
    if style.count('(') > 0:
        tmp = re.compile('\([\w\d\s\-]+\)')
        text = re.sub(tmp, '', text).strip()
    return text


def isSeason(t):
    tmp = re.compile('[^B]S\d+', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return re.findall('\d+', tmp_res[0])[0]

    tmp = re.compile('\d+nd season', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return re.findall('\d+', tmp_res[0])[0]

    tmp = re.compile('\d+rd season', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return re.findall('\d+', tmp_res[0])[0]

    tmp = re.compile('\d+th season', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return re.findall('\d+', tmp_res[0])[0]

    tmp = re.compile('season \d+', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return re.findall('\d+', tmp_res[0])[0]

    return '1'


def rename_for_searching(t):
    tmp = re.compile('[^B]S\d+', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return isSeason(t), re.sub(tmp, '', t).strip()

    tmp = re.compile('\d+nd season', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return isSeason(t), re.sub(tmp, '', t).strip()

    tmp = re.compile('\d+rd season', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return isSeason(t), re.sub(tmp, '', t).strip()

    tmp = re.compile('\d+th season', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return isSeason(t), re.sub(tmp, '', t).strip()

    tmp = re.compile('season \d+', re.I)
    tmp_res = re.findall(tmp, t)
    if tmp_res:
        return isSeason(t), re.sub(tmp, '', t).strip()
    return None, t


def renameing_tools(filename, super_season=None):  # only filename accept
    """if os.path.isfile(path): # path
        (basedir , filename) = os.path.split(path)
    else: # normal file name
        filename = path"""
    # '[Ohys-Raws] Yahari Ore no Seishun LoveCome wa Machigatte Iru. Kan - 11 (TBS 1920x1080 x264 AAC).mp4'
    season = None
    if isSeason(filename) and not super_season:
        super_season, filename = rename_for_searching(filename)

    def isYearInclude(showName):
        tmp = re.compile('\(\d{4}\)')
        if re.findall(tmp, showName):
            return re.findall(tmp, showName)[0].replace('(', '').replace(')', '').strip()

    def info_from_filename(filename):
        filename_no_ext = os.path.splitext(filename)[0]
        s = filename_no_ext.split(' - ')
        if len(s) < 2:
            return  # error
        elif len(s) == 2:  # no season
            showName = remove_bracket(s[0])
            episodeNumber = re.findall('\d+', remove_bracket(s[1], style="[("))
            season = year = None
            if super_season:
                season = super_season
            elif isSeason(showName):
                season = isSeason(showName)
            if isYearInclude(showName):
                year = isYearInclude(showName)
                showName = remove_bracket(showName, style="[(")
            return {'title': showName, 'episode': episodeNumber, 'season': season, 'year': year}
        elif len(s) > 2:  # no season
            showName = remove_bracket('-'.join(s[:-1]))
            episodeNumber = re.findall('\d+', remove_bracket(s[-1], style="[("))
            season = year = None
            if super_season:
                season = super_season
            elif isSeason(showName):
                season = isSeason(showName)
            if isYearInclude(showName):
                year = isYearInclude(showName)
                showName = remove_bracket(showName, style="[(")
            return {'title': showName, 'episode': episodeNumber, 'season': season, 'year': year}

    info = info_from_filename(filename)
    if info == None: return
    tvdb_info = \
    requests.get(f'http://{server_url}/tvdb_search', data={'title': info['title'], 'year': info['year']}).json()[
        'result']
    # myanimeinfo
    myanime_search = requests.get(f'http://{server_url}/find_myanime_season', data={'keyword': info['title']})
    if myanime_search.status_code == 200 and myanime_search.json()['result']['season']:
        info['season'] = myanime_search.json()['result']['season']

    def tvdb_filtering_cascade(tvdb_info, up_value=0.9):
        for tv in tvdb_info:
            if tv['compare'] >= up_value:
                if 'translations' in tv and 'kor' in tv['translations']:
                    showName_tvdb = tv['translations']['kor']
                elif 'translations' in tv and 'eng' in tv['translations']:
                    showName_tvdb = tv['translations']['eng']
                else:
                    showName_tvdb = tv['name']
                year = None
                if 'released' in tv:
                    year = tv['released']
                return {'tvdb_title': showName_tvdb, 'season': str(int(info['season'])), 'episode': info['episode'],
                        'year': year,
                        'tvdb_search_info': tv, 'filename_info': info}
        if up_value <= 0.6: return  # 없는거임
        return tvdb_filtering_cascade(tvdb_info, up_value=up_value - 0.05)

    result = tvdb_filtering_cascade(tvdb_info,
                                    0.9)  # '[Erai-raws] Tenchi Muyou! Ryououki Dai Go-ki - 03 [1080p][Multiple Subtitle].mkv'
    if not result:  # [Ohys-Raws] Yahari Ore no Seishun LoveCome wa Machigatte Iru. Kan - 11 (TBS 1920x1080 x264 AAC).mp4 처리해줘야
        # 시즌을. find_myanime_season
        res = requests.get(f'http://{server_url}/find_myanime_season', data={'keyword': info['title']})
        if res.status_code != 200 and res.text == "nothing found":  # 키워드를 바꿔봐야
            res = requests.get(f'http://{server_url}/find_myanime_rough_find', data={'keyword': info['title']})
            if res.status_code == 200:
                title = res.text
                return renameing_tools('%s  - %s.mp4' % (title, info['episode'][0]))
        elif res.status_code == 500:  # internal Error
            name_info = {'tvdb_title': "수동 정리 필요", "season": info['season'], 'year': None}
            return name_info
        else:
            j = res.json()['result']
            if j['season'] == None: j['season'] = '1'
            return renameing_tools('%s S0%s - %s.mp4' % (j['tvdb_title'], j['season'], info['episode'][0]),
                                   super_season=super_season)
    return result


"""for (path, dir, files) in os.walk("F:\# INCOMING\최신 애니"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        full = os.path.join(path, filename)
        tmp = renameing_tools(filename)
        if tmp == None :
            print('c')
            continue
        print(tmp)"""

# test = renameing_tools('[HorribleSubs] Boku no Hero Academia - Ikinokore! Kesshi no Survival Kunren - 01 [1080p].mkv')

def Useless_Rename(t):
    t = t.replace('BS11','')
    t = t.replace('1920x1080','')
    t = t.replace('1280x720','')
    t = t.replace('3840x2160','')
    t = t.replace('x264','')
    reg = re.compile('\s{2,9}')
    t = re.sub(reg , '', t)
    return t

if __name__ == '__main__':
    config_path = os.path.join(os.getcwd(), 'K-ani.config.pickle')
    keyword_path = os.path.join(os.getcwd(), 'keywords.txt')
    sort_keyword_path = os.path.join(os.getcwd(), 'sort_keyword.txt')
    if not os.path.exists(sort_keyword_path):
        open(sort_keyword_path, 'w').write('detective conan\none piece\n')
    if not os.path.exists(config_path):
        print("환경설정을 시작합니다.")
        print("APIKEY를 입력하세요.")
        config = {}
        config['apikey'] = input()
        print("불러올 최신 에피소드 숫자를 정해주세요. 기본값은 100개 입니다.")
        config['count'] = int(input())
        print("저장할 위치를 정하세요. TVDB에 얼추 맞게끔 폴더 구조를 자동으로 생성합니다.")
        config['save_path'] = input("애니메이션 정리 폴더 위치 입력 : ")
        config['resolution_whitelist'] = "1080,720"
        config['resolution_blacklist'] = "480,360"
        config['list_count'] = 20
        config['multi_threading'] = 3
        config['network_interface'] = None
        config_save(config, config_path)
    else:
        config = config_load(config_path)
    print(config)
    # time.sleep(3)

    res = requests.get(f'http://{server_url}/ani_list',
                       data={'apikey': config['apikey'], 'count': str(config['count'])})
    if res.status_code == 200:
        j = res.json()['result']
        main_cycle(j=j)
    else:
        print('APIKEY가 등록되지 않았습니다. 관리자에게 문의하십시오.')
        input()
