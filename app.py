
import streamlit as st




st.set_page_config(page_title="Hassna's Curriculum", page_icon=":briefcase:", layout="wide")





  #-----PRESENTATION-----
with st.container():
    st.subheader("Hi, I am HASSNA HAGAG ")
    st.title(":earth_africa: A Business Student :chart_with_upwards_trend: "
             )
    st.write(
        "Etudiante issue d'une grande ecole de business (ESMS BUSINESS SCHOOL), cherchant a approfondir ses connaissances sur le monde des Entreprises ." )
    st.write(":round_pushpin: Agadir") 
    
    # ------CERTIFICATS ET ACTIVITES -----
with st.container():
    st.write("----")
    left_column , right_column = st.columns(2)
    with left_column:
            st.header("	:female-student: Formations et Education :mortar_board:")
            st.write("##")
            st.write(
                 """ 
                 - 	:scroll: LICENCE EN MANAGEMENT DES ENTREPRISES (2019-2022)
                         * Ecole Supérieure de Management du Sud . [ESMS]
                 - 	:scroll: DEUG EN SCIENCES D'ECONOMIE ET GESTION (2019-2022)
                         * Faculté des Sciences Juridiques , Economiques et Sociales d'Agadir. [FSJES]
                 - 	:scroll: BACCALAUREAT (2018-2019)
                         * Institution Al Imam Al Kastalani Privée . [IIK]

                    """
        )

    with right_column:
        st.header(" :clap: Certificats et activités")
        st.write("##")
        st.write(
            """
            - :medal: Participation à la célébration de la journée de la femme 8 MARS à l'ESMS .
            
            - :medal: Certificat de participation à un événement professionnel sous le thème :"Marchés financiers : Fonctionnement et rôles"
            
            - :medal: Certificat de participation à l'installation des panneaux solaires à DAR TALIB quartier NAHDA dans le cadre d'un partenariat entre "l'INSTITUTION AL IMAM AL KASTALANI PRIVEE" à AGADIR  et "LYCEE CHERIOUX VITRY-SUR-SEINE" à PARIS
            
            """
        )

         #-----Compétences-------

with st.container():
    st.subheader(" :muscle: Compétences : ")
    st.write("##")
    st.write(
        """ 
        - Marketing
        - Management
        - Finance
        - Décision d’investissement
        - Gestion des Ressources Humaines 
        - Control de Gestion 
        - Comptabilité 
        - Comptabilité Analytique
        - Estimation 
        - Echantillonnage
        - Data Structure
        - Programmation
        - VBA
        - SQL
        - HTML
        - CSS
       
        """
        )




with st.container():
     st.subheader("	:confetti_ball: Loisirs ")
     st.write("##")
     st.write(
        """
        - Vintage
        - Papercraft
        - Dentelle
        - Illustration
        - Art Plastique
        - Jardinage
        - Fabrication d'accessoires
        - Broderie
        - Broderie à la machine
        - Composition florale
        - Musique
        - Photographie
        - Photographie des paysages
        - Vannerie
        - Peinture
        - Peinture à l'huile
        - Cuisine
        - Nail art
        - Collection de disques et de vinyles
        - Dessins vivant
        - Activités manuelles
        """)



        # -----Contacts-----
with st.container():
    st.subheader(" ")
    st.title(":link: Conatctez-moi sur : ")
    st.write(":iphone: téléphone : 07 06 58 73 84")
    st.write(":email: e-mail : hassna.hagag@gmail.com")
    st.write(":camera: Instagram : hassna_ha47")
    st.write(":large_blue_square: Facebook : Hassna Ha")
