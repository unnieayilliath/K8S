########################################
#     This is the file 'main.py'   #
# This is the main file for the tool. This class needs to run first
########################################

from consolehelper import ConsoleHelper
from k8scontroller import K8SController
from navigationcontroller import NavigationController

class Main():
    _isRunning = True
    def __init__(self):
        # Trigger the startup process which loads the navigation.
        self._navCtrl = NavigationController()
        self._k8sCtrl= K8SController()
    # -------------------------------------------------------------------------------
    # Show the navigation menu

    def load_navigation(self):
        # Once startup process is completed show the menu and get user action
        return self._navCtrl.display_menu()
    # -------------------------------------------------------------------------------
    # Open the screen corresponding to the menu selection
    def load_screen(self,selectedNav):
        if selectedNav["id"] ==100:
                self._k8sCtrl.load_screen()
        elif selectedNav["id"] ==200:
            self._k8sCtrl.run_predefined_scenario()
        else:
                # exit the application
                confirm = ConsoleHelper.get_yes_no_input(
                    "Are you sure to quit? (Y/N) \t")
                if confirm:
                    self.stop()
    # -------------------------------------------------------------------------------
    # This is the main method which gets run when the app is started
    def start(self):
        while self._isRunning:
            selectedNav = self.load_navigation()
            if selectedNav is not None:
              # if no menu selected , that means user pressed back button '0'
                app.load_screen(selectedNav)
    # -------------------------------------------------------------------------------
    # Stop the application

    def stop(self):
        self._isRunning = False
        print("The application is now stopped!")
app = Main()
app.start()
