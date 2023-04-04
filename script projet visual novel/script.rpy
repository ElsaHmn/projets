
define ga = Character("Ganyu")
define mo = Character("Mona Megistus")
define ch = Character("Tartaglia")
define hu = Character("Hu Tao")
define ni = Character("Ningguang")
define ve = Character("Venti")
define be = Character("Bennett")
define yo = Character("Naganohara Yoimiya")
define it = Character("Arataki Itto")
define sc = Character("Scaramouche")
define ka = Character("Kaeya Alberich")
define ba = Character("Barbara Pegg")
define al = Character("Albedo Kreideprinz")
define sa = Character("Sayu")
define pa = Character("Paimon")

label start:

    label preintro:

        scene bg room
        hide bg room

        show eileen happy
        hide eileen happy

        # These display lines of dialogue.

        ve "c'est juste pour me souvenir"

        "Welcome to Danganronpa : Impacting Despair"
        "Few informations before starting your experience :"
        "1 - This is an unofficial fangame, i do not own Genshin Impact nor Danganronpa, all rights reserved to, respectivly, Hoyoverse and Spike Chunsoft."
        "2 - English isn't my first language, so even if i've spend lots of time re-reading and correcting text, it is possible that i've mad mistake, for which i'm sorry."
        "3 - The design of the character present in this game has been reworked for the purpose of a more coherent *school life* alternate universe."
        "Even if you may not like it, i've spent quite some time doing them, so at least be respectful of my work."
        "With that say, you can start this game."

    label character_choice:

        "First of all, would you like to play as a girl or as a boy ?"

        menu:
            "A Girl":
                jump ch_girl

            "A Boy":
                jump ch_boy

        label ch_girl:
            define Player = Character("Lumine")
            define Evil = Character("Aether")
            image main blank = "lumain/lmain_blank.png"

            "So you want to play as Lumine ?"

            menu:
                "Yes":
                    jump ch1_done

                "No":
                    hide main blank
                    jump character_choice

        label ch_boy:
            define Player = Character("Aether")
            define Evil = Character("Lumine")
            image main blank = "aemain/amain_blank.png"
            show main blank at right

            "So you want to play as Aether ?"

            menu:
                "Yes":
                    jump ch1_done

                "No":
                    hide main blank
                    jump character_choice

    label ch1_done:

        "ok"

    return
