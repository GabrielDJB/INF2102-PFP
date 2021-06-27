# -------------------------------------------------------------------
# APP.PY file
#
# Author: Gabriel D. J. Barbosa
#
# Description:
#  File implementing back-end API services. Built on Flask and
#  dependent on different libraries, described in requirements.txt.
# -------------------------------------------------------------------

# Importing libraries
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, json, request, jsonify
from flask_cors import CORS, cross_origin



# ----------------------------------------------------------
# CREATE_APP function
#
# Description:
#   Constructor for the Flask application. Initializes app
#   and routes the different services to the URLs.
# ----------------------------------------------------------
def create_app(testing = False):

    # Instantiating application and CORS
    app = Flask(__name__)
    CORS(app)

    # Instantiating database client on server start and setting database
    client = MongoClient()

    if testing:
        db = client['focus-chat-test']
    else:
        db = client['focus-chat']

    # -----------------------------------------------
    # DEFAULT SERVICE
    #
    # Description:
    #   Default service. Not related to any entity.
    #   Should return a simple message.
    # -----------------------------------------------
    @app.route('/')
    def index():
        # Creating response dict to be turned into JSON
        return jsonify({'test': 'You have reached the default service. There is nothing here.'})





    # ---------------------------------------------------------------
    # LOGIN SERVICE
    #
    # Description:
    #   Service for deriving instance data based on access hashkey.
    # ---------------------------------------------------------------
    @app.route('/login/', methods = ['GET'])
    def login():

        # Getting data
        instanceID = request.values.get('instanceID')

        # Checking instanceID data
        if instanceID == None or instanceID == '':
            return jsonify({'status': 'Error', 'error': 'Instance ID is missing. Request failed.'})

        # Finding instance by ID and retrieving info
        result = db['instances'].find_one({'_id': ObjectId(instanceID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Instance was not found.'})
        else:
            return jsonify({'status': 'Success', 'chatID': result['chatID'], 'chatterID': result['chatterID'], 'categorizationName': result['categorizationName']})





    # ----------------------------------------------------------------------
    # CHATTER SERVICES
    #
    # Description:
    #   Services related to the chatter entity, i.e., those that engage in
    #   the chats
    # ----------------------------------------------------------------------

    # ----------------
    # Create Chatter
    # ----------------
    @app.route('/chatter/create/', methods = ['POST'])
    def create_chatter():

        # Getting data
        chatterName = request.values.get('chatterName')
        chatIDs = request.values.getlist('chatIDs')

        # Checking chatterName data
        if chatterName == None or chatterName == '':
            return jsonify({'status': 'Error', 'error': 'Chatter name is missing. Request failed.'})

        # Structure for entity Chatter
        chatter = {
            'chatterName': chatterName,
            'chatIDs': chatIDs
        }

        # Inserting into database collection
        result = db['chatter'].insert_one(chatter)

        # Returning results
        return jsonify({'status': 'Success', 'chatterID': str(result.inserted_id)})

    # ------------------
    # Retrieve Chatter
    # ------------------
    @app.route('/chatter/retrieve/', methods = ['GET'])
    def retrieve_chatter():

        # Getting data
        chatterID = request.values.get('chatterID')

        # Checking chatterID
        if chatterID == None or chatterID == '':
            return jsonify({'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'})

        # Finding chatter by ID and retrieving info
        result = db['chatter'].find_one({'_id': ObjectId(chatterID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chatter was not found.'})
        else:
            return jsonify({'status': 'Success', 'chatterID': str(result['_id']), 'chatterName': result['chatterName'], 'chatIDs': result['chatIDs']})

    # ----------------
    # Update Chatter
    # ----------------
    @app.route('/chatter/update/', methods = ['POST'])
    def update_chatter():

        # Getting data
        chatterID = request.values.get('chatterID')
        chatterName = request.values.get('chatterName')
        chatIDs = request.values.getlist('chatIDs')

        # Checking chatterName
        if chatterID == None or chatterID == '':
            return jsonify({'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'})

        # Checking chatterID
        if chatterName == None or chatterName == '':
            return jsonify({'status': 'Error', 'error': 'Chatter name is missing. Request failed.'})

        # Structure for entity Chatter
        chatter = {
            'name': chatterName,
            'chatIDs': chatIDs
        }

        # Finding chatter by ID and updating info
        result = db['chatter'].update_one({'_id': ObjectId(chatterID)}, {'$set': chatter})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chatter was not found.'})
        else:
            return jsonify({'status': 'Success'})

    # ----------------
    # Delete Chatter
    # ----------------
    @app.route('/chatter/delete/', methods = ['POST'])
    def delete_chatter():

        # Getting data
        chatterID = request.values.get('chatterID')

        # Checking chatterID
        if chatterID == None or chatterID == '':
            return jsonify({'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'})

        # Finding chatter by ID and deleting it
        result = db['chatter'].delete_one({'_id': ObjectId(chatterID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chatter was not found.'})
        else:
            return jsonify({'status': 'Success', 'count': result.deleted_count})





    # -----------------------------------------------------------------------
    # CHAT SERVICES
    # 
    # Description:
    #   Services related to the chat entity. Represents the top-most entity
    #   for the tool.
    # -----------------------------------------------------------------------

    # -------------
    # Create Chat
    # -------------
    @app.route('/chat/create/', methods = ['POST'])
    def create_chat():

        # Getting data
        chatterIDs = request.values.getlist('chatterIDs')
        categorizationName = request.values.get('categorizationName')

        # Checking chatterIDs
        if chatterIDs == None or chatterIDs == []:
            return jsonify({'status': 'Error', 'error': 'Chatter IDs are missing. Request failed.'})
        
        # Checking categorizationID
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization name is missing. Request failed.'})
        
        # Structure for entity Chat
        chat = {
            'chatterIDs': chatterIDs,
            'categorizationName': categorizationName
        }

        # Inserting into database collection
        result = db['chat'].insert_one(chat)

        # Returning results
        return jsonify({'status': 'Success', 'chatID': str(result.inserted_id)})

    # ---------------
    # Retrieve Chat
    # ---------------
    @app.route('/chat/retrieve/', methods = ['GET'])
    def retrieve_chat():

        # Getting data
        chatID = request.values.get('chatID')

        # Checking chatID
        if chatID == None or chatID == '':
            return jsonify({'status': 'Error', 'error': 'Chat ID is missing. Request failed.'})

        # Finding chat by ID and retrieving info
        result = db['chat'].find_one({'_id': ObjectId(chatID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chat was not found.'})
        else:
            return jsonify({'status': 'Success', 'chatID': str(result['_id']), 'chatterIDs': result['chatterIDs'], 'categorizationName': result['categorizationName']})

    # -------------
    # Update Chat
    # -------------
    @app.route('/chat/update/', methods = ['POST'])
    def update_chat():

        # Getting data
        chatID = request.values.get('chatID')
        chatterIDs = request.values.getlist('chatterIDs')
        categorizationName = request.values.get('categorizationName')

        # Checking chatID
        if chatID == None or chatID == '':
            return jsonify({'status': 'Error', 'error': 'Chat ID is missing. Request failed.'})

        # Checking chatterIDs
        if chatterIDs == None or chatterIDs == []:
            return jsonify({'status': 'Error', 'error': 'Chatter IDs are missing. Request failed.'})
        
        # Checking categorizationID
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization ID is missing. Request failed.'})

        # Structure for entity Chat
        chat = {
            'chatterIDs': chatterIDs,
            'categorizationName': categorizationName
        }

        # Finding chat by ID and updating info
        result = db['chat'].update_one({'_id': ObjectId(chatID)}, {'$set': chat})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chat was not found.'})
        else:
            return jsonify({'status': 'Success'})

    # -------------
    # Delete Chat
    # -------------
    @app.route('/chat/delete/', methods = ['POST'])
    def delete_chat():

        # Getting data
        chatID = request.values.get('chatID')

        # Checking chatID
        if chatID == None or chatID == '':
            return jsonify({'status': 'Error', 'error': 'Chat ID is missing. Request failed.'})

        # Finding chat by ID and deleting it
        result = db['chat'].delete_one({'_id': ObjectId(chatID)})

        # Checking if result was found the returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chat was not found.'})
        else:
            return jsonify({'status': 'Success', 'count': result.deleted_count})





    # --------------------------------------------------------------------------
    # CATEGORIES SERVICES
    # 
    # Description:
    #   Services related to the chat categories. These can be used in multiple
    #   chats. Each message is related to a category.
    # --------------------------------------------------------------------------

    # -----------------
    # Create Category
    # -----------------
    @app.route('/category/create/', methods = ['POST'])
    def create_category():

        # Getting data
        categorizationName = request.values.get('categorizationName')
        categoryName = request.values.get('categoryName')
        categoryDescription = request.values.get('categoryDescription')

        # Checking categorizationName
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization name is missing. Request failed.'})
        
        # Checking categoryName
        if categoryName == None or categoryName == '':
            return jsonify({'status': 'Error', 'error': 'Category name is missing. Request failed.'})

        # Checking categoryDescription
        if categoryDescription == None or categoryDescription == '':
            return jsonify({'status': 'Error', 'error': 'Category description is missing. Request failed.'})

        # Structure for entity Category (subset of Categorization)
        category = {
            'categorizationName': categorizationName,
            'categoryName': categoryName,
            'categoryDescription': categoryDescription,
        }

        # Inserting into database collection
        result = db['category'].insert_one(category)

        # Returning results
        return jsonify({'status': 'Success', 'categoryID': str(result.inserted_id)})

    # -------------------
    # Retrieve Category
    # -------------------
    @app.route('/category/retrieve/', methods = ['GET'])
    def retrieve_category():

        # Getting data
        categoryID = request.values.get('categoryID')

        # Checking categoryID
        if categoryID == None or categoryID == '':
            return jsonify({'status': 'Error', 'error': 'Category ID is missing. Request failed.'})

        # Finding category by ID and retrieving info
        result = db['category'].find_one({'_id': ObjectId(categoryID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Category was not found.'})
        else:
            return jsonify({'status': 'Success', 'categoryID': str(result['_id']), 'categorizationName': result['categorizationName'], 'categoryName': result['categoryName'], 'categoryDescription': result['categoryDescription']})

    # -------------------------
    # Retrieve Categorization
    # -------------------------
    @app.route('/category/retrieve_categorization/', methods = ['GET'])
    def retrieve_categorization():

        # Getting data
        categorizationName = request.values.get('categorizationName')

        # Checking categorizationName
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization name is missing. Request failed.'})

        # Finding categories by categorizationName and retrieving info
        result = db['category'].find({'categorizationName': categorizationName})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Categorization was not found.'})
        else:
            # Extracting category instances
            categoryInstances = []
            for instance in result:
                # Structuring category instance
                category = {
                    "_id": str(instance['_id']),
                    'categorizationName': instance['categorizationName'],
                    'categoryName': instance['categoryName'],
                    'categoryDescription': instance['categoryDescription'],
                }
                # Appending to list of results
                categoryInstances.append(category)
            # Returning category instances in response
            return jsonify({'status': 'Success', 'categories': categoryInstances})

    # -----------------
    # Update Category
    # -----------------
    @app.route('/category/update/', methods = ['POST'])
    def update_category():

        # Getting data
        categoryID = request.values.get('categoryID')
        categorizationName = request.values.get('categorizationName')
        categoryName = request.values.get('categoryName')
        categoryDescription = request.values.get('categoryDescription')

        # Checking categoryID
        if categoryID == None or categoryID == '':
            return jsonify({'status': 'Error', 'error': 'Category ID is missing. Request failed.'})

        # Checking categorizationName
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization name is missing. Request failed.'})
        
        # Checking categoryName
        if categoryName == None or categoryName == '':
            return jsonify({'status': 'Error', 'error': 'Category name is missing. Request failed.'})

        # Checking categoryDescription
        if categoryDescription == None or categoryDescription == '':
            return jsonify({'status': 'Error', 'error': 'Category description is missing. Request failed.'})

        # Structure for entity Category (subset of Categorization)
        category = {
            'categorizationName': categorizationName,
            'categoryName': categoryName,
            'categoryDescription': categoryDescription,
        }

        # Finding category by ID and updating info
        result = db['category'].update_one({'_id': ObjectId(categoryID)}, {'$set': category})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Category was not found.'})
        else:
            return jsonify({'status': 'Success'})

    # -----------------
    # Delete Category
    # -----------------
    @app.route('/category/delete/', methods = ['POST'])
    def delete_category():

        # Getting data
        categoryID = request.values.get('categoryID')

        # Checking categoryID
        if categoryID == None or categoryID == '':
            return jsonify({'status': 'Error', 'error': 'Category ID is missing. Request failed.'})

        # Finding category by ID and deleting it
        result = db['category'].delete_one({'_id': ObjectId(categoryID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Category was not found.'})
        else:
            return jsonify({'status': 'Success', 'count': result.deleted_count})





    # --------------------------------------------------------------------------------
    # MESSAGE SERVICES
    # 
    # Description:
    #   Services related to chat messages. These are related to most other entities.
    #   It is sent by a chatter in a given chat, being related to a category.
    # --------------------------------------------------------------------------------

    # ----------------
    # Create Message
    # ----------------
    @app.route('/message/create/', methods = ['POST'])
    def create_message():

        # Getting data
        chatID = request.values.get('chatID')
        chatterID = request.values.get('chatterID')
        content = request.values.get('content')
        timestamp = request.values.get('timestamp')
        categorizationName = request.values.get('categorizationName')
        categoryName = request.values.get('categoryName')
        replyID = request.values.get('replyID') # Reply ID is optional

        # Checking chatID
        if chatID == None or chatID == '':
            return jsonify({'status': 'Error', 'error': 'Chat ID is missing. Request failed.'})
        
        # Checking chatterID
        if chatterID == None or chatterID == '':
            return jsonify({'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'})
        
        # Checking content
        if content == None or content == '':
            return jsonify({'status': 'Error', 'error': 'Message content is missing. Request failed.'})
        
        # Checking timestamp
        if timestamp == None:
            return jsonify({'status': 'Error', 'error': 'Timestamp is missing. Request failed.'})
        
        # Checking categorizationName
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization name is missing. Request failed.'})
        
        # Checking categoryName
        if categoryName == None or categoryName == '':
            return jsonify({'status': 'Error', 'error': 'Category name is missing. Request failed.'})

        # Structure for entity Message
        message = {
            'chatID': chatID,
            'chatterID': chatterID,
            'content': content,
            'timestamp': timestamp,
            'categorizationName': categorizationName,
            'categoryName': categoryName,
            'replyID': replyID
        }

        # Inserting into database collection
        result = db['message'].insert_one(message)

        # Returning results
        return jsonify({'status': 'Success', 'messageID': str(result.inserted_id)})

    # ------------------
    # Retrieve Message
    # ------------------
    @app.route('/message/retrieve/', methods = ['GET'])
    def retrieve_message():

        # Getting data
        messageID = request.values.get('messageID')

        # Checking messageID
        if messageID == None or messageID == '':
            return jsonify({'status': 'Error', 'error': 'Message ID is missing. Request failed.'})

        # Finding message by ID and retrieving info
        result = db['message'].find_one({'_id': ObjectId(messageID)})

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Message was not found.'})
        else:
            return jsonify({
                'status': 'Success',
                'messageID': str(result['_id']),
                'chatID': str(result['chatID']),
                'chatterID': str(result['chatterID']),
                'content': result['content'],
                'timestamp': result['timestamp'],
                'categorizationName': result['categorizationName'],
                'categoryName': result['categoryName'],
                'replyID': str(result['replyID'])
            })

    # -----------------------
    # Retrive Chat Messages
    # -----------------------
    @app.route('/message/retrieve_chat/', methods = ['GET'])
    def retrieve_chat_messages():

        # Getting data
        chatID = request.values.get('chatID')

        # Checking chatID
        if chatID == None or chatID == '':
            return jsonify({'status': 'Error', 'error': 'Chat ID is missing. Request failed.'})

        # Finding messages by chatID and retrieving info
        result = db['message'].find({'chatID': chatID})

        # Checking if result exists and returning its content
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Chat was not found.'})
        else:
            # Unpacking message instances
            messageInstances = []
            for instance in result:
                # Structuring message instance
                message = {
                    'messageID': str(instance['_id']),
                    'chatID': instance['chatID'],
                    'chatterID': instance['chatterID'],
                    'content': instance['content'],
                    'timestamp': instance['timestamp'],
                    'categorizationName': instance['categorizationName'],
                    'categoryName': instance['categoryName'],
                    'replyID': instance['replyID']
                }
                # Appending instance to array
                messageInstances.append(message)
            # Returning message instances in response
            return jsonify({'status': 'Success', 'messages': messageInstances})

    # ----------------
    # Update Message
    # ----------------
    @app.route('/message/update/', methods = ['POST'])
    def update_message():

        # Getting data
        messageID = request.values.get('messageID')
        chatID = request.values.get('chatID')
        chatterID = request.values.get('chatterID')
        content = request.values.get('content')
        timestamp = request.values.get('timestamp')
        categorizationName = request.values.get('categorizationName')
        categoryName = request.values.get('categoryName')
        replyID = request.values.get('replyID') # Reply ID is optional

        # Checking messageID
        if messageID == None or messageID == '':
            return jsonify({'status': 'Error', 'error': 'Message ID is missing. Request failed.'})
        
        # Checking chatID
        if chatID == None or chatID == '':
            return jsonify({'status': 'Error', 'error': 'Chat ID is missing. Request failed.'})
        
        # Checking chatterID integrity
        if chatterID == None or chatterID == '':
            return jsonify({'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'})
        
        # Checking content
        if content == None or content == '':
            return jsonify({'status': 'Error', 'error': 'Message content is missing. Request failed.'})
        
        # Checking timestamp data
        if timestamp == None:
            return jsonify({'status': 'Error', 'error': 'Timestamp is missing. Request failed.'})
        
        # Checking categorizationName data
        if categorizationName == None or categorizationName == '':
            return jsonify({'status': 'Error', 'error': 'Categorization name is missing. Request failed.'})
        
        # Checking categoryName data
        if categoryName == None or categoryName == '':
            return jsonify({'status': 'Error', 'error': 'Category name is missing. Request failed.'})

        # Structure for entity Message
        message = {
            'chatID': chatID,
            'chatterID': chatterID,
            'content': content,
            'timestamp': timestamp,
            'categorizationName': categorizationName,
            'categoryName': categoryName,
            'replyID': replyID
        }

        # Finding message by ID and updating info
        result = db['message'].update_one({'_id': ObjectId(messageID)}, {'$set': message})
        

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Message was not found.'})
        else:
            return jsonify({'status': 'Success'})

    # ----------------
    # Delete Message
    # ----------------
    @app.route('/message/delete/', methods = ['POST'])
    def delete_message():

        # Getting data
        messageID = request.values.get('messageID')

        # Checking messageID
        if messageID == None or messageID == '':
            return jsonify({'status': 'Error', 'error': 'Message ID is missing. Request failed.'})

        # Finding message by ID and deleting it
        result = db['message'].delete_one({'_id': ObjectId(messageID)})
        

        # Checking if result was found then returning data
        if result == None:
            return jsonify({'status': 'Error', 'error': 'Message was not found.'})
        else:
            return jsonify({'status': 'Success', 'count': result.deleted_count})

    return app



# -----------------------
# EXECUTING APPLICATION
# -----------------------

# Calling the application constructor to initialize server
create_app()