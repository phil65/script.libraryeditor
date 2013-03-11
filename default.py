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
        modeselect= []  
        if xbmc.getCondVisibility('Container.Content(movies)'):
            self.TYPE = "Movie"
            modeselect.append( xbmc.getLocalizedString(369) )#title
            modeselect.append( xbmc.getLocalizedString(20376) )#originaltitle
            modeselect.append( xbmc.getLocalizedString(345) )#year
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(20417) )#writer
            modeselect.append( xbmc.getLocalizedString(20339) )#director
            modeselect.append( xbmc.getLocalizedString(202) )#Tagline
            modeselect.append( xbmc.getLocalizedString(207) )#Plot
            modeselect.append( xbmc.getLocalizedString(203) )#PlotOutline
            modeselect.append( xbmc.getLocalizedString(13409) )# top250
            modeselect.append( xbmc.getLocalizedString(20457) )#set
            modeselect.append( xbmc.getLocalizedString(20459) )#tag
            modeselect.append( xbmc.getLocalizedString(21875) )#Country
            modeselect.append( xbmc.getLocalizedString(572) )#Studio
            modeselect.append( xbmc.getLocalizedString(20074) )#MPAA
            modeselect.append( xbmc.getLocalizedString(20410) )#trailer
            modeselect.append( __language__(32023) )           #showlink
            modeselect.append( xbmc.getLocalizedString(567) ) #PlayCount
            modeselect.append( xbmc.getLocalizedString(563) ) #Rating
        elif xbmc.getCondVisibility('Container.Content(tvshows)'):
            self.TYPE = "TVShow"
            modeselect.append( xbmc.getLocalizedString(369) )#title
            modeselect.append( xbmc.getLocalizedString(20376) )#originaltitle
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(207) )#Plot
            modeselect.append( xbmc.getLocalizedString(20459) )#tag
            modeselect.append( xbmc.getLocalizedString(572) )#Studio
            modeselect.append( xbmc.getLocalizedString(20074) )#MPAA
            modeselect.append( xbmc.getLocalizedString(567) )#PlayCount
            modeselect.append( xbmc.getLocalizedString(563) )#Rating
            modeselect.append( __language__(32001) )#Premiered
        elif xbmc.getCondVisibility('Container.Content(musicvideos)'):
            self.TYPE = "MusicVideo"
            modeselect.append( xbmc.getLocalizedString(369) )#title
            modeselect.append( xbmc.getLocalizedString(345) )#year
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(20339) )#director
            modeselect.append( xbmc.getLocalizedString(207) )#Plot
            modeselect.append( xbmc.getLocalizedString(20459) )#tag
            modeselect.append( xbmc.getLocalizedString(572) )#Studio
            modeselect.append( xbmc.getLocalizedString(567) )#PlayCount
        #    modeselect.append( xbmc.getLocalizedString(563) )#Rating
            modeselect.append( xbmc.getLocalizedString(558) )#Album
            modeselect.append( xbmc.getLocalizedString(557) )#Artist
            modeselect.append( xbmc.getLocalizedString(554) )#Track
        elif xbmc.getCondVisibility('Container.Content(episodes)'):
            self.TYPE = "Episode"
            modeselect.append( xbmc.getLocalizedString(369) )#title
            modeselect.append( xbmc.getLocalizedString(20376) )#originaltitle
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(207) )#Plot
            modeselect.append( xbmc.getLocalizedString(20339) )#director
            modeselect.append( xbmc.getLocalizedString(20417) )#writer
            modeselect.append( xbmc.getLocalizedString(20459) )#tag
            modeselect.append( xbmc.getLocalizedString(572) )#Studio
            modeselect.append( xbmc.getLocalizedString(20074) )#MPAA
            modeselect.append( xbmc.getLocalizedString(567) )#PlayCount
            modeselect.append( xbmc.getLocalizedString(563) )#Rating
            modeselect.append( xbmc.getLocalizedString(20416) )#FirstAired
    #        modeselect.append( xbmc.getLocalizedString(20416) )#ProductionCode
            modeselect.append( xbmc.getLocalizedString(20373) )#Season
            modeselect.append( xbmc.getLocalizedString(20359) )#Episode
    #        modeselect.append( xbmc.getLocalizedString(20416) )#EpisodeGuide
    #        modeselect.append( xbmc.getLocalizedString(20416) )#imdbnumber
        elif xbmc.getCondVisibility('Container.Content(artists)'):
            self.TYPE = "Artist"
            modeselect.append( xbmc.getLocalizedString(557) )#Artist (String)
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(21893) )#born
            modeselect.append( xbmc.getLocalizedString(21894) )#formed
            modeselect.append( xbmc.getLocalizedString(21821) )#description
            modeselect.append( xbmc.getLocalizedString(21897) )#died
            modeselect.append( xbmc.getLocalizedString(21896) )#disbanded
            modeselect.append( xbmc.getLocalizedString(21898) )#yearsactive
            modeselect.append( xbmc.getLocalizedString(175) )#Mood
            modeselect.append( xbmc.getLocalizedString(176) )#Style
            modeselect.append( xbmc.getLocalizedString(21892) )#Instrument
        elif xbmc.getCondVisibility('Container.Content(albums)'):
            self.TYPE = "Album"
            modeselect.append( xbmc.getLocalizedString(369) )#title
            modeselect.append( xbmc.getLocalizedString(557) )#Artist (Array)
            modeselect.append( xbmc.getLocalizedString(345) )#year
            modeselect.append( xbmc.getLocalizedString(175) )#Mood
            modeselect.append( xbmc.getLocalizedString(176) )#Style
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(515) )#theme
            modeselect.append( xbmc.getLocalizedString(515) )#type
            modeselect.append( xbmc.getLocalizedString(515) )#albumlabel
            modeselect.append( xbmc.getLocalizedString(21821) )#description
            modeselect.append( xbmc.getLocalizedString(563) )#Rating
        elif xbmc.getCondVisibility('Container.Content(songs)'):
            self.TYPE = "Song"
            modeselect.append( xbmc.getLocalizedString(369) )#title
            modeselect.append( xbmc.getLocalizedString(557) )#Artist (Array)
            modeselect.append( xbmc.getLocalizedString(557) )#AlbumArtist (Array)
            modeselect.append( xbmc.getLocalizedString(557) )#Album
            modeselect.append( xbmc.getLocalizedString(515) )#genre
            modeselect.append( xbmc.getLocalizedString(345) )#year
            modeselect.append( xbmc.getLocalizedString(563) )#Rating
            modeselect.append( xbmc.getLocalizedString(563) )#Comment
            modeselect.append( xbmc.getLocalizedString(563) )#Disc
            modeselect.append( xbmc.getLocalizedString(563) )#Track
          
        dialogSelection = xbmcgui.Dialog()
        Edit_Selection = dialogSelection.select( __language__(32007), modeselect ) 
        if Edit_Selection == -1 :
            return
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(369) :         #Title
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Title'))),self.TYPE,"title")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20376) :         #OriginalTitle
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.OriginalTitle'))),self.TYPE,"originaltitle")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(345) :         #Year
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"year")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20359) :         #Episode
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"episode")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20373) :         #Season
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"season")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(515) :         #Genre
            genrestring = self._set_string(xbmc.getInfoLabel('ListItem.Genre'))
            self._edit_db_tag(json.dumps(genrestring.split( ' / ' )),self.TYPE,"genre")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20417) :         #Writer
            writerstring = self._set_string(xbmc.getInfoLabel('ListItem.Writer'))
            self._edit_db_tag(json.dumps(writerstring.split( ' / ' )),self.TYPE,"writer")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20339) :         #Director
            directorstring = self._set_string(xbmc.getInfoLabel('ListItem.Director'))
            self._edit_db_tag(json.dumps(directorstring.split( ' / ' )),self.TYPE,"director")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(202) :         #Tagline
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Tagline'))),self.TYPE,"tagline")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(207) :         #Plot
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Plot'))),self.TYPE,"plot")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(203) :         #PlotOutlne
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.PlotOutline'))),self.TYPE,"plotoutline")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(13409) :         #Top250
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"top250")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20457) :         #Set
            self._edit_db_tag(json.dumps(self._set_string("")),self.TYPE,"set")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20459) :         #Tag
            tagstring = self._set_string("") 
            self._edit_db_tag(json.dumps(tagstring.split( ' / ' )),self.TYPE,"tag")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(21875) :         #Country
            countrystring = self._set_string(xbmc.getInfoLabel('ListItem.Country'))
            self._edit_db_tag(json.dumps(countrystring.split( ' / ' )),self.TYPE,"country")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(572) :         #Studio
            studiostring = self._set_string(xbmc.getInfoLabel('ListItem.Studio'))
            self._edit_db_tag(json.dumps(studiostring.split( ' / ' )),self.TYPE,"studio")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20074) :         #Mpaa
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Mpaa'))),self.TYPE,"mpaa")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20410) :         #Trailer
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Trailer'))),self.TYPE,"trailer")
        elif modeselect[Edit_Selection] == __language__(32023) :            #Showlink
            showlinkstring = self._set_string("")
            self._edit_db_tag(json.dumps(showlinkstring.split( ' / ' )),self.TYPE,"showlink")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(567) :            #PlayCount
            self._edit_db_tag(xbmcgui.Dialog().numeric(0, xbmc.getLocalizedString(16028)),self.TYPE,"playcount")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(563) :            #Rating
            self._edit_db_tag(self._set_string(xbmc.getInfoLabel('ListItem.Rating')),self.TYPE,"rating")
        elif modeselect[Edit_Selection] == __language__(32001) :             #Premiered
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Premiered'))),self.TYPE,"premiered")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(557) :             #Artist
            artiststring = self._set_string("")
            self._edit_db_tag(json.dumps(artiststring.split( ' / ' )),self.TYPE,"artist")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(558) :             #Album
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Album'))),self.TYPE,"album")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(554) :             #TrackNumber (needs checking)
            self._edit_db_tag(self._set_string(xbmc.getInfoLabel('ListItem.TrackNumber')),self.TYPE,"track")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(20416) :             #firstaired (needs checking)
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Premiered'))),self.TYPE,"firstaired")       
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(21893) :             #born
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Born)'))),self.TYPE,"born")
        elif modeselect[Edit_Selection] == xbmc.getLocalizedString(21893) :             #formed
            self._edit_db_tag(json.dumps(self._set_string(xbmc.getInfoLabel('ListItem.Property(Artist_Formed)'))),self.TYPE,"formed")
        self._select_dialog()
            
    def _set_string( self,preset ):
        keyboard = xbmc.Keyboard(preset)
        keyboard.doModal()
        if (keyboard.isConfirmed()):
            return keyboard.getText()
        else:
            return ""
                         
    def _edit_db_tag( self,genre,type,label ):
        if ((type == "Song") or (type == "Album") or (type == "Artist")):
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "AudioLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,genre,type.lower(),self.DBID))
        else:
            xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "VideoLibrary.Set%sDetails", "params": { "%s": %s, "%sid":%s }}' % (type,label,genre,type.lower(),self.DBID))
                
if ( __name__ == "__main__" ):
    Main()
log('finished')
