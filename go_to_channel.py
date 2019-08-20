import sys
import xbmc, xbmcaddon, xbmcgui
import urllib

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')

if __name__ == '__main__':
    # Extract the info we'll send over to Skin Shortcuts
    channel_id = sys.listitem.getProperty('channel_id')

    if channel_id:
        # Go to YouTube channel
        runScript = "ActivateWindow(Videos, plugin://plugin.video.youtube/channel/" + channel_id + "/,return)"
        xbmc.executebuiltin( "%s" %( runScript ) )

    else:
        xbmcgui.Dialog().ok(__addonname__, channel_id)
