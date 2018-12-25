# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import re, os, os.path
import Media, VideoFiles, Stack, Utils
import time, json, traceback, io

episode_regexps = [
    r'(?P<show>.*?)[\s\.]E?(?P<ep>\d{1,2})[\-\~]E?\d{1,2}',  #합본 걸리게
    r'(?P<show>.*?)[eE](?P<ep>[0-9]{1,4})'
]

date_regexps = [
    r'(?P<show>.*?)[^0-9a-zA-Z](?P<year>[0-9]{2})(?P<month>[0-9]{2})(?P<day>[0-9]{2})[^0-9a-zA-Z]', # 6자리
]

try:
    import logging
    import logging.handlers
    logger = logging.getLogger('sjva_scanner')
    logger.setLevel(logging.ERROR)
    formatter = logging.Formatter(u'[%(asctime)s|%(lineno)s]:%(message)s')
    #file_max_bytes = 10 * 1024 * 1024 
    filename = os.path.join(os.path.dirname( os.path.abspath( __file__ ) ), '../../', 'Logs', 'sjva.scanner.korea.tv.download.log')
    fileHandler = logging.FileHandler(filename, encoding='utf8')
    #fileHandler = logging.handlers.RotatingFileHandler(filename=filename), maxBytes=file_max_bytes, backupCount=5, encoding='euc-kr')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
except:
    pass

def Scan(path, files, mediaList, subdirs, language=None, root=None):
    VideoFiles.Scan(path, files, mediaList, subdirs, root)
    paths = Utils.SplitPath(path)
    shouldStack = True
    logger.debug('=====================================================')
    logger.debug('- path:%s' % path)
    logger.debug('- files count:%s' % len(files))
    logger.debug('- subdir count:%s' % len(subdirs))
    for _ in subdirs:
        logger.debug('  * %s' % _)
    if len(paths) != 0:
	    logger.debug('- paths[0] : %s' % paths[0])
    logger.debug('- files count : %s', len(files))
    for i in files:
        tempDone = False
        try:
            file = os.path.basename(i)
            logger.debug(' * FILE : %s' % file)
            #for idx, rx in enumerate(episode_regexps):
            for rx in episode_regexps:
                match = re.search(rx, file, re.IGNORECASE)
                if match:
                    show = match.group('show').replace('.', '') if match.groupdict().has_key('show') else ''
                    season = 1
                    episode = int(match.group('ep'))
                    name, year = VideoFiles.CleanName(show)
                    name = re.sub(r'((.*?기획)|(미니시리즈)|(.*?드라마)|(.*?특집))', '', name).strip()
                    logger.debug('  - MATCH show:[%s] name:[%s] episode:[%s] year:[%s]', show, name, episode, year)
                    if len(name) > 0:
                        tv_show = Media.Episode(name, season, episode, '', year)
                        tv_show.display_offset = 0
                        tv_show.parts.append(i)
                        mediaList.append(tv_show)
                        logger.debug('  - APPEND by episode: %s' % tv_show)
                        tempDone = True
                        break
            if tempDone == False:
                for rx in date_regexps:
                    match = re.search(rx, file)
                    if match:
                        year = int(match.group('year')) + 2000
                        month = int(match.group('month'))
                        day = int(match.group('day'))
                        show = match.group('show')
                        tv_show = Media.Episode(show, year, None, None, None)
                        tv_show.released_at = '%d-%02d-%02d' % (year, month, day)
                        tv_show.parts.append(i)
                        mediaList.append(tv_show)
                        logger.debug('  - APPEND by date: %s' % tv_show)
                        tempDone = True
                        break
            if tempDone == False:
                logger.error(' NOT APPEND!!')
        except Exception, e:
            logger.error(e)
    if shouldStack:
        Stack.Scan(path, files, mediaList, subdirs)

