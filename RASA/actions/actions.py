# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions


# # This is a simple example for a custom action which utters "Hello World!"

# # from typing import Any, Text, Dict, List
# #
# # from rasa_sdk import Action, Tracker
# # from rasa_sdk.executor import CollectingDispatcher
# #
# #
# # class ActionHelloWorld(Action):
# #
# #     def name(self) -> Text:
# #         return "action_hello_world"
# #
# #     def run(self, dispatcher: CollectingDispatcher,
# #             tracker: Tracker,
# #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# #
# #         dispatcher.utter_message(text="Hello World!")
# #
# #         return []

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# class ActionUtterGreet(Action):
#     def name(self) -> Text:
#         return "utter_greet"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Hello! How can I assist you today?")
#         return []

# class ActionUtterHappy(Action):
#     def name(self) -> Text:
#         return "utter_happy"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="I'm glad you're feeling great!")
#         return []

# class ActionUtterCheerUp(Action):
#     def name(self) -> Text:
#         return "utter_cheer_up"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Cheer up! Things will get better.")
#         return []

# class ActionUtterDidThatHelp(Action):
#     def name(self) -> Text:
#         return "utter_did_that_help"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Did that help?")
#         return []

# class ActionUtterGoodbye(Action):
#     def name(self) -> Text:
#         return "utter_goodbye"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Goodbye! Take care.")
#         return []

# class ActionUtterPersonalCareResponse(Action):
#     def name(self) -> Text:
#         return "utter_personal_care_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="I can help you with personal care products.")
#         return []

# class ActionUtterAccessoriesAndAttachmentsResponse(Action):
#     def name(self) -> Text:
#         return "utter_accessories_and_attachments_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Let me assist you with accessories and attachments.")
#         return []

# class ActionUtterElectronicsResponse(Action):
#     def name(self) -> Text:
#         return "utter_electronics_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="I have information about our electronics products.")
#         return []

# class ActionUtterFragrancesResponse(Action):
#     def name(self) -> Text:
#         return "utter_fragrances_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Explore our collection of fragrances.")
#         return []

# class ActionUtterHealthAndSafetyResponse(Action):
#     def name(self) -> Text:
#         return "utter_health_and_safety_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Your health and safety are important to us.")
#         return []

# class ActionUtterIngridientSpecificQuestionsResponse(Action):
#     def name(self) -> Text:
#         return "utter_ingridient_specific_questions_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Feel free to ask any ingredient-specific questions.")
#         return []

# class ActionUtterProductAunthenticityResponse(Action):
#     def name(self) -> Text:
#         return "utter_product_aunthenticity_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Our products are authentic and genuine.")
#         return []

# class ActionUtterProductComparisonResponse(Action):
#     def name(self) -> Text:
#         return "utter_product_comparison_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Let me help you compare our products.")
#         return []

# class ActionUtterShippingAndPackagingResponse(Action):
#     def name(self) -> Text:
#         return "utter_shipping_and_packaging_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Learn more about our shipping and packaging options.")
#         return []

# class ActionUtterUsageInstructionsResponse(Action):
#     def name(self) -> Text:
#         return "utter_usage_instructions_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Find usage instructions for our products here.")
#         return []

# class ActionUtterWarrantyAndCustomerSupportResponse(Action):
#     def name(self) -> Text:
#         return "utter_warranty_and_customer_support_response"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
       
#         dispatcher.utter_message(text="Contact our customer support for warranty assistance.")
#         return []