from consolehelper import ConsoleHelper
from navigationcontroller import NavigationController
import os
 # -------------------------------------------------------------------------------------------------
 # A class for controlling interactions with the K8S
class K8SController:
   
    # --------------------------------------------------------------------------------------------------
    # This is the main method for this controller
    def load_screen(self):
        loop=True
        while loop:
            ConsoleHelper.clear()
            self.__list_pods()
            loop=self.__perform_action()
    # -------------------------------------------------------------------------------------------------
    # This protected method returns all containers
    def __list_pods(self):
       os.system("kubectl get pods -o wide")
    # ------------------------------------------------------------------------------------------------
    # This method allows user to select an action
    def __perform_action(self):
        repeat = True
        # show all actions for this menu
        selectedAction = NavigationController.print_actions()
        if selectedAction is None:
            repeat=False
        else:
            # add the page to the breadcrumb
            ConsoleHelper.append_breadcrumb(selectedAction["name"])
        try:
            if selectedAction["key"]=="describe":
                    self.__describe_pod()
            elif selectedAction["key"]== "create":
                    self.__create_deployment()
            elif selectedAction["key"]== "update":
                    self.__update_deployment()
            elif selectedAction["key"]== "deploy":
                    self.__deploy_ubuntu()
            else:
                    self.__delete_deployment()
        except Exception as ex:
            ConsoleHelper.print_error(ex)
            print("Something went wrong! Please check error details above")
        if repeat:
            input("Press any key to continue..")
            # remove the last added item from breadcrumb
            ConsoleHelper.pop_breadcrumb()
        return repeat
    # ------------------------------------------------------------------------------------------------------------
    # This method describes a pod
    def __describe_pod(self):
        podName=ConsoleHelper.get_alphanumeric_input("Please enter the pod name:\t")
        os.system(f"kubectl describe pod {podName}")
    # ------------------------------------------------------------------------------------------------------------
    # This method creates a deployment with 2 pods.
    def __create_deployment(self):
        image=ConsoleHelper.get_number_input(1,2,"Please select image,\n 1. nginx:1.20\t2. couchbase:6.0.5\n > ")
        os.system("ls")
    # ------------------------------------------------------------------------------------------------------------
    # This method updates a deployment
    def __update_deployment(self):
        podName=ConsoleHelper.get_alphanumeric_input("Please enter the pod name:\t")
        os.system("ls")
    # ------------------------------------------------------------------------------------------------------------
    # This method deploys an ubuntu pod
    def __deploy_ubuntu(self):
        podName=ConsoleHelper.get_alphanumeric_input("Please enter the pod name:\t")
        os.system("ls")
    # ------------------------------------------------------------------------------------------------------------
    # This method deploys an ubuntu pod
    def __delete_deployment(self):
        deploymentName=ConsoleHelper.get_alphanumeric_input("Please enter the deployment to delete:\t")
        os.system("ls")
    # ------------------------------------------------------------------------------------------------------------
    # This method runs a predfined scenario
    def __run_predfined_scenario(self):
        deploymentName=ConsoleHelper.get_alphanumeric_input("Please enter the deployment to delete:\t")
        os.system("ls")
  
  
   
        

