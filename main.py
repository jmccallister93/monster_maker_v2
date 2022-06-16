from doctest import master
from msilib.schema import ComboBox
import string
import tkinter
import tkinter.messagebox
from turtle import width
import customtkinter
from tkinter import *
import random
from spells import *
from score_modifier import *


#TODO List:
# 1. ORGANIZE 
# 2. Figure out add health value button based on health pool 
# 3. Figure out Special Traits/Actions/Spells/Legendary/Lair Buttons and how to make them work
#    - Probably best to pop these into new windows 
# 4. Create a remove function to remove a stat
# 5. Create a save option to save stats to file
# 6. Fix Error Popup window when on "Random" to register the value as already added
# 7. Create command for the Generate Monster button to encompass and "Add" Buttons
# 8. Get Data for Actions/Legendary/Lair - Half way Done
# 9. Format Spells data to link to dndbeyond.com for descriptions (possilby?) 
# 10. Calculate Save bonuses based on stats given
# 11. Legendary Resistances, where to put them?
# 12. Add None options to optional Stats


#Set starting apperances
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Create main window class
class App(customtkinter.CTk):

    WIDTH = 1450
    HEIGHT = 900
    #Labels for displaying stats
    monster_stat_list = [
                            "Monster Name",
                            "Size",
                            "Monster Type",
                            "AC Type",
                            "AC",
                            "HP",
                            "Speed",
                            "Extra Move Type",
                            "STR",
                            "DEX",
                            "CON",
                            "INT",
                            "WIS",
                            "CHA",
                            "Saves",
                            "Skills",
                            "Vulnerabilities",
                            "Immunities",
                            "Resistances",
                            "Senses",
                            "Languages",
                            "Special Traits",
                            "Actions",
                            "Legendary Actions",
                            "Lair Actions",
                            "Spells"
                        ]

    def __init__(self):
        super().__init__()

        self.title("Monster Maker")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        #------------Setup Frames---------------#
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        #configure left frame
        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe", padx=10,pady=10)
        #configure right frame
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
        #Far Left Frame
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing        
        
        #-----------Generate Button function --------------#
        #TODO
        #Create a generate function for button 
        def generate_monster():
            pass

        #Create Generate Button
        generate_monster_button = customtkinter.CTkButton(master=self.frame_left, 
                                                        text="Generate Monster", 
                                                        command=generate_monster,
                                                        text_font=("Roboto Medium", 16))
        generate_monster_button.grid(row=0, column=0, columnspan = 4, padx=5,pady=10)
        
        #----------- Create Monster Options ------------#
        #--------Monster Name---------#
        monster_name_entry = customtkinter.CTkEntry(master=self.frame_right, placeholder_text='Enter Name')
        monster_name_entry.grid(row=0,column=1)
        monster_name = monster_name_entry.get()
        print(monster_name)

        #-------Size--------#
        #Size Combobox
        size_label = customtkinter.CTkLabel(master=self.frame_left, text="Size Option")
        size_label.grid(row=1,column=0)
        size_options_combobox = ["Random", "Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
        size_options_label = ["Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
        size_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=size_options_combobox)
        size_combobox.grid(row=1, column=1)
        size_combobox.set("Random")
        
        #Add size function
        def add_size():
            size_choice = StringVar()
            size_choice = size_combobox.get()
            random_size = random.choice(size_options_label)
            if size_choice == "Random":
                display_size['text'] = random_size
                
            else:
                display_size['text'] = size_choice
            
            
        # #Display Size
        display_size = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_size.grid(row=1,column=1)
        
        #Create button to add a size
        add_size_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_size, width=30)
        add_size_btn.grid(row=1, column=2, sticky = "W")

        #-------Monster Type--------#
        #Monster type Combobox
        monster_type_label = customtkinter.CTkLabel(master=self.frame_left, text="Monster Type Option")
        monster_type_label.grid(row=2,column=0)
        monster_type_options_combobox = ["Random","Aberration", "Beast", 
                        "Celestial", "Construct", "Dragon", 
                        "Elemental", "Fey", "Fiend", 
                        "Giant", "Humanoid", "Monstrosity", 
                        "Ooze", "Plant", "Undead"
                        ]
        monster_type_options_label = ["Aberration", "Beast", 
                        "Celestial", "Construct", "Dragon", 
                        "Elemental", "Fey", "Fiend", 
                        "Giant", "Humanoid", "Monstrosity", 
                        "Ooze", "Plant", "Undead"
                        ]
        monster_type_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=monster_type_options_combobox)
        monster_type_combobox.grid(row=2, column=1)
        monster_type_combobox.set("Random")
        
        #Add Monster Type function
        def add_monster_type():
            monster_type_choice = StringVar()
            monster_type_choice = monster_type_combobox.get()
            monster_random_type = random.choice(monster_type_options_label)
            if monster_type_choice == "Random":
                display_monster_type['text'] = monster_random_type
            else:
                display_monster_type['text'] = monster_type_choice
        #Display Type
        display_monster_type = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_monster_type.grid(row=2,column=1)
        #Create button to add a monster type
        add_monster_type_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_monster_type, width=30)
        add_monster_type_btn.grid(row=2, column=2, sticky="W")

        # ---------------- AC Options --------------#
        #AC type Combobox
        ac_type_label = customtkinter.CTkLabel(master=self.frame_left, text="AC Type Option")
        ac_type_label.grid(row=3,column=0)
        ac_type_options_combobox = ["Random", "Ancestral", "Magic", "Natural", "Worn"]
        ac_type_options_label = ["Ancestral", "Magic", "Natural", "Worn"]
        ac_type_combobox = customtkinter.CTkComboBox(master=self.frame_left, values= ac_type_options_combobox)
        ac_type_combobox.grid(row=3, column=1)
        ac_type_combobox.set("Random")
        current_ac_type = ac_type_combobox.current_value
        #Add AC Type function
        def add_ac_type():
            ac_type_choice = StringVar()
            ac_type_choice = ac_type_combobox.get()
            random_ac_type = random.choice(ac_type_options_label)
            if ac_type_choice == "Random":
                display_ac_type['text'] = random_ac_type
            else:
                display_ac_type['text'] = ac_type_choice
        #Display AC Type
        display_ac_type = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_ac_type.grid(row=3,column=1)
        #Create button to add a AC Type
        add_ac_type_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_ac_type, width=30)
        add_ac_type_btn.grid(row=3, column=2, sticky = "W")
        
        #---------AC Value--------#
        #AC Value Combobox
        ac_value_label = customtkinter.CTkLabel(master=self.frame_left, text="AC Value Option")
        ac_value_label.grid(row=4,column=0)
        ac_value_options_combobox = ["Random",
                    "7","8","9","10",
                    "11","12","13","14",
                    "15","16","17","18",
                    "19","20","21","22",
                    "23","24","25","26",
                    ]
        ac_value_options_label = [
                    "7","8","9","10",
                    "11","12","13","14",
                    "15","16","17","18",
                    "19","20","21","22",
                    "23","24","25","26",
                    ]
        ac_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, values= ac_value_options_combobox)
        ac_value_combobox.grid(row=4, column=1)
        ac_value_combobox.set("Random")
        current_ac_value = ac_value_combobox.current_value

        #Add AC Value function
        def add_ac_value():
            ac_value_choice = StringVar()
            ac_value_choice = ac_value_combobox.get()
            random_ac_value = random.choice(ac_value_options_label)
            if ac_value_choice == "Random":
                display_ac_value['text'] = random_ac_value
            else:
                display_ac_value['text'] = ac_value_choice
        #Display AC Value
        display_ac_value = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_ac_value.grid(row=4,column=1)
        #Create button to add AC Value
        add_ac_value_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_ac_value, width=30)
        add_ac_value_btn.grid(row=4, column=2, sticky="w")



        # ---------------- HP Pool Option --------------#
        hp_pool_options = {"Low" : (
                        "5","10","15","20",
                        "25","30","35","40",
                        "45","50","55","60",
                        "65","70","75","80",
                        "85","90","95","100"),

                    "Medium" : (
                        "105","110","115","120",
                        "125","130","135","140",
                        "145","150","155","160",
                        "165","170","175","180",
                        "185","190","195","200",),

                    "High" : (
                        "205","210","215","220",
                        "225","230","235","240",
                        "245","250","255","260",
                        "265","270","275","280",
                        "285","290","295","300",),

                    "Extreme" : (
                        "325","350","375","400",
                        "425","450","475","500",
                        "525","550","575","600",
                        "625","650","675","700",
                        "725","750","775","800",)}
        
        def on_pool_selected(hp_value):
            hp_values = ('Random',)
            if hp_value == 'Random':
                for v in hp_pool_options.values():
                    hp_values += v
            else:
                hp_values += hp_pool_options[hp_value]
            hp_value_combobox.configure(values=hp_values)
            hp_value_combobox.set('Random')
            
        
        #Label
        hp_pool_label = customtkinter.CTkLabel(master=self.frame_left, text="HP Pool Option")
        hp_pool_label.grid(row=5,column=0)
        hp_var1 = customtkinter.StringVar()
        hp_pool_combobox = customtkinter.CTkComboBox(master=self.frame_left, 
                                        variable=hp_var1, 
                                        values=("Random",)+tuple(hp_pool_options.keys()), 
                                        command=on_pool_selected)
        hp_pool_combobox.grid(row=5, column=1)
        
        hp_value_label = customtkinter.CTkLabel(master=self.frame_left, text="Hp Value Option")
        hp_value_label.grid(row=6,column=0)

        hp_var2 = customtkinter.StringVar()
        hp_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, variable=hp_var2)
        hp_value_combobox.grid(row=6, column=1)
        hp_value_combobox.set("Random")
        hp_pool_combobox.set("Random")
        
        # #TODO
        # #Add HP Value function
        # def add_hp_value():
        #     hp_value_choice = StringVar()
        #     hp_value_choice = hp_value_combobox.get()
        #     random_hp_value = random.choice(hp_values)
        #     if hp_value_choice == "Random":
        #         display_hp_value['text'] = random_hp_value
        #     else:
        #         display_hp_value['text'] = hp_value_choice

        #Display HP Value
        display_hp_value = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_hp_value.grid(row=5,column=1)
        #Create button to add HP Value
        add_hp_value_btn = customtkinter.CTkButton(master=self.frame_left, text="+", width=30) #TODO , command=add_hp_value()
        add_hp_value_btn.grid(row=6, column=2, sticky="w")

        # ----------Movement Options ------------#
        # Base Movement Speed Combobox
        move_speed_label = customtkinter.CTkLabel(master=self.frame_left, text="Base Move Speed Option")
        move_speed_label.grid(row=7,column=0)
        move_speed_options_combobox = ["Random", 
                                        "10 ft","20 ft","30 ft",
                                        "40 ft","50 ft","60 ft",
                                        "70 ft","80 ft","90 ft",
                                        "100 ft","110 ft","120 ft"
                                        ]
        move_speed_options_label = [
                                        "10 ft","20 ft","30 ft",
                                        "40 ft","50 ft","60 ft",
                                        "70 ft","80 ft","90 ft",
                                        "100 ft","110 ft","120 ft"
                                        ]
        move_speed_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=move_speed_options_combobox)
        move_speed_combobox.grid(row=7, column=1)
        move_speed_combobox.set("Random")
        
        #Add Move Speed function
        def add_move_speed():
            move_speed_choice = StringVar()
            move_speed_choice = move_speed_combobox.get()
            random_move_speed = random.choice(move_speed_options_label)
            if move_speed_choice == "Random":
                display_move_speed['text'] = random_move_speed
            else:
                display_move_speed['text'] = move_speed_choice
        #Display Move Speed
        display_move_speed = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_move_speed.grid(row=6,column=1)
        
        #Create button to add Move Speed
        add_move_speed_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_move_speed, width=30)
        add_move_speed_btn.grid(row=7, column=2, sticky ="w")

        # ------------Extra Move Type /Speed --------------#
        #Extra Movement Type Combobox
        extra_move_type_label = customtkinter.CTkLabel(master=self.frame_left, text="Extra Move Type Option")
        extra_move_type_label.grid(row=8,column=0)
        extra_move_type_options_combobox = ["Random", "Burrow", "Climb", "Fly", "Swim"]
        extra_move_type_options_label = [ "Burrow", "Climb", "Fly", "Swim"]
        extra_move_type_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=extra_move_type_options_combobox)
        extra_move_type_combobox.grid(row=8, column=1)
        extra_move_type_combobox.set("Random")
        current_extra_move_type = extra_move_type_combobox.current_value
        #Create list of move speeds
        extra_move_list = []    

        #Add Extra Move Type function
        def add_extra_move_type():
            #Type
            extra_move_type_choice = StringVar()
            extra_move_type_choice = extra_move_type_combobox.get()
            random_extra_move_type = random.choice(extra_move_type_options_label)
            #Speed
            extra_move_speed_choice = StringVar()
            extra_move_speed_choice = extra_move_speed_combobox.get()
            random_extra_move_speed = random.choice(extra_move_speed_options_label)

            if any(extra_move_type_choice in s for s in extra_move_list):
                tkinter.messagebox.showinfo('Error', f'{extra_move_type_choice} Movement type already added.')
            else:                              
                if extra_move_type_choice == "Random" and extra_move_speed_choice == "Random":
                    extra_move_list.append(random_extra_move_type + ' ' + random_extra_move_speed)
                    display_extra_move_type['text'] = ' | '.join(extra_move_list)
                                                
                elif extra_move_type_choice == "Random" and extra_move_speed_choice != "Random":
                    extra_move_list.append(random_extra_move_type + ' ' + extra_move_speed_choice)
                    display_extra_move_type['text'] = ' | '.join(extra_move_list)

                elif extra_move_type_choice !="Random" and extra_move_speed_choice == "Random":
                    extra_move_list.append(extra_move_type_choice + ' ' + random_extra_move_speed)
                    display_extra_move_type['text'] = ' | '.join(extra_move_list)

                elif extra_move_type_choice !="Random" and extra_move_speed_choice != "Random":
                    extra_move_list.append(extra_move_type_choice + ' ' + extra_move_speed_choice)
                    display_extra_move_type['text'] = ' | '.join(extra_move_list)

        #Extra Speed
        extra_move_speed_options_combobox = ["Random", 
                            "10 ft","20 ft","30 ft",
                            "40 ft","50 ft","60 ft",
                            "70 ft","80 ft","90 ft",
                            "100 ft","110 ft","120 ft"
                            ]
        extra_move_speed_options_label = [ 
                            "10 ft","20 ft","30 ft",
                            "40 ft","50 ft","60 ft",
                            "70 ft","80 ft","90 ft",
                            "100 ft","110 ft","120 ft"
                            ]

        extra_move_speed_label = customtkinter.CTkLabel(master=self.frame_left, text="Extra Move Speed Option")
        extra_move_speed_label.grid(row=9,column=0)
        extra_move_speed_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=extra_move_speed_options_combobox)
        extra_move_speed_combobox.grid(row=9, column=1)
        extra_move_speed_combobox.set("Random")

        #Display Extra Move Speed
        display_extra_move_type = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_extra_move_type.grid(row=7,column=1)
        #Create button to add Move Extra Speed
        add_extra_move_type_btn = customtkinter.CTkButton(master=self.frame_left, text="+",command=add_extra_move_type, width=30)
        add_extra_move_type_btn.grid(row=9, column=2, sticky="w")

        


        # ---------- Monster Stats --------- #
        #Stats options
        stats_options_combobox = [
            "Random",
            "1","2","3","4","5","6","7","8",
            "9","10","11","12","13",
            "14","15","16","17","18",
            "19","20","21","22","23",
            "24","25","26","27","28",
            "29","30",
        ]
        stats_options_label = [
            "1","2","3","4","5","6","7","8",
            "9","10","11","12","13",
            "14","15","16","17","18",
            "19","20","21","22","23",
            "24","25","26","27","28",
            "29","30",
        ]

        #STR Combobox
        str_label = customtkinter.CTkLabel(master=self.frame_left, text="STR Option")
        str_label.grid(row=10,column=0)
        str_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        str_combobox.grid(row=10, column=1)
        str_combobox.set("Random")
        current_str = str_combobox.current_value
        #Add str Value function
        def add_str():
            str_choice = StringVar()
            str_choice = str_combobox.get()
            random_str = random.choice(stats_options_label)
            if str_choice == "Random":
                display_str['text'] = random_str
            else:
                display_str['text'] = str_choice
        #Display STR Value
        display_str = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_str.grid(row=8,column=1)
        #Create button to add STR Value
        add_str_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_str, width=30)
        add_str_btn.grid(row=10, column=2, sticky="w")

        #DEX Combobox
        dex_label = customtkinter.CTkLabel(master=self.frame_left, text="DEX Option")
        dex_label.grid(row=11,column=0)
        dex_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        dex_combobox.grid(row=11, column=1)
        dex_combobox.set("Random")
        current_dex = dex_combobox.current_value
        #Add DEX Value function
        def add_dex():
            dex_choice = StringVar()
            dex_choice = dex_combobox.get()
            random_dex = random.choice(stats_options_label)
            if dex_choice == "Random":
                display_dex['text'] = random_dex
            else:
                display_dex['text'] = dex_choice
        #Display DEX Value
        display_dex = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_dex.grid(row=9,column=1)
        #Create button to add DEX Value
        add_dex_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_dex, width=30)
        add_dex_btn.grid(row=11, column=2,sticky="w")

        #CON Combobox
        con_label = customtkinter.CTkLabel(master=self.frame_left, text="CON Option")
        con_label.grid(row=12,column=0)
        con_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        con_combobox.grid(row=12, column=1)
        con_combobox.set("Random")
        current_con = con_combobox.current_value
        #Add con Value function
        def add_con():
            con_choice = StringVar()
            con_choice = con_combobox.get()
            random_con = random.choice(stats_options_label)
            if con_choice == "Random":
                display_con['text'] = random_con
            else:
                display_con['text'] = con_choice
        #Display con Value
        display_con = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_con.grid(row=10,column=1)
        #Create button to add con Value
        add_con_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_con,width=30)
        add_con_btn.grid(row=12, column=2,sticky="w")

        #INT Combobox
        int_label = customtkinter.CTkLabel(master=self.frame_left, text="INT Option")
        int_label.grid(row=13,column=0)
        int_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        int_combobox.grid(row=13, column=1)
        int_combobox.set("Random")
        current_int = int_combobox.current_value
        #Add int Value function
        def add_int():
            int_choice = StringVar()
            int_choice = int_combobox.get()
            random_int = random.choice(stats_options_label)
            if int_choice == "Random":
                display_int['text'] = random_int
            else:
                display_int['text'] = int_choice
        #Display int Value
        display_int = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_int.grid(row=11,column=1)
        #Create button to add int Value
        add_int_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_int, width=30)
        add_int_btn.grid(row=13, column=2,sticky="w")

        #WIS Combobox
        wis_label = customtkinter.CTkLabel(master=self.frame_left, text="WIS Option")
        wis_label.grid(row=14,column=0)
        wis_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        wis_combobox.grid(row=14, column=1)
        wis_combobox.set("Random")
        current_wis = wis_combobox.current_value
        #Add wis Value function
        def add_wis():
            wis_choice = StringVar()
            wis_choice = wis_combobox.get()
            random_wis = random.choice(stats_options_label)
            if wis_choice == "Random":
                display_wis['text'] = random_wis
            else:
                display_wis['text'] = wis_choice
        #Display wis Value
        display_wis = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_wis.grid(row=12,column=1)
        #Create button to add wis Value
        add_wis_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_wis, width=30)
        add_wis_btn.grid(row=14, column=2, sticky="w")

        #CHA Combobox
        cha_label = customtkinter.CTkLabel(master=self.frame_left, text="CHA Option")
        cha_label.grid(row=15,column=0)
        cha_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options_combobox)
        cha_combobox.grid(row=15, column=1)
        cha_combobox.set("Random")
        current_cha = cha_combobox.current_value
        #Add cha Value function
        def add_cha():
            cha_choice = StringVar()
            cha_choice = cha_combobox.get()
            random_cha = random.choice(stats_options_label)
            if cha_choice == "Random":
                display_cha['text'] = random_cha
                calculate_score_modifier(random_cha)
            else:
                display_cha['text'] = cha_choice
                calculate_score_modifier(cha_choice)
            
            


        #Display cha Value
        display_cha = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_cha.grid(row=13,column=1)
        #Create button to add cha Value
        add_cha_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_cha, width=30)
        add_cha_btn.grid(row=15, column=2, sticky="w")

        #---------Modifiers----------#
        #TODO
        #Just adding to the bottom for now
        #Stat Score Modifier Calculator ~ Temporary 
        #Stat Modifier Label right frame
        stat_modifier = customtkinter.CTkLabel(master=self.frame_right, text="Stat Modifiers: ")
        stat_modifier.grid(row=26,column=0)
        stat_modifier_display = customtkinter.CTkLabel(master=self.frame_right, text='')
        stat_modifier_display.grid(row=26, column=1)
        
        
        # ----------- Skills ------------#
        #Skills combobox
        skills_label = customtkinter.CTkLabel(master=self.frame_left, text="Skills Option")
        skills_label.grid(row=16,column=0)
        skills_options_combobox = ["Random","None","Acrobatics","Animal Handling",
                        "Arcana","Athletics","Deception",
                        "History","Insight","Intimidation",
                        "Investigation","Medicine","Nature",
                        "Perception","Performance","Persuasion",
                        "Religion","Sleight of Hand","Stealth",
                        "Survival",
                        ]
        skills_options_label = ["Random","None","Acrobatics","Animal Handling",
                        "Arcana","Athletics","Deception",
                        "History","Insight","Intimidation",
                        "Investigation","Medicine","Nature",
                        "Perception","Performance","Persuasion",
                        "Religion","Sleight of Hand","Stealth",
                        "Survival",
                        ]
        skills_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=skills_options_combobox)
        skills_combobox.grid(row=16, column=1)
        skills_combobox.set("Random")
        current_skills = skills_combobox.current_value
        #Skills value combobox
        skills_value_options_combobox = ["Random","+1","+2","+3",
                                    "+4","+5","+6","+7","+8",
                                    "+9","+10"]
        skills_value_options_label = ["+1","+2","+3",
                                    "+4","+5","+6","+7","+8",
                                    "+9","+10"]
        
        skills_value_label = customtkinter.CTkLabel(master=self.frame_left, text="Skills Value Option")
        skills_value_label.grid(row=17,column=0)
        skills_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=skills_value_options_combobox)
        skills_value_combobox.grid(row=17, column=1)
        skills_value_combobox.set("Random")
        current_skills_value = skills_value_combobox.current_value
        #Create list of Skills
        skills_list = []    

        #Add Skills function
        def add_skills():
            #Type
            skills_choice = StringVar()
            skills_choice = skills_combobox.get()
            random_skills = random.choice(skills_options_label)
            #Value
            skills_value_choice = StringVar()
            skills_value_choice = skills_value_combobox.get()
            random_skills_value = random.choice(skills_value_options_label)
            
            if any(skills_choice in s for s in skills_list):
                tkinter.messagebox.showinfo('Error', f'{skills_choice} Skill already added.')
            else:                                    
                if skills_choice == "Random" and skills_value_choice == "Random":
                    skills_list.append(random_skills + ' ' + random_skills_value)
                    display_skills['text'] = ' | '.join(skills_list)
                                                
                elif skills_choice == "Random" and skills_value_choice != "Random":
                    skills_list.append(random_skills + ' ' + skills_value_choice)
                    display_skills['text'] = ' | '.join(skills_list)

                elif skills_choice !="Random" and skills_value_choice == "Random":
                    skills_list.append(skills_choice + ' ' + random_skills_value)
                    display_skills['text'] = ' | '.join(skills_list)

                elif skills_choice !="Random" and skills_value_choice != "Random":
                    skills_list.append(skills_choice + ' ' + skills_value_choice)
                    display_skills['text'] = ' | '.join(skills_list)
            
        #Display Skills
        display_skills = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_skills.grid(row=15,column=1)
        #Create button to add Skills
        add_skills_btn = customtkinter.CTkButton(master=self.frame_left, text="+",command=add_skills,width=30)
        add_skills_btn.grid(row=17, column=2,sticky="w")


        # ------------- Vulnerabilites ----------#
        #Vulnerabilites combobox
        vuln_label = customtkinter.CTkLabel(master=self.frame_left, text="Vulnerability Option")
        vuln_label.grid(row=18,column=0)
        vuln_options_combobox = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        vuln_options_label = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        vuln_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=vuln_options_combobox)
        vuln_combobox.grid(row=18, column=1)
        vuln_combobox.set("Random")
        current_vuln = vuln_combobox.current_value
        #Create Vuln list
        vuln_list = []
        #Add vuln Value function
        def add_vuln():
            vuln_choice = StringVar()
            vuln_choice = vuln_combobox.get()
            random_vuln = random.choice(vuln_options_label)
            if vuln_choice in vuln_list:
                tkinter.messagebox.showinfo('Error', f'{vuln_choice} Vulneability already added.')
            else:
                if vuln_choice == "Random":
                    vuln_list.append(random_vuln)
                    display_vuln['text'] = ' | '.join(vuln_list)
                else:
                    vuln_list.append(vuln_choice)
                    display_vuln['text'] = ' | '.join(vuln_list)
                
        #Display vuln Value
        display_vuln = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_vuln.grid(row=16,column=1)
        #Create button to add vuln Value
        add_vuln_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_vuln, width=30)
        add_vuln_btn.grid(row=18, column=2,sticky="w")
        

                            # ------------ Immunities ---------#
        #Immunities combobox
        immune_label = customtkinter.CTkLabel(master=self.frame_left, text="Immunity Option")
        immune_label.grid(row=19,column=0)
        immune_options_combobox = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        immune_options_label = ["Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        immune_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=immune_options_combobox)
        immune_combobox.grid(row=19, column=1)
        immune_combobox.set("Random")
        current_immune = immune_combobox.current_value
        #Add list of immunes
        immune_list = []
        #Add immune Value function
        def add_immune():
            immune_choice = StringVar()
            immune_choice = immune_combobox.get()
            random_immune = random.choice(immune_options_label)
            if immune_choice in immune_list:
                tkinter.messagebox.showinfo('Error', f'{immune_choice} Immunity already added.')
            else:
                if immune_choice == "Random":
                    immune_list.append(random_immune)
                    display_immune['text'] = ' | '.join(immune_list)
                else:
                    immune_list.append(immune_choice)
                    display_immune['text'] = ' | '.join(immune_list)
                
        #Display immune Value
        display_immune = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_immune.grid(row=17,column=1)
        #Create button to add immune Value
        add_immune_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_immune, width=30)
        add_immune_btn.grid(row=19, column=2,sticky="w")

        # ---------- Resistances -----------#
        #Resistances combobox
        resist_label = customtkinter.CTkLabel(master=self.frame_left, text="Resistance Option")
        resist_label.grid(row=20,column=0)
        resist_options_combobox = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        resist_options_label = ["Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        resist_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=resist_options_combobox)
        resist_combobox.grid(row=20, column=1)
        resist_combobox.set("Random")
        current_resist = resist_combobox.current_value
        #Resistance Add button
        resist_add_button = customtkinter.CTkButton(master=self.frame_left, text="+", width=30)
        resist_add_button.grid(row=20,column=2,sticky="w")
        #Create resist list
        resist_list = []
        #Add resist Value function
        def add_resist():
            resist_choice = StringVar()
            resist_choice = resist_combobox.get()
            random_resist = random.choice(resist_options_label)
            if resist_choice in resist_list:
                tkinter.messagebox.showinfo('Error', f'{resist_choice} Resistance already added.')
            else:
                if resist_choice == "Random":
                    resist_list.append(random_resist)
                    display_resist['text'] = ' | '.join(resist_list)
                else:
                    resist_list.append(resist_choice)
                    display_resist['text'] = ' | '.join(resist_list)
                
        #Display resist
        display_resist = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_resist.grid(row=18,column=1)
        #Create button to add resist
        add_resist_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_resist, width=30)
        add_resist_btn.grid(row=20, column=2,sticky="w")

        # -------- Senses ---------#
        #Sense combobox
        senses_label = customtkinter.CTkLabel(master=self.frame_left, text="Senses Option")
        senses_label.grid(row=21,column=0)
        senses_options_combobox = ["Random","Darkvision","Blindsight","Truesight","Tremorsense"]
        senses_options_label = ["Random","Darkvision","Blindsight","Truesight","Tremorsense"]
        senses_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=senses_options_combobox)
        senses_combobox.grid(row=21, column=1)
        senses_combobox.set("Random")
        current_sense = senses_combobox.current_value
        #Sense value combobox
        senses_value_options_combobox = ["Random",
                                "10 ft","20 ft","30 ft",
                                "40 ft","50 ft","60 ft",
                                "70 ft","80 ft","90 ft",
                                "100 ft","110 ft","120 ft"
                                ]
        senses_value_options_label = [
                                "10 ft","20 ft","30 ft",
                                "40 ft","50 ft","60 ft",
                                "70 ft","80 ft","90 ft",
                                "100 ft","110 ft","120 ft"
                                ]

        sense_value_label = customtkinter.CTkLabel(master=self.frame_left, text="Sense Value Option")
        sense_value_label.grid(row=22,column=0)
        senses_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=senses_value_options_combobox)
        senses_value_combobox.grid(row=22, column=1)
        senses_value_combobox.set("Random")
        current_sense_value = senses_value_combobox.current_value
        #Create list of senses
        senses_list = []    

        #Add senses function
        def add_senses():
            #Type
            senses_choice = StringVar()
            senses_choice = senses_combobox.get()
            random_senses = random.choice(senses_options_label)
            #Value
            senses_value_choice = StringVar()
            senses_value_choice = senses_value_combobox.get()
            random_senses_value = random.choice(senses_value_options_label)
            
            if any(senses_choice in s for s in senses_list):
                tkinter.messagebox.showinfo('Error', f'{senses_choice} Sense already added.')
            else:                                    
                if senses_choice == "Random" and senses_value_choice == "Random":
                    senses_list.append(random_senses + ' ' + random_senses_value)
                    display_senses['text'] = ' | '.join(senses_list)
                                                
                elif senses_choice == "Random" and senses_value_choice != "Random":
                    senses_list.append(random_senses + ' ' + senses_value_choice)
                    display_senses['text'] = ' | '.join(senses_list)

                elif senses_choice !="Random" and senses_value_choice == "Random":
                    senses_list.append(senses_choice + ' ' + random_senses_value)
                    display_senses['text'] = ' | '.join(senses_list)

                elif senses_choice !="Random" and senses_value_choice != "Random":
                    senses_list.append(senses_choice + ' ' + senses_value_choice)
                    display_senses['text'] = ' | '.join(senses_list)
            
        #Display senses
        display_senses = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_senses.grid(row=19,column=1)
        #Create button to add senses
        add_senses_btn = customtkinter.CTkButton(master=self.frame_left, text="+",command=add_senses,width=30)
        add_senses_btn.grid(row=22, column=2, sticky="w")

        #---------- Languages ----------#
        #Languages combobox
        lang_label = customtkinter.CTkLabel(master=self.frame_left, text="Languages Option")
        lang_label.grid(row=23,column=0)
        lang_options_combobox = ["Random","Common","Dwarvish",
                        "Elvish","Giant","Gnomish",
                        "Goblin","Halfling","Orc",
                        "Abyssal","Celestial","Deep Speech",
                        "Draconic","Infernal","Primordial",
                        "Sylvan","Undercommon"
                        ]
        lang_options_label = ["Random","Common","Dwarvish",
                        "Elvish","Giant","Gnomish",
                        "Goblin","Halfling","Orc",
                        "Abyssal","Celestial","Deep Speech",
                        "Draconic","Infernal","Primordial",
                        "Sylvan","Undercommon"
                        ]
        lang_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=lang_options_combobox)
        lang_combobox.grid(row=23, column=1)
        lang_combobox.set("Random")
        current_lang = lang_combobox.current_value
        #Language Add button
        # lang_add_button = customtkinter.CTkButton(master=self.frame_left, text="+", width=30)
        # lang_add_button.grid(row=23,column=2,sticky="w")
        #Create lang list
        lang_list = []
        #Add lang Value function
        def add_lang():
            lang_choice = StringVar()
            lang_choice = lang_combobox.get()
            random_lang = random.choice(lang_options_label)
            if lang_choice in lang_list:
                tkinter.messagebox.showinfo('Error', f'{lang_choice} Language already added.')
            else:
                if lang_choice == "Random":
                    lang_list.append(random_lang)
                    display_lang['text'] = ' | '.join(lang_list)
                else:
                    lang_list.append(lang_choice)
                    display_lang['text'] = ' | '.join(lang_list)
                
        #Display lang
        display_lang = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_lang.grid(row=20,column=1)
        #Create button to add lang
        add_lang_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_lang,width=30)
        add_lang_btn.grid(row=23, column=2,sticky="w")


        ###TODO
        #Special traits value combobox
        special_traits_label = customtkinter.CTkLabel(master=self.frame_left, text="Special Traits Option")
        special_traits_label.grid(row=24,column=0)
        special_traits_options = ["Random"]
        special_traits_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=special_traits_options)
        special_traits_combobox.grid(row=24, column=1)
        special_traits_combobox.set("Random")
        current_special_traits = special_traits_combobox.current_value
        #Language Add button
        special_traits_add_button = customtkinter.CTkButton(master=self.frame_left, text="+", width=30)
        special_traits_add_button.grid(row=24,column=2,sticky="w")

        ###TODO
        #lair Actions Options ~Temporary
        action_options_combobox = ["Random", "Bite", "Bite & Shake","Call / Howl","Claw","Death from Above",
                                    "Head Butt","Mule Kick","Pounce","Roll over","Stomp","Swallow Whole",
                                    "Tail Slap" ,"Tentacle","Trample","Weapon (Appendage / Natural Weapons)",
                                    "Weapon (Blood)","Weapon (Breath / Spit)","Weapon (External Glands Spray)",
                                    "Weapon (Gaze)","Weapon (Saliva)" ,"Weapon (Scream / Howl / Roar)",
                                    "Weapon (Touch)" ,"Weapon (Web Spinners)"]
        action_options_label = ["Bite", "Bite & Shake","Call / Howl","Claw","Death from Above",
                                    "Head Butt","Mule Kick","Pounce","Roll over","Stomp","Swallow Whole",
                                    "Tail Slap" ,"Tentacle","Trample","Weapon (Appendage / Natural Weapons)",
                                    "Weapon (Blood)","Weapon (Breath / Spit)","Weapon (External Glands Spray)",
                                    "Weapon (Gaze)","Weapon (Saliva)" ,"Weapon (Scream / Howl / Roar)",
                                    "Weapon (Touch)" ,"Weapon (Web Spinners)"]
        #Create action list
        action_list = []
        #Add action Value function
        def add_action():
            action_choice = StringVar()
            action_choice = action_combobox.get()
            random_action = random.choice(action_options_label)
            if action_choice in action_list:
                tkinter.messagebox.showinfo('Error', f'{action_choice} Action already added.')
            else:
                if action_choice == "Random":
                    action_list.append(random_action)
                    display_action['text'] = ' | '.join(action_list)
                else:
                    action_list.append(action_choice)
                    display_action['text'] = ' | '.join(action_list)
            
                
        #Display action
        display_action = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_action.grid(row=22,column=1)
        #Create button to add action
        add_action_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_action, width=30)
        add_action_btn.grid(row=25, column=2,sticky="w")
        #lair Actions value combobox
        action_label = customtkinter.CTkLabel(master=self.frame_left, text="Actions Option")
        action_label.grid(row=25,column=0)
        
        action_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=action_options_combobox)
        action_combobox.grid(row=25, column=1)
        action_combobox.set("Random")
        

        ###TODO
        #Legendary Actions Options ~Temporary
        legendary_action_options_combobox = ["Random", "Difficult Terrain", "Obscure Sight",
                                            "Snaring", "Knockdown", "Lighting Change", 
                                            "Heal Dampening", "Spell Dampening", "Effect on Enter",
                                            "Effect on Exit", "Free Action", "Free Reaction",
                                            "Free Spell", "Free Ability"]
        legendary_action_options_label = ["Difficult Terrain", "Obscure Sight",
                                            "Snaring", "Knockdown", "Lighting Change", 
                                            "Heal Dampening", "Spell Dampening", "Effect on Enter",
                                            "Effect on Exit", "Free Action", "Free Reaction",
                                            "Free Spell", "Free Ability"]
         #Create legendary_action list
        legendary_action_list = []
        #Add legendary_action Value function
        def add_legendary_action():
            legendary_action_choice = StringVar()
            legendary_action_choice = legendary_action_combobox.get()
            random_legendary_action = random.choice(legendary_action_options_label)
            if legendary_action_choice in legendary_action_list:
                tkinter.messagebox.showinfo('Error', f'{legendary_action_choice} Legendary Action already added.')
            else:
                if legendary_action_choice == "Random":
                    legendary_action_list.append(random_legendary_action)
                    display_legendary_action['text'] = ' | '.join(legendary_action_list)
                else:
                    legendary_action_list.append(legendary_action_choice)
                    display_legendary_action['text'] = ' | '.join(legendary_action_list)
            
                
        #Display legendary_action
        display_legendary_action = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_legendary_action.grid(row=23,column=1)
        #Create button to add legendary_action
        add_legendary_action_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_legendary_action, width=30)
        add_legendary_action_btn.grid(row=26, column=2,sticky="w")
        #Legendary Actions value combobox
        legendary_action_label = customtkinter.CTkLabel(master=self.frame_left, text="Legendary Actions Option")
        legendary_action_label.grid(row=26,column=0)
        
        legendary_action_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=legendary_action_options_combobox)
        legendary_action_combobox.grid(row=26, column=1)
        legendary_action_combobox.set("Random")
    
        ###TODO
        #Lair Actions Options ~Temporary
        lair_action_options_combobox = ["Random", "Difficult Terrain", "Obscure Sight",
                                            "Snaring", "Knockdown", "Lighting Change", 
                                            "Heal Dampening", "Spell Dampening", "Effect on Enter",
                                            "Effect on Exit", "Free Action", "Free Reaction",
                                            "Free Spell", "Free Ability"]
        lair_action_options_label = ["Difficult Terrain", "Obscure Sight",
                                            "Snaring", "Knockdown", "Lighting Change", 
                                            "Heal Dampening", "Spell Dampening", "Effect on Enter",
                                            "Effect on Exit", "Free Action", "Free Reaction",
                                            "Free Spell", "Free Ability"]
        #Create Lair Action list
        lair_action_list = []
        #Add Lair Action Value function
        def add_lair_action():
            lair_action_choice = StringVar()
            lair_action_choice = lair_action_combobox.get()
            random_lair_action = random.choice(lair_action_options_label)
            if lair_action_choice in lair_action_list:
                tkinter.messagebox.showinfo('Error', f'{lair_action_choice} lair Action already added.')
            else:
                if lair_action_choice == "Random":
                    lair_action_list.append(random_lair_action)
                    display_lair_action['text'] = ' | '.join(lair_action_list)
                else:
                    lair_action_list.append(lair_action_choice)
                    display_lair_action['text'] = ' | '.join(lair_action_list)
            
                
        #Display Lair Action
        display_lair_action = customtkinter.CTkLabel(master=self.frame_right, text='')
        display_lair_action.grid(row=24,column=1)
        #Create button to add Lair Action
        add_lair_action_btn = customtkinter.CTkButton(master=self.frame_left, text="+", command=add_lair_action, width=30)
        add_lair_action_btn.grid(row=27, column=2,sticky="w")
        #Lair Actions value combobox
        lair_action_label = customtkinter.CTkLabel(master=self.frame_left, text="Lair Actions Option")
        lair_action_label.grid(row=27,column=0)
        
        lair_action_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=lair_action_options_combobox)
        lair_action_combobox.grid(row=27, column=1)
        lair_action_combobox.set("Random")
        

        ###TODO
        #Spells value combobox
        # spells_label = customtkinter.CTkLabel(master=self.frame_left, text="Spells Option")
        # spells_label.grid(row=25,column=0)

        # #Create lists of spells from spells.py
        # df_spells_0 = pd.read_excel("data/level_0_spells.xlsx")
        # list_spells_0 = df_spells_0["Name"].values.tolist()

        # df_spells_1 = pd.read_excel("data/level_1_spells.xlsx")
        # list_spells_1 = df_spells_1["Name"].values.tolist()

        # df_spells_2 = pd.read_excel("data/level_2_spells.xlsx")
        # list_spells_2 = df_spells_2["Name"].values.tolist()

        # df_spells_3 = pd.read_excel("data/level_3_spells.xlsx")
        # list_spells_3 = df_spells_3["Name"].values.tolist()

        # df_spells_4 = pd.read_excel("data/level_4_spells.xlsx")
        # list_spells_4 = df_spells_4["Name"].values.tolist()

        # df_spells_5 = pd.read_excel("data/level_5_spells.xlsx")
        # list_spells_5 = df_spells_5["Name"].values.tolist()

        # df_spells_6 = pd.read_excel("data/level_6_spells.xlsx")
        # list_spells_6 = df_spells_6["Name"].values.tolist()

        # df_spells_7 = pd.read_excel("data/level_7_spells.xlsx")
        # list_spells_7 = df_spells_7["Name"].values.tolist()

        # df_spells_8 = pd.read_excel("data/level_8_spells.xlsx")
        # list_spells_8 = df_spells_8["Name"].values.tolist()

        # df_spells_9 = pd.read_excel("data/level_9_spells.xlsx")
        # list_spells_9 = df_spells_9["Name"].values.tolist()

        # #List out All Spells for all Levels
        # spells_level_options_combobox = {"Random": "Random",
        #                             "Level 0": list_spells_0,
        #                             "Level 1": list_spells_1,
        #                             "Level 2": list_spells_2,
        #                             "Level 3": list_spells_3,
        #                             "Level 4": list_spells_4,
        #                             "Level 5": list_spells_5,
        #                             "Level 6": list_spells_6,
        #                             "Level 7": list_spells_7,
        #                             "Level 8": list_spells_8,
        #                             "Level 9": list_spells_9,}
        # spells_level_options_label = ["Level 0","Level 1",
        #                                 "Level 2","Level 3","Level 4",
        #                                 "Level 5","Level 6","Level 7",
        #                                 "Level 8","Level 9"]
            
        
        # def on_spell_selected(spell_value):
        #     spell_values = ('Random')
        #     if spell_value == "Random":
        #         for v in spells_level_options_combobox.values():
        #             spell_values += v
        #     else:
        #         spell_values += spells_level_options_combobox[spell_value]
        #     spells_level_combobox.configure(values=spell_values)
        #     spells_level_combobox.set('Random')

        # spells_var1 = customtkinter.StringVar()
        # spells_level_combobox = customtkinter.CTkComboBox(master=self.frame_left, 
        #                                                 variable=spells_var1, 
        #                                                 values=("Random",)+tuple(spells_level_options_combobox.keys()), 
        #                                                 command=on_spell_selected)
        # spells_level_combobox.grid(row=25,column=1)
        # spells_level_combobox.set("Random")

        # spells_var2 = customtkinter.StringVar()
        # spells_combobox = customtkinter.CTkComboBox(master=self.frame_left, 
        #                                             variable=spells_var2, 
        #                                             values=("Random",)+tuple(spells_level_options_combobox.keys()), 
        #                                             command=on_spell_selected) 
        # spells_combobox.grid(row=25, column=2)
        # spells_combobox.set("Random")
        
        # #Create list of spells
        # spells_list = []    

        # #Add spells function
        # def add_spells():
        #     #Level
        #     spells_level_choice = StringVar()
        #     spells_level_choice = spells_level_combobox.get()
        #     random_spells_level = random.choice(spells_level_options_label)
        #     #Value
        #     spells_choice = StringVar()
        #     spells_choice = spells_combobox.get()
        #     random_spells_value = random.choice(spells_options_label)
            
        #     if any(spells_choice in s for s in spells_list):
        #         tkinter.messagebox.showinfo('Error', f'{spells_choice} Sense already added.')
        #     else:                                    
        #         if spells_choice == "Random" and spells_level_choice == "Random":
        #             spells_list.append(random_spells_level + ' ' + random_spells_value)
        #             display_spells['text'] = ' | '.join(spells_list)
                                                
        #         elif spells_choice == "Random" and spells_level_choice != "Random":
        #             spells_list.append(random_spells_level + ' ' + spells_level_choice)
        #             display_spells['text'] = ' | '.join(spells_list)

        #         elif spells_choice !="Random" and spells_level_choice == "Random":
        #             spells_list.append(spells_choice + ' ' + random_spells_value)
        #             display_spells['text'] = ' | '.join(spells_list)

        #         elif spells_choice !="Random" and spells_level_choice != "Random":
        #             spells_list.append(spells_choice + ' ' + spells_level_choice)
        #             display_spells['text'] = ' | '.join(spells_list)
            
        # #Display spells
        # display_spells = customtkinter.CTkLabel(master=self.frame_right, text='')
        # display_spells.grid(row=25,column=1)
        # #Create button to add spells
        # add_spells_btn = customtkinter.CTkButton(master=self.frame_left, text="Add Spells",command=add_spells)
        # add_spells_btn.grid(row=25, column=3)

        #TODO Export to PDF 
        #------ Display Stats ----#
        
        for index, row in enumerate(self.monster_stat_list): 
            monster_stats_label = customtkinter.CTkLabel(master=self.frame_right, 
                                                        text=row + ":")
                                                        
            #may want to add index + 1 to start it on row 2 
            monster_stats_label.grid(row=index, column=0,padx=1,pady=1, sticky="w")

        #TODO
        #------Remove Button------#
        # def remove_stat():
        #     #Create Window
        #     remove_stat_window = customtkinter.CTkToplevel(master)
        
        #     # sets the title of the
        #     # Toplevel widget
        #     remove_stat_window.title("Remove Stat")
        
        #     # sets the geometry of toplevel
        #     remove_stat_window.geometry("400x400")
        
        #     # A Label widget to show in toplevel
        #     customtkinter.CTkLabel(remove_stat_window, text="Choose Stat to Clear")
        #     customtkinter.CTkComboBox(remove_stat_window,
        #         text ="Choose Stat to Clear").pack()

        # remove_btn = customtkinter.CTkButton(master=self.frame_left, text="Remove Stat?", command=remove_stat)
        # remove_btn.grid(row=28,column=0, columnspan=4)

        #TODO
        #------------Save Monster------------#
        # def save_monster():
        #     file = open("monster.txt", "w")
        #     file.write("Monster Name: " + monster_name + 
        #                 "\n" + "Size: "+ display_size.cget("Text"))
        #     file.close 
        # save_btn = customtkinter.CTkButton(master=self.frame_left,text="Save to File", command=save_monster)
        # save_btn.grid(row=29,column=0, columnspan=4)
              


if __name__ == "__main__":
    app = App()
    app.mainloop()