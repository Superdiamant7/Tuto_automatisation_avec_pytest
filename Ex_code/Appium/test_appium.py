# Importation des bibliothèques nécessaires
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Configuration du test
def setup_driver():
    # Paramètres (vous retrouvez le package et l'activité donc adaptez-les comme vous l'aviez fait avant dans l'inspecteur)
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Device"
    options.app_package = "com.sec.android.app.popupcalculator"
    options.app_activity = "com.sec.android.app.popupcalculator.Calculator"
    options.no_reset = True

    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver

# Définition du test
def test_addition():
    # Initialisation du test
    driver = setup_driver()

    # Try = essayer un bout de code
    try:
        # Pour désigner un élément on part toujours de "driver", expliquant le code "driver"
        # Trouver l'élément de driver avec le XPATH puis cliquer dessus
        # Bouton "2"
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="2"]').click()
        # Bouton "+"
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Plus"]').click()
        # Bouton "3"
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="3"]').click()
        # Bouton "="
        driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Calcul"]').click()

        # Attendre 1 seconde pour être sûr que le résultat a eu le temps de s'afficher afin de ne pas provoquer une erreur pour rien (nécessite d'importer "time")
        time.sleep(1)

        # Trouver l'élément de driver avec le XPATH correspondant à l'affichage du résultat
        result_element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]')
        # Récupérer le texte de l'élément
        result = result_element.text.strip()
    
        # Vérifier si 5 est affiché dans l'élément
        assert "5" in result
        # Afficher "Test réussi !" (Si la ligne au dessus provoque une erreur, le test se terminera avec une erreur et le texte ne sera pas affiché)
        print("Test réussi !")
    
    # Finlly permet d'éxécuter du code après le "try"
    finally:
        # Mettre fin au test
        driver.quit()