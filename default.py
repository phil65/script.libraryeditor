import sys, time
import xbmc, xbmcgui, xbmcaddon
import json

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__language__     = __addon__.getLocalizedString

def log(txt):
    if isinstance (txt,str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % (__addonid__, txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

class Main:
    def __init__( self ):
        log('version %s started' % __addonversion__ )
        self._parse_argv()
        self._select_dialog()
            
    def _parse_argv( self ):
        try:
            params = dict( arg.split( '=' ) for arg in sys.argv[ 1 ].split( '&' ) )
        except:
            params = {}
        self.DBID = int(params.get( 'DBID', False ))
        
    def _select_dialog( self ):
        self.modeselect= []
        self.identifierlist= []
        if xbmc.getCondVisibility('Container.Content(movies)'):
            self.TYPE = "Movie"
            self._AddToList( xbmc.getLocalizedString(369),"title" )
            self._AddToList( xbmc.getLocalizedString(20376),"originaltitle" )
            self._AddToList( xbmc.getLocalizedString(345),"year" )
            self._AddToList( xbmc.getLocalizedString(515),"genre" )
            self._AddToList( xbmc.getLocalizedString(20417),"writer" )
            self._AddToList( xbmc.getLocalizedString(20339),"director" )
            self._AddToList( xbmc.getLocalizedString(202),"tagline" )
            self._AddToList( xbmc.getLocalizedString(207),"plot" )
            self._AddToList( xbmc.getLocalizedString(203),"plotoutline" )
            self._AddToList( xbmc.getLocalizedString(13409),"top250" )
            self._AddToList( xbmc.getLocalizedString(20457),"set" )
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )
            self._AddToList( xbmc.getLocalizedString(21875),"country" )
            self._AddToList( xbmc.getLocalizedString(572),"studio" )
            self._AddToList( xbmc.getLocalizedString(20074),"mpaa" )
            self._AddToList( xbmc.getLocalizedString(20410),"trailer" )
            self._AddToList( xbmc.getLocalizedString(567),"playcount" ) 
            self._AddToList( xbmc.getLocalizedString(563),"rating" )
        elif xbmc.getCondVisibility('Container.Content(tvshows)'):
            self.TYPE = "TVShow"
            self._AddToList( xbmc.getLocalizedString(369),"title" )
            self._AddToList( xbmc.getLocalizedString(20376),"originaltitle" )
            self._AddToList( xbmc.getLocalizedString(515),"genre" )
            self._AddToList( xbmc.getLocalizedString(207),"plot" )
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )
            self._AddToList( xbmc.getLocalizedString(572),"studio" )
            self._AddToList( xbmc.getLocalizedString(20074),"mpaa" )
            self._AddToList( xbmc.getLocalizedString(567),"playcount" )
            self._AddToList( xbmc.getLocalizedString(563),"rating" )
            self._AddToList( __language__(32001),"premiered" )
        elif xbmc.getCondVisibility('Container.Content(musicvideos)'):
            self.TYPE = "MusicVideo"
            self._AddToList( xbmc.getLocalizedString(369),"title" )
            self._AddToList( xbmc.getLocalizedString(345),"year" )
            self._AddToList( xbmc.getLocalizedString(515),"genre" )
            self._AddToList( xbmc.getLocalizedString(20339),"director" )
            self._AddToList( xbmc.getLocalizedString(207),"plot" )
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )
            self._AddToList( xbmc.getLocalizedString(572),"studio" )
            self._AddToList( xbmc.getLocalizedString(567),"playcount" )
        #    self._AddToList( xbmc.getLocalizedString(563),"title" )
            self._AddToList( xbmc.getLocalizedString(558),"album" )
            self._AddToList( xbmc.getLocalizedString(557),"arr_artist" )
            self._AddToList( xbmc.getLocalizedString(554),"track" )
        elif xbmc.getCondVisibility('Container.Content(episodes)'):
            self.TYPE = "Episode"
            self._AddToList( xbmc.getLocalizedString(369),"title" )
            self._AddToList( xbmc.getLocalizedString(20376),"originaltitle" )
            self._AddToList( xbmc.getLocalizedString(515),"genre" )
            self._AddToList( xbmc.getLocalizedString(207),"plot" )
            self._AddToList( xbmc.getLocalizedString(20339),"director" )
            self._AddToList( xbmc.getLocalizedString(20417),"writer" )
            self._AddToList( xbmc.getLocalizedString(20459),"tag" )
            self._AddToList( xbmc.getLocalizedString(572),"studio" )
            self._AddToList( xbmc.getLocalizedString(20074),"mpaa" )
            self._AddToList( xbmc.getLocalizedString(567),"playcount" )
            self._AddToList( xbmc.getLocalizedString(563),"rating" )
            self._AddToList( xbmc.getLocalizedString(20416),"firstaired" )
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )
            self._AddToList( xbmc.getLocalizedString(20373),"season" )
            self._AddToList( xbmc.getLocalizedString(20359),"episode" )
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )
        elif xbmc.getCondVisibility('Container.Content(artists)'):
            self.TYPE = "Artist"
            self._AddToList( xbmc.getLocalizedString(557),"str_artist" )#artist (String)
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(21893),"born" )#born
            self._AddToList( xbmc.getLocalizedString(21894),"formed" )#formed
            self._AddToList( xbmc.getLocalizedString(21821),"artist_description" )#description
            self._AddToList( xbmc.getLocalizedString(21897),"died" )#died
            self._AddToList( xbmc.getLocalizedString(21896),"disbanded" )#disbanded
            self._AddToList( xbmc.getLocalizedString(21898),"yearsactive" )#yearsactive
            self._AddToList( xbmc.getLocalizedString(175),"mood" )#mood
            self._AddToList( xbmc.getLocalizedString(176),"style" )#style
            self._AddToList( xbmc.getLocalizedString(21892),"instruments" )#Instrument
        elif xbmc.getCondVisibility('Container.Content(albums)'):
            self.TYPE = "Album"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(557),"arr_artist" )#artist (Array)
            self._AddToList( xbmc.getLocalizedString(345),"year" )#year
            self._AddToList( xbmc.getLocalizedString(175),"mood" )#mood
            self._AddToList( xbmc.getLocalizedString(176),"style" )#style
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(21895),"themes" )#themes
         #   self._AddToList( xbmc.getLocalizedString(515),"type" )#type
          #  self._AddToList( xbmc.getLocalizedString(515),"albumlabel" )#albumlabel
            self._AddToList( xbmc.getLocalizedString(21821),"album_description" )#description
            self._AddToList( xbmc.getLocalizedString(563),"rating" )#rating
        elif xbmc.getCondVisibility('Container.Content(songs)'):
            self.TYPE = "Song"
            self._AddToList( xbmc.getLocalizedString(369),"title" )#title
            self._AddToList( xbmc.getLocalizedString(557),"arr_artist" )#artist (Array)
            self._AddToList( xbmc.getLocalizedString(557),"artist" )#artist (Array)
            self._AddToList( xbmc.getLocalizedString(558),"album" )#Album
            self._AddToList( xbmc.getLocalizedString(515),"genre" )#genre
            self._AddToList( xbmc.getLocalizedString(345),"year" )#year
            self._AddToList( xbmc.getLocalizedString(563),"rating" )#rating
            self._AddToList( xbmc.getLocalizedString(569),"comment" )#comment
            self._AddToList( xbmc.getLocalizedString(427),"disc" )#disc
            self._AddToList( xbmc.getLocalizedString(554),"Track" )#Track
          
        dialogSelection = xbmcgui.Dialog()
        Edit_Selection = dialogSelection.select( __language__(32007), self.modeselect ) 
        if Edit_Selection == -1 :
            return
        elif self.identifierlist[Edit_Selection] == "title" : 
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Title'),self.TYPE,"title")
        elif self.identifierlist[Edit_Selection] == "originaltitle" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.OriginalTitle'),self.TYPE,"originaltitle")
        elif self.identifierlist[Edit_Selection] == "year" :
            self._edit_db_integer(self.TYPE,"year")
        elif self.identifierlist[Edit_Selection] == "episode" :
            self._edit_db_integer(self.TYPE,"episode")
        elif self.identifierlist[Edit_Selection] == "season" :
            self._edit_db_integer(self.TYPE,"season")
        elif self.identifierlist[Edit_Selection] == "track" :
            self._edit_db_integer(self.TYPE,"track")
        elif self.identifierlist[Edit_Selection] == "disc" :
            self._edit_db_integer(self.TYPE,"disc")
        elif self.identifierlist[Edit_Selection] == "genre" :
            genrestring = self._set_string(xbmc.getInfoLabel('ListItem.Genre'))
            self._edit_db_tag(json.dumps(genrestring.split( ' / ' )),self.TYPE,"genre")
        elif self.identifierlist[Edit_Selection] == "writer" :
            writerstring = self._set_string(xbmc.getInfoLabel('ListItem.Writer'))
            self._edit_db_tag(json.dumps(writerstring.split( ' / ' )),self.TYPE,"writer")
        elif self.identifierlist[Edit_Selection] == "director" :
            directorstring = self._set_string(xbmc.getInfoLabel('ListItem.Director'))
            self._edit_db_tag(json.dumps(directorstring.split( ' / ' )),self.TYPE,"director")
        elif self.identifierlist[Edit_Selection] == "tagline" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Tagline'),self.TYPE,"tagline")
        elif self.identifierlist[Edit_Selection] == "plot" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Plot'),self.TYPE,"plot")
        elif self.identifierlist[Edit_Selection] == "plotoutline" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.PlotOutline'),self.TYPE,"plotoutline")
        elif self.identifierlist[Edit_Selection] == "top250" :
            self._edit_db_integer(self.TYPE,"top250")
        elif self.identifierlist[Edit_Selection] == "set" :
            self._edit_db_string("",self.TYPE,"set")
        elif self.identifierlist[Edit_Selection] == "tag" :
            tagstring = self._set_string("") 
            self._edit_db_tag(json.dumps(tagstring.split( ' / ' )),self.TYPE,"tag")
        elif self.identifierlist[Edit_Selection] == "country" :
            countrystring = self._set_string(xbmc.getInfoLabel('ListItem.Country'))
            self._edit_db_tag(json.dumps(countrystring.split( ' / ' )),self.TYPE,"country")
        elif self.identifierlist[Edit_Selection] == "studio" :
            studiostring = self._set_string(xbmc.getInfoLabel('ListItem.Studio'))
            self._edit_db_tag(json.dumps(studiostring.split( ' / ' )),self.TYPE,"studio")
        elif self.identifierlist[Edit_Selection] == "mpaa" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Mpaa'),self.TYPE,"mpaa")
        elif self.identifierlist[Edit_Selection] == "trailer" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Trailer'),self.TYPE,"trailer")
        elif self.identifierlist[Edit_Selection] == "playcount" :
            self._edit_db_integer(self.TYPE,"playcount")
        elif self.identifierlist[Edit_Selection] == "rating" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Rating'),self.TYPE,"rating")
        elif self.identifierlist[Edit_Selection] == "premiered" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Premiered'),self.TYPE,"premiered")
        elif self.identifierlist[Edit_Selection] == "arr_artist" :
            artiststring = self._set_string("")
            self._edit_db_tag(json.dumps(artiststring.split( ' / ' )),self.TYPE,"artist")
        elif self.identifierlist[Edit_Selection] == "str_artist" :
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Artist'))),self.TYPE,"artist")
        elif self.identifierlist[Edit_Selection] == "album" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Album'),self.TYPE,"album")
        elif self.identifierlist[Edit_Selection] == "tracknumber" :             #TrackNumber (needs checking)
            self._edit_db_string(xbmc.getInfoLabel('ListItem.TrackNumber'),self.TYPE,"track")
        elif self.identifierlist[Edit_Selection] == "firstaired" :             #firstaired (needs checking)
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Premiered'),self.TYPE,"firstaired")
        elif self.identifierlist[Edit_Selection] == "born" : 
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(artist_Born)'),self.TYPE,"born")
        elif self.identifierlist[Edit_Selection] == "formed" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(artist_Formed)'),self.TYPE,"formed")
        elif self.identifierlist[Edit_Selection] == "artist_description" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_Description)'),self.TYPE,"description")
        elif self.identifierlist[Edit_Selection] == "album_description" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Album_Description)'),self.TYPE,"description")
        elif self.identifierlist[Edit_Selection] == "died" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_Died)'),self.TYPE,"died")
        elif self.identifierlist[Edit_Selection] == "disbanded" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_Disbanded)'),self.TYPE,"disbanded")
        elif self.identifierlist[Edit_Selection] == "yearsactive" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_YearsActive)'),self.TYPE,"yearsactive")
        elif self.identifierlist[Edit_Selection] == "comment" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Comment'),self.TYPE,"comment")
        elif self.identifierlist[Edit_Selection] == "mood" :
            moodstring = self._set_string("")
            self._edit_db_tag(json.dumps(moodstring.split( ' / ' )),self.TYPE,"mood")
        elif self.identifierlist[Edit_Selection] == "style" :
            stylestring = self._set_string("")
            self._edit_db_tag(json.dumps(stylestring.split( ' / ' )),self.TYPE,"style")
        elif self.identifierlist[Edit_Selection] == "instruments" :
            instrumentstring = self._set_string("")
            self._edit_db_tag(json.dumps(instrumentstring.split( ' / ' )),self.TYPE,"instrument")
        elif self.identifierlist[Edit_Selection] == "themes" :
            themestring = self._set_string("")
            self._edit_db_tag(json.dumps(themestring.split( ' / ' )),self.TYPE,"theme")
        self._select_dialog()
            
    def _set_string( self,preset ):
        keyboard = xbmc.Keyboard(preset)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            return keyboard.getText()
        else:
            return ""
            
    def _AddToList( self, Label, identifier ):
        self.modeselect.append(Label)
        self.identifierlist.append(identifier)    
        
    def _edit_db_tag( self,genre,type,label ):
        if ((type == "Song") or (type == "Album") or (type == "Artist")):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,genre,type.lower(),self.DBID))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,genre,type.lower(),self.DBID))

    def _edit_db_integer( self,type,label ):
        value = xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028))
        if ((type == "Song") or (type == "Album") or (type == "Artist")):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,value,type.lower(),self.DBID))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,value,type.lower(),self.DBID))

    def _edit_db_string( self,preset,type,label ):
        InputLabel = self._set_string(preset)
        if InputLabel <> "":
            if ((type == "Song") or (type == "Album") or (type == "Artist")):
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": "%s", "%sid":%s }}' % (type,label,InputLabel,type.lower(),self.DBID))
            else:
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": "%s", "%sid":%s }}' % (type,label,InputLabel,type.lower(),self.DBID))
                
if ( __name__ == "__main__" ):
    Main()
log('finished')
