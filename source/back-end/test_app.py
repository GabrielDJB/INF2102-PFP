import pytest
import app

from flask import json


# ---------------
# ---------------
# TESTING SETUP
# ---------------
# ---------------
@pytest.fixture
def client():
    # Initializing the application in the test database
    test_app = app.create_app(testing = True)
    # Initializing the test client for server requests
    with test_app.test_client() as client:
        # Yielding client reference for further testing
        yield client




# ---------------
# ---------------
# CHATTER TESTS
# ---------------
# ---------------


# ------------------------
# Testing Create Chatter
# ------------------------
#@pytest.fixture
def test_create_chatter(client):

    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatterName': 'test_chatter_name', 'chatIDs': ['test_chat_ID']}
    # Failed chatterName instances
    fail_chatter_name_missing = {'chatIDs': ['test_chat_ID']}
    fail_chatter_name_empty = {'chatterName': '', 'chatIDs': ['test_chat_ID']}
    # Failed chatIDs instances
    fail_chatIDs_missing = {'chatterName': 'test_chatter_name'}

    # ------------ TESTING ------------ #
    # Testing successful instance
    # assert client.post('/chatter/create/', data = success).get_json()["status"] == "Success"
    # Testing chatterName validation
    assert client.post('/chatter/create/', data = fail_chatter_name_missing).get_json() == {'status': 'Error', 'error': 'Chatter name is missing. Request failed.'}
    assert client.post('/chatter/create/', data = fail_chatter_name_empty).get_json() == {'status': 'Error', 'error': 'Chatter name is missing. Request failed.'}

    # ------------ CLEAN UP ------------ #
    pass


# --------------------------
# Testing Retrieve Chatter
# --------------------------
#@pytest.fixture
def test_retrieve_chatter(client):
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatterID': 'test_chatter_ID'}
    # Failed chatterID instances
    fail_chatterID_missing = {}
    fail_chatterID_empty = {'chatterID': ''}
    
    # ------------ TESTING ------------ #
    # Testing successful instance
    # assert client.get('/chatter/retrieve/', data = success).get_json()['status'] == "Success"
    # Testing chatterID validation
    assert client.get('/chatter/retrieve/', data = fail_chatterID_missing).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    assert client.get('/chatter/retrieve/', data = fail_chatterID_empty).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ------------------------
# Testing Update Chatter
# ------------------------
#@pytest.fixture
def test_update_chatter(client):
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatterID': 'test_chatter_ID', 'chatterName': 'test_chatter_name', 'chatIDs':['test_chat_ID']}
    # Failed chatterID instances
    fail_chatterID_missing = {'chatterName': 'test_chatter_name', 'chatIDs':['test_chat_ID']}
    fail_chatterID_empty = {'chatterID': '', 'chatterName': 'test_chatter_name', 'chatIDs':['test_chat_ID']}
    # Failed chatterName instances
    fail_chatterName_missing = {'chatterID': 'test_chatter_ID', 'chatIDs': ['test_chat_ID']}
    fail_chatterName_empty = {'chatterID': 'test_chatter_ID', 'chatterName': '', 'chatIDs': ['test_chat_ID']}
    # Failed chatIDs instances
    fail_chatIDs_missing = {'chatterID': 'test_chatter_ID', 'chatterName': 'test_chatter_name'}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/chatter/update/', data = success).get_json()['status'] == "Success"
    # Testing chatterID validation
    assert client.post('/chatter/update/', data = fail_chatterID_missing).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    assert client.post('/chatter/update/', data = fail_chatterID_empty).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    # Testing chatterName validation
    assert client.post('/chatter/update/', data = fail_chatterName_missing).get_json() == {'status': 'Error', 'error': 'Chatter name is missing. Request failed.'}
    assert client.post('/chatter/update/', data = fail_chatterName_empty).get_json() == {'status': 'Error', 'error': 'Chatter name is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ------------------------
# Testing Delete Chatter
# ------------------------
#@pytest.fixture
def test_delete_chatter(client):
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatterID': 'test_chatter_ID'}
    # Failed chatterID instances
    fail_chatterID_missing = {}
    fail_chatterID_empty = {'chatterID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/chatter/delete/', data = success).get_json()['status'] == "Success"
    # Testing chatterID validation
    assert client.post('/chatter/delete/', data = fail_chatterID_missing).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    assert client.post('/chatter/delete/', data = fail_chatterID_empty).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass




# ------------
# ------------
# CHAT TESTS
# ------------
# ------------


# ---------------------
# Testing Create Chat
# ---------------------
#@pytest.fixture
def test_create_chat(client):
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatterIDs': ['test_chatter_ID'], 'categorizationName': 'test_categorization_ID'}
    # Failed chatterIDs instances
    fail_chatterIDs_missing = {'categorizationName': 'test_categorization_ID'}
    fail_chatterIDs_empty = {'chatterIDs': [], 'categorizationName': 'test_categorization_ID'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {'chatterIDs': ['test_chatter_ID']}
    fail_categorizationName_empty = {'chatterIDs': ['test_chatter_ID'], 'categorizationName': ''}
    
    # ------------ TESTING ------------ #
    # Succesful instance
    # assert client.post('/chat/create/', data = success).get_json()['status'] == "Success"
    # Testing chatterIDs validation
    assert client.post('/chat/create/', data = fail_chatterIDs_missing).get_json() == {'status': 'Error', 'error': 'Chatter IDs are missing. Request failed.'}
    assert client.post('/chat/create/', data = fail_chatterIDs_empty).get_json() == {'status': 'Error', 'error': 'Chatter IDs are missing. Request failed.'}
    # Testing categorizationName validation
    assert client.post('/chat/create/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    assert client.post('/chat/create/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# -----------------------
# Testing Retrieve Chat
# -----------------------
#@pytest.fixture
def test_retrieve_chat(client):  
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatID': 'test_chat_ID'}
    # Failed chatID instances
    fail_chatID_missing = {}
    fail_chatID_empty = {'chatID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.get('/chat/retrieve/', data = success).get_json()['status'] == "Success"
    # Testing chatID validation
    assert client.get('/chat/retrieve/', data = fail_chatID_missing).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    assert client.get('/chat/retrieve/', data = fail_chatID_empty).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ---------------------
# Testing Update Chat
# ---------------------
#@pytest.fixture
def test_update_chat(client):   
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatID': 'test_chat_ID', 'chatterIDs': ['test_chatter_ID'], 'categorizationName': 'test_categorization_ID'}
    # Failed chatID instances
    fail_chatID_missing = {'chatterIDs': ['test_chatter_ID'], 'categorizationName': 'test_categorization_ID'}
    fail_chatID_empty = {'chatID': '', 'chatterIDs': ['test_chatter_ID'], 'categorizationName': 'test_categorization_ID'}
    # Failed chatterIDs instances
    fail_chatterIDs_missing = {'chatID': 'test_chat_ID', 'categorizationName': 'test_categorization_ID'}
    fail_chatterIDs_empty = {'chatID': 'test_chat_ID', 'chatterIDs': [], 'categorizationName': 'test_categorization_ID'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {'chatID': 'test_chat_ID', 'chatterIDs': ['test_chatter_ID']}
    fail_categorizationName_empty = {'chatID': 'test_chat_ID', 'chatterIDs': ['test_chatter_ID'], 'categorizationName': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/chat/update/', data = success).get_json()['status'] == "Success"
    # Testing chatID validation
    assert client.post('/chat/update/', data = fail_chatID_missing).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    assert client.post('/chat/update/', data = fail_chatID_empty).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    # Testing chatterIDs validation
    assert client.post('/chat/update/', data = fail_chatterIDs_missing).get_json() == {'status': 'Error', 'error': 'Chatter IDs are missing. Request failed.'}
    assert client.post('/chat/update/', data = fail_chatterIDs_empty).get_json() == {'status': 'Error', 'error': 'Chatter IDs are missing. Request failed.'}
    # Testing categorizationName validation
    assert client.post('/chat/update/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization ID is missing. Request failed.'}
    assert client.post('/chat/update/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ---------------------
# Testing Delete Chat
# ---------------------
#@pytest.fixture
def test_delete_chat(client):  
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatID': 'test_chat_ID'}
    # Failed chatID instances
    fail_chatID_missing = {}
    fail_chatID_empty = {'chatID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/chat/delete/', data = success).get_json()['status'] == "Success"
    # Testing chatID validation
    assert client.post('/chat/delete/', data = fail_chatID_missing).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    assert client.post('/chat/delete/', data = fail_chatID_empty).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass




# ----------------------
# ----------------------
# CATEGORIES TESTS
# ----------------------
# ----------------------


# -------------------------
# Testing Create Category
# -------------------------
#@pytest.fixture
def test_create_category(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    fail_categorizationName_empty = {'categorizationName': '', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    # Failed categoryName instances
    fail_categoryName_missing = {'categorizationName': 'test_categorization_name', 'categoryDescription': 'test_category_description'}
    fail_categoryName_empty = {'categorizationName': 'test_categorization_name', 'categoryName': '', 'categoryDescription': 'test_category_description'}
    # Failed categoryDescription instances
    fail_categoryDescription_missing = {'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name'}
    fail_categoryDescription_empty = {'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'categoryDescription': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/category/create/', data = success).get_json()['status'] == "Success"
    # Testing categorizationName validation
    assert client.post('/category/create/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    assert client.post('/category/create/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    # Testing categoryName validation
    assert client.post('/category/create/', data = fail_categoryName_missing).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    assert client.post('/category/create/', data = fail_categoryName_empty).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    # Testing categoryDescription validation
    assert client.post('/category/create/', data = fail_categoryDescription_missing).get_json() == {'status': 'Error', 'error': 'Category description is missing. Request failed.'}
    assert client.post('/category/create/', data = fail_categoryDescription_empty).get_json() == {'status': 'Error', 'error': 'Category description is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #    
    pass


# ---------------------------
# Testing Retrieve Category
# ---------------------------
#@pytest.fixture
def test_retrieve_category(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'categoryID': 'test_category_ID'}
    # Failed categoryID instances
    fail_categoryID_missing = {}
    fail_categoryID_empty = {'categoryID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.get('/category/retrieve/', data = success).get_json()['status'] == "Success"
    # Testing categoryID validation
    assert client.get('/category/retrieve/', data = fail_categoryID_missing).get_json() == {'status': 'Error', 'error': 'Category ID is missing. Request failed.'}
    assert client.get('/category/retrieve/', data = fail_categoryID_empty).get_json() == {'status': 'Error', 'error': 'Category ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ---------------------------------
# Testing Retrieve Categorization
# ---------------------------------
#@pytest.fixture
def test_retrieve_categorization(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'categorizationName': 'test_categorizationName'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {}
    fail_categorizationName_empty = {'categorizationName': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.get('/category/retrieve/', data = success).get_json()['status'] == "Success"
    # Testing categorizationName validation
    assert client.get('/category/retrieve_categorization/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    assert client.get('/category/retrieve_categorization/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# -------------------------
# Testing Update Category
# -------------------------
#@pytest.fixture
def test_update_category(client):
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'categoryID': 'test_category_ID', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    # Failed categoryID instances
    fail_categoryID_missing = {'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    fail_categoryID_empty = {'categoryID': '', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {'categoryID': 'test_category_ID', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    fail_categorizationName_empty = {'categoryID': 'test_category_ID', 'categorizationName': '', 'categoryName': 'test_category_name', 'categoryDescription': 'test_category_description'}
    # Failed categoryName instances
    fail_categoryName_missing = {'categoryID': 'test_category_ID', 'categorizationName': 'test_categorization_name', 'categoryDescription': 'test_category_description'}
    fail_categoryName_empty = {'categoryID': 'test_category_ID', 'categorizationName': 'test_categorization_name', 'categoryName': '', 'categoryDescription': 'test_category_description'}
    # Failed categoryDescription instances
    fail_categoryDescription_missing = {'categoryID': 'test_category_ID', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name'}
    fail_categoryDescription_empty = {'categoryID': 'test_category_ID', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'categoryDescription': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/category/update/', data = success).get_json()['status'] == "Success"
    # Testing categoryID validation
    assert client.post('/category/update/', data = fail_categoryID_missing).get_json() == {'status': 'Error', 'error': 'Category ID is missing. Request failed.'}
    assert client.post('/category/update/', data = fail_categoryID_empty).get_json() == {'status': 'Error', 'error': 'Category ID is missing. Request failed.'}
    # Testing categorizationName validation
    assert client.post('/category/update/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    assert client.post('/category/update/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    # Testing categoryName validation
    assert client.post('/category/update/', data = fail_categoryName_missing).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    assert client.post('/category/update/', data = fail_categoryName_empty).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    # Testing categoryDescription validation
    assert client.post('/category/update/', data = fail_categoryDescription_missing).get_json() == {'status': 'Error', 'error': 'Category description is missing. Request failed.'}
    assert client.post('/category/update/', data = fail_categoryDescription_empty).get_json() == {'status': 'Error', 'error': 'Category description is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# -------------------------
# Testing Delete Category
# -------------------------
#@pytest.fixture
def test_delete_category(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'categoryID': 'test_category_ID'}
    # Failed categoryID instances
    fail_categoryID_missing = {}
    fail_categoryID_empty = {'categoryID': ''}
    
    # ------------ TESTING ------------ #
    # Sccessful instance
    # assert client.post('/category/delete/', data = success).get_json()['status'] == "Success"
    # Testing categoryID validation
    assert client.post('/category/delete/', data = fail_categoryID_missing).get_json() == {'status': 'Error', 'error': 'Category ID is missing. Request failed.'}
    assert client.post('/category/delete/', data = fail_categoryID_empty).get_json() == {'status': 'Error', 'error': 'Category ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass




# ----------------------
# ----------------------
# MESSAGE TESTS
# ----------------------
# ----------------------


# ------------------------
# Testing Create Message
# ------------------------
#@pytest.fixture
def test_create_message(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed chatID instances
    fail_chatID_missing = {'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_chatID_empty = {'chatID': '', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed chatterID instances
    fail_chatterID_missing = {'chatID': 'test_chat_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_chatterID_empty = {'chatID': 'test_chat_ID', 'chatterID': '', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed content instances
    fail_content_missing = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_content_empty = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': '', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed timestamp instances
    fail_timestamp_missing = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_categorizationName_empty = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': '', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed categoryName instances
    fail_categoryName_missing = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'replyID': 'test_reply_ID'}
    fail_categoryName_empty = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': '', 'replyID': 'test_reply_ID'}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/message/create/', data = success).get_json()['status'] == "Success"
    # Testing chatID validation
    assert client.post('/message/create/', data = fail_chatID_missing).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    assert client.post('/message/create/', data = fail_chatID_empty).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    # Testing chatterID validation
    assert client.post('/message/create/', data = fail_chatterID_missing).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    assert client.post('/message/create/', data = fail_chatterID_empty).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    # Testing content validation
    assert client.post('/message/create/', data = fail_content_missing).get_json() == {'status': 'Error', 'error': 'Message content is missing. Request failed.'}
    assert client.post('/message/create/', data = fail_content_empty).get_json() == {'status': 'Error', 'error': 'Message content is missing. Request failed.'}
    # Testing timestamp validation
    assert client.post('/message/create/', data = fail_timestamp_missing).get_json() == {'status': 'Error', 'error': 'Timestamp is missing. Request failed.'}
    # Testing categorizationName validation
    assert client.post('/message/create/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    assert client.post('/message/create/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    # Testing categoryName validation
    assert client.post('/message/create/', data = fail_categoryName_missing).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    assert client.post('/message/create/', data = fail_categoryName_empty).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}    
    
    # ------------ CLEAN UP ------------ #
    pass


# --------------------------
# Testing Retrieve Message
# --------------------------
#@pytest.fixture
def test_retrieve_message(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'messageID': 'test_messsage_ID'}
    # Failed messageID instances
    fail_messageID_missing = {}
    fail_messageID_empty = {'messageID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.get('/message/retrieve/', data = success).get_json()['status'] == "Success"
    # Testing messageID validation
    assert client.get('/message/retrieve/', data = fail_messageID_missing).get_json() == {'status': 'Error', 'error': 'Message ID is missing. Request failed.'}
    assert client.get('/message/retrieve/', data = fail_messageID_empty).get_json() == {'status': 'Error', 'error': 'Message ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# --------------------------------
# Testing Retrieve Chat Messages
# --------------------------------
#@pytest.fixture
def test_retrieve_chat_messages(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'chatID': 'test_chat_ID'}
    # Failed messageID instances
    fail_chatID_missing = {}
    fail_chatID_empty = {'chatID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.get('/message/retrieve/', data = success).get_json()['status'] == "Success"
    # Testing messageID validation
    assert client.get('/message/retrieve_chat/', data = fail_chatID_missing).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    assert client.get('/message/retrieve_chat/', data = fail_chatID_empty).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ------------------------
# Testing Update Message
# ------------------------
#@pytest.fixture
def test_update_message(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatterID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed messageID instances
    fail_messageID_missing = {'chatID': 'test_chat_ID', 'chatterID': 'test_chatterID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_messageID_empty = {'messageID': '', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatterID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed chatID instances
    fail_chatID_missing = {'messageID': 'test_message_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_chatID_empty = {'messageID': 'test_message_ID', 'chatID': '', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed chatterID instances
    fail_chatterID_missing = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_chatterID_empty = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': '', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed content instances
    fail_content_missing = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_content_empty = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': '', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed timestamp instances
    fail_timestamp_missing = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'categorizationName': 'test_categorization_name', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed categorizationName instances
    fail_categorizationName_missing = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    fail_categorizationName_empty = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': '', 'categoryName': 'test_category_name', 'replyID': 'test_reply_ID'}
    # Failed categoryName instances
    fail_categoryName_missing = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'replyID': 'test_reply_ID'}
    fail_categoryName_empty = {'messageID': 'test_message_ID', 'chatID': 'test_chat_ID', 'chatterID': 'test_chatter_ID', 'content': 'test_content', 'timestamp': 'test_timestamp', 'categorizationName': 'test_categorization_name', 'categoryName': '', 'replyID': 'test_reply_ID'}
    
    # ------------ TESTING ------------ #
    # assert client.post('/message/update/', data = success).get_json()['status'] == "Success"
    # Testing messageID validation
    assert client.post('/message/update/', data = fail_messageID_missing).get_json() == {'status': 'Error', 'error': 'Message ID is missing. Request failed.'}
    assert client.post('/message/update/', data = fail_messageID_empty).get_json() == {'status': 'Error', 'error': 'Message ID is missing. Request failed.'}
    # Testing chatID validation
    assert client.post('/message/update/', data = fail_chatID_missing).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    assert client.post('/message/update/', data = fail_chatID_empty).get_json() == {'status': 'Error', 'error': 'Chat ID is missing. Request failed.'}
    # Testing chatterID validation
    assert client.post('/message/update/', data = fail_chatterID_missing).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    assert client.post('/message/update/', data = fail_chatterID_empty).get_json() == {'status': 'Error', 'error': 'Chatter ID is missing. Request failed.'}
    # Testing content validation
    assert client.post('/message/update/', data = fail_content_missing).get_json() == {'status': 'Error', 'error': 'Message content is missing. Request failed.'}
    assert client.post('/message/update/', data = fail_content_empty).get_json() == {'status': 'Error', 'error': 'Message content is missing. Request failed.'}
    # Testing timestamp validation
    assert client.post('/message/update/', data = fail_timestamp_missing).get_json() == {'status': 'Error', 'error': 'Timestamp is missing. Request failed.'}
    # Testing categorizationName validation
    assert client.post('/message/update/', data = fail_categorizationName_missing).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    assert client.post('/message/update/', data = fail_categorizationName_empty).get_json() == {'status': 'Error', 'error': 'Categorization name is missing. Request failed.'}
    # Testing categoryName validation
    assert client.post('/message/update/', data = fail_categoryName_missing).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    assert client.post('/message/update/', data = fail_categoryName_empty).get_json() == {'status': 'Error', 'error': 'Category name is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass


# ------------------------
# Testing Delete Message
# ------------------------
#@pytest.fixture
def test_delete_message(client):    
    
    # ------------ SETUP ------------ #
    # Successful instance
    success = {'messageID': 'test_messageID'}
    # Failed messageID instances
    fail_messageID_missing = {}
    fail_messageID_empty = {'messageID': ''}
    
    # ------------ TESTING ------------ #
    # Successful instance
    # assert client.post('/message/delete/', data = success).get_json()['status'] == "Success"
    # Testing messageID validation
    assert client.post('/message/delete/', data = fail_messageID_missing).get_json() == {'status': 'Error', 'error': 'Message ID is missing. Request failed.'}
    assert client.post('/message/delete/', data = fail_messageID_empty).get_json() == {'status': 'Error', 'error': 'Message ID is missing. Request failed.'}
    
    # ------------ CLEAN UP ------------ #
    pass