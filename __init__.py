# Copyright 2018 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import feedparser
# from os.path import dirname
#import re
from time import sleep

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.audio import wait_while_speaking
from mycroft.util.log import LOG
try:
    from mycroft.skills.audioservice import AudioService
except:
    from mycroft.util import play_mp3
    AudioService = None


class NoAgendaSkill(MycroftSkill):
    def __init__(self):
        super(NoAgendaSkill, self).__init__(name="NoAgendaSkill")
        self.process = None
        self.audioservice = None

    def initialize(self):
        if AudioService:
            self.audioservice = AudioService(self.emitter)

    @property
    def url_rss(self):
        pre_select = self.settings.get("pre_select", "")
        url_rss = self.settings.get("url_rss")
        if "not_set" in pre_select:
            # Use a custom RSS URL
            url_rss = self.settings.get("url_rss")
        else:
            # Use the selected preset's URL
            url_rss = pre_select

        if not url_rss and 'url_rss' in self.config:
            url_rss = self.config['url_rss']

        return url_rss

    @intent_handler(IntentBuilder("anycollusion").
        require("anycollusion").
        build())
    def handle_anycollusion_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('anycollusion')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("mymillenials").
        require("mymillenials").
        build())
    def handle_mymillenials_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('mymillenials')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("buildawall").
        require("buildawall").
        build())
    def handle_buildawall_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('buildawall')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("resistwemuch").
        require("resistwemuch").
        build())
    def handle_resistwemuch_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('resistwemuch')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("needs").
        require("needs").
        build())
    def handle_needs_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('needs')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("inthemorning").
        require("inthemorning").
        build())
    def handle_inthemorning_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('inthemorning')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("triggered").
        require("triggered").
        build())
    def handle_triggered_intent(self, message):
        try:
            self.stop()

            self.speak_dialog('NoAgenda')
            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('triggered')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            sleep(1.0)
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("penultimate").
        optionally("Play").
        require("penultimate").
        require("NoAgenda").
        build())
    def handle_penultimate_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[1]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('penultimate')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))


    @intent_handler(IntentBuilder("third").
        optionally("Play").
        require("3rd").
        require("NoAgenda").
        build())
    def handle_third_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[2]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('third')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("fourth").
        optionally("Play").
        require("4th").
        require("NoAgenda").
        build())
    def handle_fourth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[3]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('fourth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("fifth").
        optionally("Play").
        require("5th").
        require("NoAgenda").
        build())
    def handle_fifth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[4]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('fifth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("sixth").
        optionally("Play").
        require("6th").
        require("NoAgenda").
        build())
    def handle_sixth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[5]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('sixth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("seventh").
        optionally("Play").
        require("7th").
        require("NoAgenda").
        build())
    def handle_seventh_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[6]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('seventh')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("eighth").
        optionally("Play").
        require("8th").
        require("NoAgenda").
        build())
    def handle_eighth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[7]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('eighth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("ninth").
        optionally("Play").
        require("9th").
        require("NoAgenda").
        build())
    def handle_ninth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[8]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('ninth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("tenth").
        optionally("Play").
        require("10th").
        require("NoAgenda").
        build())
    def handle_tenth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[9]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('tenth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("eleventh").
        optionally("Play").
        require("11th").
        require("NoAgenda").
        build())
    def handle_eleventh_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[10]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('eleventh')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("twelfth").
        optionally("Play").
        require("12th").
        require("NoAgenda").
        build())
    def handle_twelfth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[11]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('twelfth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("thirteenth").
        optionally("Play").
        require("13th").
        require("NoAgenda").
        build())
    def handle_thirteenth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[12]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('thirteenth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("fourteenth").
        optionally("Play").
        require("14th").
        require("NoAgenda").
        build())
    def handle_fourteenth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[13]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('fourteenth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("fifteenth").
        optionally("Play").
        require("15th").
        require("NoAgenda").
        build())
    def handle_fifteenth_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[14]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('fifteenth')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    @intent_handler(IntentBuilder("query").
        require("query").
        optionally("latest").
        require("NoAgenda").
        build())
    def handle_query_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('query')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

    def stop(self):
        if self.audioservice:
            self.audioservice.stop()
        else:
            if self.process and self.process.poll() is None:
                self.process.terminate()
                self.process.wait()

    @intent_handler(IntentBuilder("latest").
        optionally("Play").
        optionally("latest").
        require("NoAgenda").
        build())
    def handle_latest_intent(self, message):
        try:
            self.stop()

            feeddata = feedparser.parse(self.url_rss)
            data = feeddata.entries[0]
            # Stop anything already playing

            url = data.enclosures[0]['url']
            LOG.info('latest')
            LOG.info(url)

            # After the intro, start the no agenda stream
            # if audio service module is available use it
            wait_while_speaking()
            if self.audioservice:
                LOG.info('AudioService')
                self.audioservice.play(url, message.data['utterance'])
            else:  # othervice use normal mp3 playback
                LOG.info('playmp3')
                self.process = play_mp3(url)

        except Exception as e:
            LOG.error("Error: {0}".format(e))

def create_skill():
    return NoAgendaSkill()
