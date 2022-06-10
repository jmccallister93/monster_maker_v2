from doctest import master
import string
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import *

#TODO Create IF statement for Saves based on stats
#TODO Create healthpool options

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

    WIDTH = 1450
    HEIGHT = 900
    monster_stat_list = [
                            "Name",
                            "Size",
                            "Type",
                            "AC",
                            "HP",
                            "Speed",
                            "STR",
                            "DEX",
                            "CON",
                            "INT",
                            "WIS",
                            "CHA",
                            "Saves",
                            "Skills",
                            "Senses",
                            "Languages",
                            "Abilites",
                            "actions",
                            "Spells"
                        ]

    def __init__(self):
        super().__init__()

        self.title("Monster Maker")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        #------------Setup Frame---------------#
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

        #Size Combobox
        size_label = customtkinter.CTkLabel(master=self.frame_left, text="Size Option")
        size_label.grid(row=1,column=0)
        size_options = ["Random", "Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
        size_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=size_options)
        size_combobox.grid(row=1, column=1)
        size_combobox.set("Random")
        current_size = size_combobox.current_value

        #Monster type Combobox
        type_label = customtkinter.CTkLabel(master=self.frame_left, text="Monster Type Option")
        type_label.grid(row=2,column=0)
        type_options = ["Random","Aberration", "Beast", 
                        "Celestial", "Construct", "Dragon", 
                        "Elemental", "Fey", "Fiend", 
                        "Giant", "Humanoid", "Monstrosity", 
                        "Ooze", "Plant", "Undead"
                        ]
        type_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=type_options)
        type_combobox.grid(row=2, column=1)
        type_combobox.set("Random")
        current_type = type_combobox.current_value

        # ---------------- AC Options --------------#
        #AC type Combobox
        ac_type_label = customtkinter.CTkLabel(master=self.frame_left, text="AC Type Option")
        ac_type_label.grid(row=3,column=0)
        ac_type_options = ["Random", "Ancestral", "Magic", "Natural", "Worn"]
        ac_type_combobox = customtkinter.CTkComboBox(master=self.frame_left, values= ac_type_options)
        ac_type_combobox.grid(row=3, column=1)
        ac_type_combobox.set("Random")
        current_ac_type = ac_type_combobox.current_value
        
        #AC Value Combobox
        ac_label = customtkinter.CTkLabel(master=self.frame_left, text="AC Value Option")
        ac_label.grid(row=4,column=0)
        ac_options = ["Random",
                    "7","8","9","10",
                    "11","12","13","14",
                    "15","16","17","18",
                    "19","20","21","22",
                    "23","24","25","26",
        ]
        ac_combobox = customtkinter.CTkComboBox(master=self.frame_left, values= ac_options)
        ac_combobox.grid(row=4, column=1)
        ac_combobox.set("Random")
        current_ac = ac_combobox.current_value

        # ---------------- HP Pool Option --------------#
        hp_options = {"Low" : (
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
                for v in hp_options.values():
                    hp_values += v
            else:
                hp_values += hp_options[hp_value]
            hp_value_combobox.configure(values=hp_values)
            hp_value_combobox.set('Random')


        #Label
        hp_pool_label = customtkinter.CTkLabel(master=self.frame_left, text="HP Option")
        hp_pool_label.grid(row=5,column=0)
        hp_var1 = customtkinter.StringVar()
        hp_pool_combobox = customtkinter.CTkComboBox(master=self.frame_left, 
                                        variable=hp_var1, 
                                        values=("Random",)+tuple(hp_options.keys()), 
                                        command=on_pool_selected)
        hp_pool_combobox.grid(row=5, column=1)
        

        hp_var2 = customtkinter.StringVar()
        hp_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, variable=hp_var2)
        hp_value_combobox.grid(row=5, column=2)
        hp_value_combobox.set("Random")
        hp_pool_combobox.set("Random")
        
        # ----------Movement Options ------------#
        # Base Movement Speed Combobox
        move_speed_label = customtkinter.CTkLabel(master=self.frame_left, text="Base Move Speed Option")
        move_speed_label.grid(row=6,column=0)
        move_speed_options = ["Random", 
                            "10 ft","20 ft","30 ft",
                            "40 ft","50 ft","60 ft",
                            "70 ft","80 ft","90 ft",
                            "100 ft","110 ft","120 ft"
                            ]
        move_speed_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=move_speed_options)
        move_speed_combobox.grid(row=6, column=1)
        move_speed_combobox.set("Random")
        current_move_speed = move_speed_combobox.current_value

        #Extra Movement Type Combobox
        move_type_label = customtkinter.CTkLabel(master=self.frame_left, text="Extra Move Type Option")
        move_type_label.grid(row=7,column=0)
        move_type_options = ["Random", "Burrow", "Climb", "Fly", "Swim"]
        move_type_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=move_type_options)
        move_type_combobox.grid(row=7, column=1)
        move_type_combobox.set("Random")
        current_move_type = move_type_combobox.current_value

        #Extra Speed
        extra_speed_options = ["Random", 
                            "10 ft","20 ft","30 ft",
                            "40 ft","50 ft","60 ft",
                            "70 ft","80 ft","90 ft",
                            "100 ft","110 ft","120 ft"
                            ]
        extra_speed_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=extra_speed_options)
        extra_speed_combobox.grid(row=7, column=2)
        extra_speed_combobox.set("Random")
        current_extra_speed = extra_speed_combobox.current_value
        #Extra Move Add button
        resist_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Move Type")
        resist_add_button.grid(row=7,column=3)

        # ---------- Monster Stats --------- #
        #Stats
        stats_options = [
            "Random",
            "1","5","6","7","8",
            "9","10","11","12","13",
            "14","15","16","17","18",
            "19","20","21","22","23",
            "24","25","26","27","28",
            "29","30",
        ]

        #STR Combobox
        str_label = customtkinter.CTkLabel(master=self.frame_left, text="STR Option")
        str_label.grid(row=9,column=0)
        str_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options)
        str_combobox.grid(row=9, column=1)
        str_combobox.set("Random")
        current_str = str_combobox.current_value

        #DEX Combobox
        dex_label = customtkinter.CTkLabel(master=self.frame_left, text="DEX Option")
        dex_label.grid(row=10,column=0)
        dex_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options)
        dex_combobox.grid(row=10, column=1)
        dex_combobox.set("Random")
        current_dex = dex_combobox.current_value

        #CON Combobox
        con_label = customtkinter.CTkLabel(master=self.frame_left, text="CON Option")
        con_label.grid(row=11,column=0)
        con_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options)
        con_combobox.grid(row=11, column=1)
        con_combobox.set("Random")
        current_con = con_combobox.current_value

        #INT Combobox
        int_label = customtkinter.CTkLabel(master=self.frame_left, text="INT Option")
        int_label.grid(row=12,column=0)
        int_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options)
        int_combobox.grid(row=12, column=1)
        int_combobox.set("Random")
        current_int = int_combobox.current_value

        #WIS Combobox
        wis_label = customtkinter.CTkLabel(master=self.frame_left, text="WIS Option")
        wis_label.grid(row=13,column=0)
        wis_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options)
        wis_combobox.grid(row=13, column=1)
        wis_combobox.set("Random")
        current_wis = wis_combobox.current_value

        #CHA Combobox
        cha_label = customtkinter.CTkLabel(master=self.frame_left, text="CHA Option")
        cha_label.grid(row=14,column=0)
        cha_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=stats_options)
        cha_combobox.grid(row=14, column=1)
        cha_combobox.set("Random")
        current_cha = cha_combobox.current_value

        #--------- Saving Throws ---------#
        #TODO Create IF statement for Saves based on stats
        
        # ----------- Skills ------------#
        #Skills combobox
        skills_label = customtkinter.CTkLabel(master=self.frame_left, text="Skills Option")
        skills_label.grid(row=15,column=0)
        skills_options = ["Random","Acrobatics","Animal Handling",
                        "Arcana","Athletics","Deception",
                        "History","Insight","Intimidation",
                        "Investigation","Medicine","Nature",
                        "Perception","Performance","Persuasion",
                        "Religion","Sleight of Hand","Stealth",
                        "Survival",
                        ]
        skills_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=skills_options)
        skills_combobox.grid(row=15, column=1)
        skills_combobox.set("Random")
        current_skills = skills_combobox.current_value
        #Skills value combobox
        skills_value_options = ["Random","+1","+2","+3",
                                "+4","+5","+6","+7","+8",
                                "+9","+10"]
        skills_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=skills_value_options)
        skills_value_combobox.grid(row=15, column=2)
        skills_value_combobox.set("Random")
        current_skills_value = skills_value_combobox.current_value
        #Skills Add button
        skills_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Skill")
        skills_add_button.grid(row=15,column=3)
        
        # ------------- Vulnerabilites ----------#
        #Vulnerabilites combobox
        vuln_label = customtkinter.CTkLabel(master=self.frame_left, text="Vulnerability Option")
        vuln_label.grid(row=16,column=0)
        vuln_options = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        vuln_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=vuln_options)
        vuln_combobox.grid(row=16, column=1)
        vuln_combobox.set("Random")
        current_vuln = vuln_combobox.current_value
        #Vuln Add button
        vuln_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Vulnerability")
        vuln_add_button.grid(row=16,column=2)

        # ------------ Immunities ---------#
        #Immunities combobox
        immune_label = customtkinter.CTkLabel(master=self.frame_left, text="Immunity Option")
        immune_label.grid(row=17,column=0)
        immune_options = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        immune_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=immune_options)
        immune_combobox.grid(row=17, column=1)
        immune_combobox.set("Random")
        current_immune = immune_combobox.current_value
        #Immune Add button
        immune_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Immunity")
        immune_add_button.grid(row=17,column=2)

        # ---------- Resistances -----------#
        #Resistances combobox
        resist_label = customtkinter.CTkLabel(master=self.frame_left, text="Resistance Option")
        resist_label.grid(row=18,column=0)
        resist_options = ["Random","Acid","Cold","Fire",
                        "Force","Lightning","Necrotic",
                        "Poison","Psychic","Radiant",
                        "Thunder","Bludgeoning","Slashing",
                        "Piercing","Magical","Magical Bludgeoning",
                        "Magical Slashing","Magical Piercing",
                        ]
        resist_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=resist_options)
        resist_combobox.grid(row=18, column=1)
        resist_combobox.set("Random")
        current_resist = resist_combobox.current_value
        #Resistance Add button
        resist_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Resistance")
        resist_add_button.grid(row=18,column=2)

        # -------- Senses ---------#
        #Sense combobox
        senses_label = customtkinter.CTkLabel(master=self.frame_left, text="Senses Option")
        senses_label.grid(row=19,column=0)
        senses_options = ["Random","Darkvision","Blindsight","Truesight","Tremorsense"]
        senses_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=senses_options)
        senses_combobox.grid(row=19, column=1)
        senses_combobox.set("Random")
        current_sense = senses_combobox.current_value
        #Sense value combobox
        senses_value_options = ["Random",
                                "10 ft","20 ft","30 ft",
                                "40 ft","50 ft","60 ft",
                                "70 ft","80 ft","90 ft",
                                "100 ft","110 ft","120 ft"
                                ]
        senses_value_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=senses_value_options)
        senses_value_combobox.grid(row=19, column=2)
        senses_value_combobox.set("Random")
        current_sense_value = senses_value_combobox.current_value
        #senses Add button
        senses_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Sense")
        senses_add_button.grid(row=19,column=3)

        #---------- Languages ----------#
        #Languages combobox
        lang_label = customtkinter.CTkLabel(master=self.frame_left, text="Languages Option")
        lang_label.grid(row=20,column=0)
        lang_options = ["Random","Common","Dwarvish",
                        "Elvish","Giant","Gnomish",
                        "Goblin","Halfling","Orc",
                        "Abyssal","Celestial","Deep Speech",
                        "Draconic","Infernal","Primordial",
                        "Sylvan","Undercommon"
                        ]
        lang_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=lang_options)
        lang_combobox.grid(row=20, column=1)
        lang_combobox.set("Random")
        current_lang = lang_combobox.current_value
        #Language Add button
        lang_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Language")
        lang_add_button.grid(row=20,column=2)

        ###TODO
        #Abilites value combobox
        abilities_label = customtkinter.CTkLabel(master=self.frame_left, text="Abilities Option")
        abilities_label.grid(row=21,column=0)
        abilities_options = ["Random"]
        abilities_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=abilities_options)
        abilities_combobox.grid(row=21, column=1)
        abilities_combobox.set("Random")
        current_abilities = abilities_combobox.current_value
        #Language Add button
        abilities_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Abilities")
        abilities_add_button.grid(row=21,column=2)

        ###TODO
        #Actions value combobox
        actions_label = customtkinter.CTkLabel(master=self.frame_left, text="Actions Option")
        actions_label.grid(row=22,column=0)
        actions_options = ["Random"]
        actions_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=actions_options)
        actions_combobox.grid(row=22, column=1)
        actions_combobox.set("Random")
        current_actions = actions_combobox.current_value
        #Actions Add button
        actions_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Actions")
        actions_add_button.grid(row=22,column=2)

        ###TODO
        #Spells value combobox
        spells_label = customtkinter.CTkLabel(master=self.frame_left, text="Spells Option")
        spells_label.grid(row=23,column=0)
        spells_options = ["Random"]
        spells_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=spells_options)
        spells_combobox.grid(row=23, column=1)
        spells_combobox.set("Random")
        current_spells = spells_combobox.current_value
        #Spell Add button
        spell_add_button = customtkinter.CTkButton(master=self.frame_left, text="Add Spell")
        spell_add_button.grid(row=23,column=2)

if __name__ == "__main__":
    app = App()
    app.mainloop()