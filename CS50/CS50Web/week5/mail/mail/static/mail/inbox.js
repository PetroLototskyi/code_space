document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  document.querySelector('#compose-form').addEventListener('submit', send);

  // By default, load the inbox
  load_mailbox('inbox');
});


/*----------------------------showPage Function----------------------*/
// Shows one page and hides the other two
function showPage(page) {
  // Hide specific views
  const views = ['#emails-view', '#compose-view', '#email-open'];
  views.forEach(view => {
    document.querySelector(view).style.display = 'none';
  });

  // Show the selected page
  document.querySelector(`#${page}`).style.display = 'block';
}


/*----------------------------compose_email Function----------------------*/
function compose_email() {

  // Use showPage to show compose view and hide other views
  showPage('compose-view');

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}



/*----------------------------emails_view Function----------------------*/
function emails_view(id){
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);

      // Show only the email-open view using showPage function
      showPage('email-open');

       // Populate the email content
    document.querySelector('#email-open').innerHTML = `
      <b>From:</b> ${email.sender}<br>
      <b>To:</b> ${email.recipients}<br>
      <b>Subject:</b> ${email.subject}<br>
      <b>Timestemp:</b> ${email.timestamp}<br><br>
      ${email.body}
      <br><br>`;

      // Mark email as read if not already
    if(email.read === false){
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
          })
        })
      }

      // Archive

    const button_archive = document.createElement('button');
    if (email.archived){
      button_archive.innerHTML="Unarchive"
      button_archive.className="btn btn-info text-warning"
    }else{
      button_archive.innerHTML="Archive"
      button_archive.className="btn btn-danger text-warning"
    }

    button_archive.addEventListener('click', function() {
      fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: !email.archived
        })
      })
      .then(() => {
        load_mailbox('inbox');
    })
    });
    document.querySelector('#email-open').append(button_archive);


     // Reply

    const button_reply = document.createElement('button');

    button_reply.innerHTML="Reply"
    button_reply.className="btn btn-info mx-3"

    button_reply.addEventListener('click', function() {
      // console.log("Reply")
      compose_email();

      // Pre fill email's fields:
      document.querySelector('#compose-recipients').value = email.sender;
      let subject = email.subject;
      if (!subject.startsWith("Re: ")) {
        subject ="Re: " + subject;
      }
      document.querySelector('#compose-subject').value = subject;

      const body = `\n\nOn ${email.timestamp}, ${email.sender} wrote: \n${email.body}`;
      document.querySelector('#compose-body').value = body;

    });

    document.querySelector('#email-open').append(button_reply);
});
}



/*----------------------------load_mailbox Function----------------------*/
function load_mailbox(mailbox) {

   // Use showPage to show emails-view and hide other views
   showPage('emails-view');

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Gett and display emails
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

    // Loop through emails and display them
    emails.forEach(email => {
      const email_element = document.createElement('div');
      email_element.className="list-group-item";
      email_element.innerHTML = `<b>From:</b> ${email.sender} - <b>Subject:</b> ${email.subject} - <b>Time:</b> ${email.timestamp}`
      //  - read:     ${email.read}`;

      // console.log(mailbox);
      if (mailbox === 'inbox' || mailbox ==='archive') {
        if (email.read) {
          email_element.className = 'grey';
        } else {
            email_element.className = 'white';
        }
      }
      if (mailbox === 'sent') {email_element.className = 'white'}

      email_element.addEventListener('click', function() {
        emails_view(email.id);
      });
      document.querySelector('#emails-view').append(email_element);
    });


});
}


/*----------------------------send Function----------------------*/
function send(event){
  event.preventDefault();
  // alert("I am an alert before fetch: line 40");
  console.log("Before fetch call");

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: document.querySelector('#compose-recipients').value,
        subject: document.querySelector('#compose-subject').value,
        body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      // console.log(result);
      // alert("I am an alert inside fetch: line 54!");
      load_mailbox('sent');

  });
  // alert("I am an alert after fetch: line 57!");
  console.log("After fetch call");

}
