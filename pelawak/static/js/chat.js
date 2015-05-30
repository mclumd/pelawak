/*
 * Implements the chat functionality with websockets.
 */

(function() {

  Chat = function() {

    // Elements
    this.chatbox   = null;
    this.chatInput = null;
    this.chatUser  = null;
    this.chatForm  = null;
    this.messages  = null;

    // Message template
    this.template  = _.template($("script#message-template").html());

    this.init = function(selector) {
      this.elem = $(selector);
      this.chatInput = this.elem.find('.chat-input');
      this.chatForm  = this.elem.find('.chat-form');
      this.chatUser  = this.elem.find('input[name=username]');
      this.messages  = this.elem.find('.chat-messages');

      // Resolve "this" ambiguity
      var self = this;

      // Bind messages on enter to submit form
      this.chatInput.keydown(function(e) {
        if (e.keyCode == 13 && !e.shiftKey) {
          e.preventDefault();
          self.chatForm.submit();
        }
      });

      // Bind the submit form
      this.chatForm.submit(this.onChatInput(self));

    }

    // This is what happens when a user enters a chat
    this.onChatInput = function(self) {
      return function(e) {
        e.preventDefault();

        // Get and send data to the server
        data = self.getChatData();

        // Temporarily just add data directly to the message window
        self.messages.append(self.template(data));

        // Empty the chat input to get ready to type again
        self.chatInput.val('');
        self.scrollDown();

        return false;
      }
    }

    // Used to extract chat data from the chat form
    this.getChatData = function() {
      return {
        message: this.chatInput.val(),
        username: this.chatUser.val()
      }
    }

    // Used to set message scrolling to the bottom
    this.scrollDown = function() {
      var box = this.messages[0];
      var scrollHeight = Math.max(box.scrollHeight, box.clientHeight);
      box.scrollTop = scrollHeight - box.clientHeight;
    }

  }

  var chat = new Chat().init("#chatbox");
})();
