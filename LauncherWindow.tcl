#############################################################################
# Generated by PAGE version 4.20
#  in conjunction with Tcl version 8.6
#  Feb 14, 2019 06:15:26 PM CET  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#
    menu .pop43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -font {{Segoe UI} 9} -foreground black \
        -tearoff 1 
    vTcl:DefineAlias ".pop43" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m85" -relief ridge -background {#d9d9d9} \
        -highlightbackground {#d9d9d9} -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 511x327+1247+587
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2564 1421
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "SQK FlyFF Server Starter"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    labelframe $top.lab44 \
        -font TkDefaultFont -foreground black -text Server \
        -background {#d9d9d9} -height 285 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 251 
    vTcl:DefineAlias "$top.lab44" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab44
    message $site_3_0.mes62 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes62" "ServMsg01" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes64 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes64" "ServState01" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC1 
    vTcl:DefineAlias "$site_3_0.che45" "ServCbx01" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che46 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC2 
    vTcl:DefineAlias "$site_3_0.che46" "ServCbx02" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che47 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC3 
    vTcl:DefineAlias "$site_3_0.che47" "ServCbx03" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che48 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC4 
    vTcl:DefineAlias "$site_3_0.che48" "ServCbx04" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che49 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC5 
    vTcl:DefineAlias "$site_3_0.che49" "ServCbx05" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che50 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC6 
    vTcl:DefineAlias "$site_3_0.che50" "ServCbx06" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $site_3_0.che51 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -justify left \
        -variable ServC7 
    vTcl:DefineAlias "$site_3_0.che51" "ServCbx07" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes52 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes52" "ServMsg02" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes53 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes53" "ServMsg03" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes54 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes54" "ServMsg04" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes55 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes55" "ServMsg05" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes56 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes56" "ServMsg06" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes57 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 120 
    vTcl:DefineAlias "$site_3_0.mes57" "ServMsg07" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes58 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes58" "ServState02" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes59 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes59" "ServState03" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes60 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes60" "ServState04" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes61 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes61" "ServState05" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes63 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes63" "ServState06" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes65 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 50 
    vTcl:DefineAlias "$site_3_0.mes65" "ServState07" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but69 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Start 
    vTcl:DefineAlias "$site_3_0.but69" "ServStart" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but70 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Stop 
    vTcl:DefineAlias "$site_3_0.but70" "ServStop" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.mes62 \
        -in $site_3_0 -x 50 -y 20 -width 120 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes64 \
        -in $site_3_0 -x 180 -y 20 -width 50 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.che45 \
        -in $site_3_0 -x 10 -y 20 -width 21 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.che46 \
        -in $site_3_0 -x 10 -y 50 -width 21 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che47 \
        -in $site_3_0 -x 10 -y 80 -width 21 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che48 \
        -in $site_3_0 -x 10 -y 110 -width 21 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che49 \
        -in $site_3_0 -x 10 -y 140 -width 21 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che50 \
        -in $site_3_0 -x 10 -y 170 -width 21 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.che51 \
        -in $site_3_0 -x 10 -y 200 -width 21 -height 25 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes52 \
        -in $site_3_0 -x 50 -y 50 -width 120 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes53 \
        -in $site_3_0 -x 50 -y 80 -width 120 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes54 \
        -in $site_3_0 -x 50 -y 110 -width 120 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes55 \
        -in $site_3_0 -x 50 -y 140 -width 120 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes56 \
        -in $site_3_0 -x 50 -y 170 -width 120 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes57 \
        -in $site_3_0 -x 50 -y 200 -width 120 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes58 \
        -in $site_3_0 -x 180 -y 50 -width 50 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes59 \
        -in $site_3_0 -x 180 -y 80 -width 50 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes60 \
        -in $site_3_0 -x 180 -y 110 -width 50 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes61 \
        -in $site_3_0 -x 180 -y 140 -width 50 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes63 \
        -in $site_3_0 -x 180 -y 170 -width 50 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes65 \
        -in $site_3_0 -x 180 -y 200 -width 50 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but69 \
        -in $site_3_0 -x 10 -y 230 -width 97 -relwidth 0 -height 44 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but70 \
        -in $site_3_0 -x 130 -y 230 -width 97 -height 44 -anchor nw \
        -bordermode ignore 
    labelframe $top.lab66 \
        -font TkDefaultFont -foreground black -text Client \
        -background {#d9d9d9} -height 245 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 240 
    vTcl:DefineAlias "$top.lab66" "Labelframe2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab66
    message $site_3_0.mes75 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 220 
    vTcl:DefineAlias "$site_3_0.mes75" "ClientState2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but76 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Start 
    vTcl:DefineAlias "$site_3_0.but76" "ClientStartBig" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but77 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Kill all} 
    vTcl:DefineAlias "$site_3_0.but77" "ClientKill" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but78 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Kill and Update} 
    vTcl:DefineAlias "$site_3_0.but78" "ClientUpdate" vTcl:WidgetProc "Toplevel1" 1
    message $site_3_0.mes79 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Message \
        -width 220 
    vTcl:DefineAlias "$site_3_0.mes79" "ClientState" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but43 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text Start 
    vTcl:DefineAlias "$site_3_0.but43" "ClientIni" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.mes75 \
        -in $site_3_0 -x 10 -y 50 -width 220 -relwidth 0 -height 23 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but76 \
        -in $site_3_0 -x 10 -y 120 -width 217 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but77 \
        -in $site_3_0 -x 10 -y 200 -width 217 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but78 \
        -in $site_3_0 -x 10 -y 160 -width 217 -height 34 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes79 \
        -in $site_3_0 -x 10 -y 20 -width 220 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but43 \
        -in $site_3_0 -x 10 -y 80 -width 217 -height 34 -anchor nw \
        -bordermode ignore 
    message $top.mes71 \
        -background {#d9d9d9} -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {FlyFF Server Launcher by SquonK, 2019} -width 240 
    vTcl:DefineAlias "$top.mes71" "Message1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.m85
    menu $site_3_0 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -font TkMenuFont -foreground {#000000} \
        -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab44 \
        -in $top -x 10 -y 20 -width 240 -relwidth 0 -height 285 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 260 -y 20 -width 240 -relwidth 0 -height 245 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.mes71 \
        -in $top -x 260 -y 280 -width 240 -relwidth 0 -height 23 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

