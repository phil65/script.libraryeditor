import sys, time, os
import xbmc, xbmcgui, xbmcaddon
import json
import time

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
        if self.TAG <> "":
            self._choose_action(self.TAG)      
            log("choose_action executed")
        elif self.DBID <> "":
            self._select_dialog()
        else:
            log("No DBID given")
            
    def _parse_argv( self ):
        try:
            params = dict( arg.split( '=' ) for arg in sys.argv[ 1 ].split( '&' ) )
        except:
            params = {}
        self.DBID = int(params.get( 'DBID', False ))
        self.PARAM_TYPE = str(params.get( 'type', "" ))         
        self.TAG = str(params.get( 'tag', "" ))         
        
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
     #       self._AddToList( xbmc.getLocalizedString(20416),"firstaired" )
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )
            self._AddToList( xbmc.getLocalizedString(20373),"season" )
            self._AddToList( xbmc.getLocalizedString(20359),"episode" )
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )
    #        self._AddToList( xbmc.getLocalizedString(20416),"title" )
        elif xbmc.getCondVisibility('Container.Content(artists)'):
            self.TYPE = "Artist"
   #         self._AddToList( xbmc.getLocalizedString(557),"str_artist" )
            self._AddToList( xbmc.getLocalizedString(515),"artist_genre" )
            self._AddToList( xbmc.getLocalizedString(21893),"born" )
            self._AddToList( xbmc.getLocalizedString(21894),"formed" )
            self._AddToList( xbmc.getLocalizedString(21821),"artist_description" )
            self._AddToList( xbmc.getLocalizedString(21897),"died" )
            self._AddToList( xbmc.getLocalizedString(21896),"disbanded" )
            self._AddToList( xbmc.getLocalizedString(21898),"yearsactive" )
            self._AddToList( xbmc.getLocalizedString(175),"artist_mood" )
            self._AddToList( xbmc.getLocalizedString(176),"artist_style" )
            self._AddToList( xbmc.getLocalizedString(21892),"instruments" )
        elif xbmc.getCondVisibility('Container.Content(albums)'):
            self.TYPE = "Album"
     #       self._AddToList( xbmc.getLocalizedString(369),"title" )
    #        self._AddToList( xbmc.getLocalizedString(557),"arr_artist" )
            self._AddToList( xbmc.getLocalizedString(345),"year" )
            self._AddToList( xbmc.getLocalizedString(175),"album_mood" )
            self._AddToList( xbmc.getLocalizedString(176),"album_style" )
            self._AddToList( xbmc.getLocalizedString(515),"album_genre" )
            self._AddToList( xbmc.getLocalizedString(21895),"themes" )
         #   self._AddToList( xbmc.getLocalizedString(515),"type" )
            self._AddToList( xbmc.getLocalizedString(21899),"albumlabel" )
            self._AddToList( xbmc.getLocalizedString(21821),"album_description" )
            self._AddToList( xbmc.getLocalizedString(563),"rating" )
        elif xbmc.getCondVisibility('Container.Content(songs)'):
            self.TYPE = "Song"
            self._AddToList( xbmc.getLocalizedString(369),"title" )
            self._AddToList( xbmc.getLocalizedString(557),"arr_artist" )
            self._AddToList( xbmc.getLocalizedString(558),"album" )
            self._AddToList( xbmc.getLocalizedString(515),"genre" )
            self._AddToList( xbmc.getLocalizedString(345),"year" )
            self._AddToList( xbmc.getLocalizedString(563),"rating" )
            self._AddToList( xbmc.getLocalizedString(569),"comment" )
            self._AddToList( xbmc.getLocalizedString(427),"disc" )
            self._AddToList( xbmc.getLocalizedString(554),"Track" )
            self._AddToList( "Delete File","delete" )
        dialogSelection = xbmcgui.Dialog()
        self.Edit_Selection = dialogSelection.select( __language__(32007), self.modeselect )
        if self.Edit_Selection == -1:
            return
        self._choose_action(self.identifierlist[self.Edit_Selection])
        self._select_dialog()

    def _choose_action( self,actionstring ):
             #override auto type
        log("choose_action executed")
        if self.PARAM_TYPE <> "":
            self.TYPE = self.PARAM_TYPE
        if actionstring == "title" : 
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Title'),self.TYPE,"title")
        elif actionstring == "originaltitle" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.OriginalTitle'),self.TYPE,"originaltitle")
        elif actionstring == "year" :
            self._edit_db_integer(self.TYPE,"year")
        elif actionstring == "episode" :
            self._edit_db_integer(self.TYPE,"episode")
        elif actionstring == "season" :
            self._edit_db_integer(self.TYPE,"season")
        elif actionstring == "track" :
            self._edit_db_integer(self.TYPE,"track")
        elif actionstring == "disc" :
            self._edit_db_integer(self.TYPE,"disc")
        elif actionstring == "genre" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Genre'),self.TYPE,"genre")
        elif actionstring == "artist_genre" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Artist_Genre)'),self.TYPE,"genre")
        elif actionstring == "album_genre" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Album_Genre)'),self.TYPE,"genre")
        elif actionstring == "writer" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Writer'),self.TYPE,"writer")
        elif actionstring == "director" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Director'),self.TYPE,"director")
        elif actionstring == "tagline" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Tagline'),self.TYPE,"tagline")
        elif actionstring == "plot" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Plot'),self.TYPE,"plot")
        elif actionstring == "plotoutline" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.PlotOutline'),self.TYPE,"plotoutline")
        elif actionstring == "top250" :
            self._edit_db_integer(self.TYPE,"top250")
        elif actionstring == "set" :
            self._edit_db_string("",self.TYPE,"set")
        elif actionstring == "tag" :
            self._edit_db_array("",self.TYPE,"tag")
        elif actionstring == "country" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Country'),self.TYPE,"country")
        elif actionstring == "studio" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Studio'),self.TYPE,"studio")
        elif actionstring == "mpaa" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Mpaa'),self.TYPE,"mpaa")
        elif actionstring == "trailer" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Trailer'),self.TYPE,"trailer")
        elif actionstring == "playcount" :
            self._edit_db_integer(self.TYPE,"playcount")
        elif actionstring == "rating" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Rating'),self.TYPE,"rating")
        elif actionstring == "premiered" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Premiered'),self.TYPE,"premiered")
        elif actionstring == "arr_artist" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Artist'),self.TYPE,"artist")
        elif actionstring == "str_artist" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Artist'),self.TYPE,"artist")
        elif actionstring == "albumlabel" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Album_Label)'),self.TYPE,"albumlabel")
        elif actionstring == "album" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Album'),self.TYPE,"album")
        elif actionstring == "tracknumber" :             #TrackNumber (needs checking)
            self._edit_db_string(xbmc.getInfoLabel('ListItem.TrackNumber'),self.TYPE,"track")
        elif actionstring == "firstaired" :             #firstaired (needs checking)
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Premiered'),self.TYPE,"firstaired")
        elif actionstring == "born" : 
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(artist_Born)'),self.TYPE,"born")
        elif actionstring == "formed" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(artist_Formed)'),self.TYPE,"formed")
        elif actionstring == "artist_description" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_Description)'),self.TYPE,"description")
        elif actionstring == "album_description" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Album_Description)'),self.TYPE,"description")
        elif actionstring == "died" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_Died)'),self.TYPE,"died")
        elif actionstring == "disbanded" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_Disbanded)'),self.TYPE,"disbanded")
        elif actionstring == "yearsactive" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Property(Artist_YearsActive)'),self.TYPE,"yearsactive")
        elif actionstring == "comment" :
            self._edit_db_string(xbmc.getInfoLabel('ListItem.Comment'),self.TYPE,"comment")
        elif actionstring == "artist_mood" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Artist_Mood)'),self.TYPE,"mood")
        elif actionstring == "artist_style" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Artist_Style)'),self.TYPE,"style")
        elif actionstring == "album_mood" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Album_Mood)'),self.TYPE,"mood")
        elif actionstring == "album_style" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Album_Style)'),self.TYPE,"style")
        elif actionstring == "instruments" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Artist_Instrument)'),self.TYPE,"instrument")
        elif actionstring == "themes" :
            self._edit_db_array(xbmc.getInfoLabel('ListItem.Property(Album_Theme)'),self.TYPE,"theme")
        elif actionstring == "delete" :
            os.unlink(xbmc.getInfoLabel('ListItem.FilenameAndPath'))
            
    def _AddToList( self, Label, identifier ):
        self.modeselect.append(Label)
        self.identifierlist.append(identifier)    
        
    def _edit_db_array( self,preset,type,label ):
        keyboard = xbmc.Keyboard(preset)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            string_array=json.dumps(keyboard.getText().split( ' / ' ))
            if ((type == "Song") or (type == "Album") or (type == "Artist")):
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,string_array,type.lower(),self.DBID))
            else:
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,string_array,type.lower(),self.DBID))
        else:
            return ""

    def _edit_db_integer( self,type,label ):
        InputLabel = xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028))
        if ((type == "Song") or (type == "Album") or (type == "Artist")):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,InputLabel,type.lower(),self.DBID))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,InputLabel,type.lower(),self.DBID))

    def _edit_db_string( self,preset,type,label ):
        keyboard = xbmc.Keyboard(preset)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            try:
                InputLabel=keyboard.getText()
                conv=time.strptime(InputLabel,"%d/%m/%Y")
              #  InputLabel = Time.strftime('%Y-%m-%d')
                InputLabel = time.strftime("%Y-%m-%d",conv)
            except Exception:
                sys.exc_clear()
            if ((type == "Song") or (type == "Album") or (type == "Artist")):
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": "%s", "%sid":%s }}' % (type,label,InputLabel,type.lower(),self.DBID))
            else:
                xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": "%s", "%sid":%s }}' % (type,label,InputLabel,type.lower(),self.DBID))
        else:
            return ""
                
if ( __name__ == "__main__" ):
    Main()
log('finished')
