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

      swampdragon.open(function() {
        swampdragon.subscribe('chat-route', 'messages', null, function(context, data) {
          // successfully subscribed
          console.log(context, data);
          self.addMessage({
            user: 'system',
            message:'Subscribed to Pelawak chat!'
          });

          // Bind messages on enter to submit form
          self.chatInput.keydown(function(e) {
            if (e.keyCode == 13 && !e.shiftKey) {
              e.preventDefault();
              self.chatForm.submit();
            }
          });

          // Bind the submit form
          self.chatForm.submit(self.onChatInput(self));

          // Listen for channel messages
          swampdragon.onChannelMessage(function (channels, message) {
            console.log(message);
            self.addMessage(message.data);
          });

        }, function(context, data) {
          // failed to subscribe
          console.log(context, data);
          self.addMessage({
            user: 'system',
            message: 'Was unable to subscribe to Pelawak!'
          });
        });
      });



    }

    // This is what happens when a user enters a chat
    this.onChatInput = function(self) {
      return function(e) {
        e.preventDefault();

        // Get and send data to the server
        data = self.getChatData();

        swampdragon.create('chat-route', data, function (context, data) {
          // successful creation
          console.log(context, data);
        }, function (context, data) {
          // failed creation
          console.log(context, data);
        });

        // Empty the chat input to get ready to type again
        self.chatInput.val('');
        self.scrollDown();

        return false;
      }
    }

    // Helper function to add messages
    this.addMessage = function(data) {
      this.messages.append(this.template(data));
    }

    // Used to extract chat data from the chat form
    this.getChatData = function() {
      return {
        message: this.chatInput.val(),
        user: this.chatUser.val()
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
