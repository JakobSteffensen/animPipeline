import nuke


def build_gizmo_menu():
    ''' Create the top menu '''
    pass

def build_menu():
    ''' Create the top menu '''
    pass

def build_toolbar():
    ''' Create the top menu '''

    #film_root = aiPipeline.aiConfig.expandSetting("ai_ProductionEpisodesPath")
    #asset_root = aiPipeline.aiConfig.expandSetting("ai_ProductionAssetPath")

    tb = nuke.menu("Nuke")
    tb.addCommand("   %s   " % "Advance/E2502_Dentist", "")
    tb.addCommand("[Previous]", "anim.app.nuke.io.previous_shot()")
    tb.addCommand("[Next]", "anim.app.nuke.io.next_shot()")
    tb.addCommand("[Settings]", "anim.app.nuke.util.select('Settings')")