# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
 
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import UserUtteranceReverted


class ActionHelloWorld(Action):
 
      def name(self) -> Text:
          return "action_greet_user"
 
      def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

          dispatcher.utter_message(text="Hi! Welcome to CareerNaksha. I am your Career Counsellor. I hope you and your family are safe.")

          return [UserUtteranceReverted()]


#from typing import Any, Text, Dict, List
##from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.events import UserUtteranceReverted

#class ActionHelloWorld(Action):
#
#    def name(self) -> Text:
#        return "action_greet_user"
#    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#        dispatcher.utter_message("hello, I am a demo bot")  
#        return [UserUtteranceReverted()]  