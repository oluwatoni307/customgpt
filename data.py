data = """
1

SLACK MESSAGE THREAD:
Username: jd
Text: Ok I can try to if I get time

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Hi <@U083E324RCL|Julia Gumeniuk> and <@U083N3A9NRF|Aleksandra>, since you were asking about holidays, we went ahead and decided on a clear policy around this to make it easier. <@U083N3A9NRF|Aleksandra> you had sent me , and I think what would be best is this: • You as managers can pick 15 total holidays per year for your team - it's your decision which holidays apply to the 15, but it needs to be standardized and documented for the year. • Beyond the 15 official holidays you document, everything else will be considered a PTO request and is approved by you in partnership with Trevor. Let me know if you have any questions! Thanks ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yes you can pick ANY 15 holidays you like - I totally don't care. The list is just what Aleks had sent me. Thanks all!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And what's your notta login?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: which ones did you do already?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'll work on this for you

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Oh ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just didn't want to double up if you did some

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: gotcha

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: oh right

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or just the ones in the main folder?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Meetings also?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Which sections should i be transcribing

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Working well for me so far

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Transcripts are done, loaded into Claude Project

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We can review later and work out bugs

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: answering questions etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: function combineSpreadsheets() {
  // Create a new spreadsheet to store all the combined data
  var combinedSheet = SpreadsheetApp.create('Combined Spreadsheets');
  var combinedSheetId = combinedSheet.getId();
  var sheet = combinedSheet.getSheets()[0];
  var currentRow = 1;

  // Get all files in the Drive folder
  var files = DriveApp.getFiles();
  var processedCount = 0;

  while (files.hasNext()) {
    var file = files.next();

    // Only process Google Spreadsheets
    if (file.getMimeType() === MimeType.GOOGLE_SHEETS) {
      try {
        // Open the spreadsheet
        var ss = SpreadsheetApp.openById(file.getId());
        var sourceSheet = ss.getSheets()[0]; // Gets first sheet

        // Get data from the current spreadsheet
        var data = sourceSheet.getDataRange().getValues();

        // If this is the first spreadsheet, include headers
        if (currentRow === 1) {
          sheet.getRange(currentRow, 1, data.length, data[0].length).setValues(data);
          currentRow += data.length;
        } else {
          // Skip header row for subsequent sheets
          sheet.getRange(currentRow, 1, data.length - 1, data[0].length)
               .setValues(data.slice(1));
          currentRow += data.length - 1;
        }

        processedCount++;

        // Log progress every 100 files
        if (processedCount % 100 === 0) {
          Logger.log('Processed ' + processedCount + ' files');
        }
      } catch (error) {
        Logger.log('Error processing file: ' + file.getName() + '. Error: ' + error.toString());
      }
    }
  }

  Logger.log('Finished processing ' + processedCount + ' files');
  Logger.log('Combined spreadsheet ID: ' + combinedSheetId);
}

// Add this function to handle specific folders if needed
function combineSpreadsheetsByFolder(folderId) {
  // Create a new spreadsheet to store all the combined data
  var combinedSheet = SpreadsheetApp.create('Combined Spreadsheets');
  var combinedSheetId = combinedSheet.getId();
  var sheet = combinedSheet.getSheets()[0];
  var currentRow = 1;

  // Get all files in the specified folder
  var folder = DriveApp.getFolderById(folderId);
  var files = folder.getFiles();
  var processedCount = 0;

  while (files.hasNext()) {
    var file = files.next();

    // Only process Google Spreadsheets
    if (file.getMimeType() === MimeType.GOOGLE_SHEETS) {
      try {
        // Open the spreadsheet
        var ss = SpreadsheetApp.openById(file.getId());
        var sourceSheet = ss.getSheets()[0]; // Gets first sheet

        // Get data from the current spreadsheet
        var data = sourceSheet.getDataRange().getValues();

        // If this is the first spreadsheet, include headers
        if (currentRow === 1) {
          sheet.getRange(currentRow, 1, data.length, data[0].length).setValues(data);
          currentRow += data.length;
        } else {
          // Skip header row for subsequent sheets
          sheet.getRange(currentRow, 1, data.length - 1, data[0].length)
               .setValues(data.slice(1));
          currentRow += data.length - 1;
        }

        processedCount++;

        // Log progress every 100 files
        if (processedCount % 100 === 0) {
          Logger.log('Processed ' + processedCount + ' files');
        }
      } catch (error) {
        Logger.log('Error processing file: ' + file.getName() + '. Error: ' + error.toString());
      }
    }
  }

  Logger.log('Finished processing ' + processedCount + ' files');
  Logger.log('Combined spreadsheet ID: ' + combinedSheetId);
}

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Yes, you can download messages from a specific Slack channel. Here are two main methods: 1. As a Workspace Admin/Owner: - Go to your workspace settings at [yourworkspace]. - Request a full data export which includes messages from all public channels - Private channels and DMs require Enterprise plan and special approval 2. Using the Slack API: ```python import slack_sdk from datetime import datetime client = slack_sdk.WebClient(token='YOUR_TOKEN') def get_channel_messages(channel_id): messages = [] try: result = client.conversations_history(channel=channel_id) messages.extend(result["messages"]) while result.get("has_more", False): result = client.conversations_history( channel=channel_id, cursor=result["response_metadata"]["next_cursor"] ) messages.extend(result["messages"]) except Exception as e: print(f"Error: {e}") return messages ``` You'll need: - A Slack API token (Bot or User token) - The channel ID (can be found in channel URL or using conversations_list API) - Appropriate scopes: channels:history, groups:history Do you want me to help you implement either of these approaches? ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: try that and see how it goes

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: kk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can't access that link

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Help answer questions about the paid media departments strategy and methods for managing paid media accounts. Always reference the attached document that contains transcripts from live training calls. But if the document does not include any information relevant to the query, then just say there's no information about that topic and to reach out to Mitch to update the SOP for that question.

If there is a video link available for that topic, please share the link in your response. Share think link whenever available and don't require that they ask Mitch.

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan & Mitch
Meeting Participants:Jordan Dahlquist
Start Time: 2024-12-20T14:29:18-08:00
End Time: 2024-12-20T15:54:00-08:00
Transcript: Hello? All right. I'm still waiting on that export.,Obviously, since I sent that message, I've followed through with trying to make an app and export specific channels.,Yeah, he's working on the same thing, too.,OK. All right.,Let's move this glitter stuff so we can.,Yeah, I can. Snuggle. There is something that this is in the literal state. And then it's hard.,What's that glitter for?,Those are the ornaments of the,You guys can call me Jojo.,I used to be my nickname.,All righty, so we're looking at Claude. Let me get in here. So, yeah, were you able to get into Claude when I invited you, paid media guru?,No, I was I used Login through Google like in our logins email the shared one Says an out of messages or whatever.,You need to go to the one I invited you to because that one is Mitch at And the reason I want you to do that is because you're gonna be managing Projects and different things. So I think it's gonna help you So make sure you log out of the other one and then wait you get into the right one.,you To me, a brand is one single thing, and that is trust. Customers trust you. And so brands are like bank accounts. So there's a Shared chat, this one.,Uh, all right.,So yeah, you'll go over to the left and then hit projects and then paid media guru. That's the one I put together for you. And right now it's already synced up with this video transcripts. Yeah, I did. I did only the ones in that main folder. I didn't do your meetings ones. Okay. Um, but you may want to add them. I don't know. I was going to just meet with you about it and get your thoughts on it.

 But, um, let me find the one that I synced it all up with.,I think I shared it with you too.,You should have it.,Um, the transcript of all, uh, probably I think I sent it.,the name I called it.,Actually, this is export complete.,Sorry.,Oh, cool. So you can upload that to? Yep.,Let me do you see the Word doc that I invited you to?,I do right here.,Here it is paid media knowledge database. Yep. So yeah, save that. And then basically, all you're gonna do this whole doc is literally just a header. With the name of what the call was about and the transcript and you've got like 34 pages here And so what I would do is just keep adding to it like for example your slack transcripts I would literally just paste it right in there with a header that just says slack transcripts Moving forward.

 I would not use slack to do that anymore For the most part you slack to yes Let me explain the process basically Almost like since we got this cool whiteboard Anytime you get a question You're gonna someone's gonna message you right I'm gonna say hey Mitch I don't know how to do this thing. And then you're going to go to Clog.,And then they can access that and ask Clog.,And they can ask Clog. If it doesn't know the answer, in other words, you've never included anything in your database, I programmed it. Ask Mitch to update.,And the update is going to be into this doc, and this is the database that Claude pulls from Exactly. That doc is everything.,That doc is every bit of knowledge you've ever shared. If you need to add anything to it, that's how you're going to do it. Everything's in that doc. And so if you update the doc, then Claude gets updated automatically. It's a win-win. And so, yeah, so they're going to ask you a question. Don't answer in Slack, because if you answer in Slack, nothing gets fixed. We don't know if Claude knows the answer, and if Claude does know the answer, great, then the problem is solved.

 And also, you need to train your people to start using Claude to ask questions. If Claude doesn't know the answer, then that's an opportunity for you to train Claude and add to that doc. So that's pretty much it. That's cool. So that's why I say don't use Slack to answer technical questions anymore. And so when someone comes to you, what I would tell them is go ask Claude. And if Claude doesn't know, then ask me.

 And then I'll update Claude, and then I'll tell you to go ask Claude again.,You know what I mean? So when I'm updating in here, just It looks like this is just a bolded line. So yep, that's pretty much it.,Yeah So yeah, I would just add a new header like say someone wants to know how to do X I would just pull a little header that says how to X and then downspace and then you're gonna either write out the steps or another way to do it is do a loom video and then Use the transcript from the loom video And then drop that in here It could be beneficial too. I wonder if we could even get Claude to share the link to the video where you tell them how to do it.

 That'd be kind of cool.,Yeah.,Like what if let's test it really quick.,So Salesforce ad conversions, where's the folder you sent me? Let me check. Yep.,Okay, so where which one was that salesforce All right, so it's this one so we're gonna do is make a shareable link so I'm gonna hit share anyone can view I'm gonna add it to this All right, now let's,test it and see if it works.,Let me refresh this.,What was that about Salesforce? Salesforce Google Ads conversions.,OK.,So I'll just say, how do I connect Salesforce to Google Ads for conversions?,That works, probably.,But then also I need to update this thing really fast.,If there is a video link available for that topic, please share the link.,Okay, let's try that.,Might have to refresh one more time, but we'll see.,Hmm, it's hanging out here.,Actually, let's fix the programming on it.,You don't have to do all this. Yeah. This is good.,I haven't been using it until recently.,Yeah. Yeah, I've tried a bunch of different ones We're talking about podcasts I was listening to the guy who's the main dude on that Lex Friedman podcast Anthropic, dude Nice.,Yeah. Okay, give me the video link. Sure, I think it's good. We're not pulling it yet.,We may need to Yes, probably try that person should grab it. Yeah, it's saying there is no link right there is so it's clearly Not Getting it I'll try disconnecting and then oh That's why Okay, this is an issue I recognize into is you can only connect a live doc to private projects.,And this is now a public project?,Yeah, this is a team project.,So there's two options. What I did was I just downloaded a PDF of the doc and uploaded it here. But that's not live. So anytime you update it, it's going to have to redo that. So what we could do is just give each person a duplicate of this in a private mode. You know what I'm saying?,So maybe we should do that.,So let's make it private, if we can. I don't know how to do that.,Let's see. Can you duplicate the project?,That's a great question.,It's not very hard to just redo. Like, we could just do a Private, great. And anyone who that doc is shared with will be able to access it?,Mm-hmm.,They just need the private project.,Yep.,Let's see here. We could do, wait, it's cold.,Pay media knowledge database.,Oh, this is, I'm in the wrong account. No, I'm in the team plan.,What's up here? What is this under?,Hey, it worked. Sick. All right, so now.,Brilliant. There we go.,It's working perfect now.,Let me see if I can just verify real quick. Settings, versions, navigates.,Thank you. You Yeah.,Very good.,So that gave them a video link and everything. But I didn't even program this one yet with direction.,So let me grab that.,So I programmed it to do, but this is something you could also think about as you go, like if you want to make it do different things. The only thing I told it to do is help answer questions about paid media department strategy, methods for managing paid media accounts. I said always reference the attached document that contains transcripts from live training calls. I specified if the document does not include any information relevant to the query, then just say there's no information about that topic and reach out to Mitch to update the SOP for that question.

 And the reason I say that is because I don't want cloud just coming up with stuff. It should probably come from because you might have a unique angle on something. So that means that if it doesn't have anything, it's going to just tell them ask Mitch. And so in that case, that's where you get that alert to. Yeah. And also, when you do your loom videos to make the transcripts work better, try to use lots of descriptive language.

 Yeah, I usually try.,Yeah, totally. Yeah. Yeah.,Like you could say, OK, now I'm navigating to this dropdown in the upper right where you can change the date.,Otherwise, it's not going to.,Yeah, it'll just help it know more about it. Yeah, for sure And then I said if there's a video link available, please share it in your response So, yeah, awesome Okay, yeah, oh Man you go to a chiropractor or something.,Yeah, I was going to one for a while But Yeah, I'm alright. I just get tight. Yeah.,There's some Advil here if you need it.,You know it's a standing desk, so I try to stand a lot. That's good. Is your whole paid media team here at all, or are they?,Keaton is not, but everyone else is. If you want, we could have a quick huddle with them and show them how this works. Sure. If you think that's useful.,I think it's useful.,Cool. Alright.,Let's do it.,You can share it on your screen and demo it if you want.,We need to make it a private project, right?,We actually need to invite all of them to their own account. Good point. Let me go invite all them. Here, can you add in all their Emails.,This is users. I'm assuming.,Yeah. Probably.,All right, cool. Let's see, verification.,I'll probably talk to them a little bit too about like how to add Questions.,Hello.,I can't see anything.,Usually my computer's kind of... I guess because it's a PC, not a Mac. I don't know. Sometimes it works.,If it doesn't, you can probably just show them on your computer.,I'm not sure you're smart enough. Yeah, we can just get on that.,Sure.,It doesn't even work right now.,Or do you want to go to the other one? I usually hit this button and it's like all these menu.,I could do it on my computer if you want.,Uh, sure.,If you can connect to the TV. Which one's this one called conference room. Pretty sure this one's conference room. Maybe this one's Preston's TV.,Let's try this one.,It's not where we want to be. Honestly, it's probably not a big deal. I could literally just show them on my computer here.,I can just gather around.,So I got two of four You can explain it to them whenever yeah, or you can you get in the loom I'm Jordan. Yeah. Nice to meet you. I Know we've been ships in the night Yes from Claude, yeah, yeah cool so I'll show you up here what we're doing I mean It would be a good thing, but we need some more commenters for that. We need some more commenters for what we have.,Yeah.,All right, so basically we're trying to work on a knowledge database so it's easier to get your questions answered. So what we've done is trained a Cloud AI on every video recording and every Slack message that So when you have a question You're gonna be sad But instead of going to Mitch, you're gonna go to Claude.,Mitch has needed this for longer than we know.,You're going to ask Claude your question, but I'm going to give you some coaching on that too. And then if it doesn't know the answer, it's going to tell you to ask Mitch. And the reason we do this is because I don't want Claude making up answers. So it's programming.,If it says ask Mitch, don't keep like, just go ask Mitch. And Mitch is going to be gracious enough to update the database with that new information so that you never have to ask him again.,And Claude will forever count on you.,Sorry.,Mitch is so happy right now. I literally just sent him the, why can't we not answer with what the fuck are you talking about?,There you go, no longer. So, if it does know the answer, fantastic. If it doesn't, if it gives you an answer, but you're still confused, what are you gonna do then? Don't go directly back to Michigan, go stay in Claude, and you're gonna say like, ask more questions. Be like, okay, I'm stuck on this part, how do I figure that out? You know what I mean? And work with Claude. And so that's what I wanted to say about the asking questions part.

 Is you need to talk to it like it's a woman. I'm pretty sure you guys have plenty of experience with these actuals.,Are we going to have pre-read prompts?,Well, that's what I was going to show you.,There's actually a tool called Prompt Perfect.,And if I could share my screen up here, I could show it a lot easier. No, I don't know how to do it.,With the little check on the top?,Here? I don't know. She wouldn't go like what's the thing here? Yeah, I tried that I tried both and it wouldn't do it. Yeah You can go to Yeah, all good. You can go to prompt perfect dot AI Mm-hmm, and it's free for quite a while. We could always get a paid account if we really need it But this is kind of not mission-critical you can put in a basic question like, how do I connect Salesforce to Google ads?

 And then it's going to optimize your prompt for you with a way bigger line of questioning. And then you copy that and then you paste that into your cloud. And then it's going to give you like a really hardcore answer, like really in depth. But it might be too verbose. So you may not want to do that. You may want to just ask a simple question and run with it. That's one way to do it. But what I was going to say is you don't have to do that.

 Like, the more you can just talk to it like a human, the better. Don't try to be like robotic.,Don't try to be like anything just literally like for dummies, literally, like for dummies, like tugging him like or just just be like, I'm trying to do this thing.,I have tears what I've tried, like literally talk to as you were talking to Mitch, like, be like, Hey, I did this thing. I'm trying to connect it here. I'm getting stuck up on this part where I do this and blah, blah, like explain it.,And then it's going to answer you more realistically.,So for example, is it uploaded everything now?,Yeah, almost. If I ask him like, hey Mitch, how can I do the dynamic insertion headlines on an elementary page?,We'll get there. We have the messages in Slack. But this just right now has training videos and not are full meetings, but we're getting there.,But I've told him he's no longer allowed to answer questions in Slack. He has to now, if you ask a question and it's for sure not in Cloud, he has to record a video, upload that transcript into the knowledge database here, and then tell you to go back to Cloud. So nothing lives in Slack anymore. We just have to be clear on that. Another thing I forgot to mention if there is a video with it You had a link to the video This is really cool you can ask for the video link for that topic if he's done a video See I,need more videos and oh wait, I'm on a roll wrong topic.,But for example, if you were to put, um, Oh, we're not in the project. Oh, that's why.,So there's, um, like essentially essentially this project and yeah, this is what has, um, the database connected to it. So I'm going to ask you this question, right?,It should provide the video.,So it's going to give Mitch's answer. So this is Mitch talking right now.,This is based on his info, OK?,And then you'd say, can I get a video link?,Or whatever.,You could just say video link, probably, and it'll do it.,I think this is the one we didn't program yet, and that's why it's not providing it automatically.,No, this is synced up.,This is the new one. Oh, you changed the prompt for it?,Yeah. So I asked for an answer on a topic and then I said, can I get the video link? And boom, you can go right to the video where Mitch literally taught about that topic. So there you go. You have to make sure there's a difference between a chat and a project. A chat is not programmed with Mitch. Only projects are. So you go to projects and then you go to paid media guru, which we're going to talk about in a minute.

 Actually have to create on each of your accounts. What's the chat for? Chat's just general quad.,Okay. Yeah. Using it. Pretty damn good by the way.,It's better. It's better at writing. Okay. Yeah. Chatty BD is better at some things, but for, if you want to write more natural language text, you have to have a spit something out and rewrite it. Kind of Yeah. The next step is basically you need to share that knowledge doc with each person and then you need to set up their project.,Yeah. Yeah.,Um, cool.,That's pretty much it guys. Anything you want to add?,Uh, could you send me the prompt for the project?,Um, oh yes.,Yeah.,Um, anything I want to add?,Um, what was the name again of the prompt expert one?,We're going to make it for you. It Okay. Yep. But it will be as soon as he sets it up for you. He's going to have to set it up on your computer, so he's going to come out and do it for you. It only takes a minute.,Does that make sense? Yep.,Do you have hesitation, Bobby?,You know, just someone entered. I have no idea who that was. I didn't look over.,He said hi to you. He said hi?,Yeah. Nice guy.,hesitation is just, um, I think that's it. It's like, instead of asking, instead of Keenan saying, let's ask Google, it's going to be like, let's ask Claude. Yeah. Well, you can still ask Google if you want.,You can ask everything, but this is going to help save you having to go to Mitch a lot.,And then, uh, we have like, you know, sort of proprietary ways that On the internet and so this is yeah trained who's your whole paid media team or can you add me to the channel? Or yeah, I could just get sent it to everyone I'm just gonna send it to you guys and you can set up your own project.,Okay, it's super easy. You just hit create new project I'll put the instructions for you.,All right. Thanks, guys. See you. No, we're good.,Oh, nice. Oh, you were major?,Oh, damn!,Oh! I think that counts.,Yeah, you too.,Okay, wow.,By the way, there's a way to export Asana, but I think it exports is a spreadsheet or at least that's the way I've exported it before But I could probably put a spreadsheet within the doc What are we talking,about?,Asana What about it? We have like a lot of stuff documented just within the sauna project.,Oh cool Yeah, export that and stick it in there too. Yeah, that'd be great. I would just think of anywhere and everywhere that you can pull from,Right.,Just fire it in there.,you Okay, there you have it All right, man Well, let me know how it goes and I'm sure there's gonna be little bugs and things a lot to fix as we go, right?,But hopefully we can continue to optimize it and get it to where it's pretty solid. Yeah How do you feel like your team's doing overall Um, pretty good.,That's why, um, what's the vibes. So we've, we're, we're pretty stacked, like on clients, um, right now. And, um, so, you know, we were mentioning last time, like with Preston and so, Like, you know, sometimes we lose a trust in the beginning and yeah, we're just we're getting like good number of clients right now and There's been just some issues I've noticed within the setups. It's really like small nuanced like Stuff but sometimes that makes like a big difference but overall Pretty good And yeah, I don't know Every team member kind of has their own strengths and weaknesses.

 But I mean, I feel like we're doing pretty good. Obviously, I want to be doing way better. And there's a lot of little mistakes and things that need to be cleaned up. And I think this should help. That's great. We have the paid media department. Which cooperates with the design department. Um, and so I'm just trying to think how to, uh, put together some things to like make processes a little bit clearer and like checklists and stuff.

 Um, I've been told sometimes those processes don't get followed and when they don't get followed, things do slip through the cracks. So, um, need to Work on that Got it Yeah, that makes sense What kind of things slip through is it like it's usually tracking shit like we're getting a track No, it's like setting things up. But then I mean sometimes it's as simple as like not installing like to call tracking metrics plug-in but then Yeah, because design builds things.

 So yeah, the paid media account manager is supposed to do all these things to be included within the Asana task. And then they do these things when it's delivered and update. And then, yeah, here's all the things.,How does it follow through if you have such a good checklist?,I just don't think people even use a checklist sometimes. It's like there, but I feel like...,Do you think it's too detailed to the point where it's like pointless, like there's too many checks?,Yeah, and I don't like the fact that it's even listed on a Google Doc at all. I'd much rather things So I don't have to go through different platforms. Yeah.,It seems like you need a Asana template that you just create a new clean slate every time for that new client. And there's a whole onboarding checklist, right? Is that what you have?,Yeah.,So why aren't we doing that?,So it's not the Google doc?,So like, here, let's look at... Like it sounds like a Google doc. Like you were saying, you guys use a Google Doc is my point, but Yeah, I hate the Google Docs. The Google Docs are just for specific parts of specific tasks.,That sounds really confusing.,I agree. Yeah.,So there's this, so it's like, I made links to a Google Doc. I'd rather it just be within. It needs to be all right there. I agree. Yeah. Yeah. That's the way I've wanted it to be. There's a little bit extra context. But then, yeah. So you have a subtask. You can click it. You can add more info on the subtask if you do it there. Yeah. That's the way I wanted it to be done. And I think, yeah, we agree it's a bit confusing.

,You know what I think we need to do is set up a type form where each step in the type Form is an action item. And there's a box where they have to take a note on what they did. And then at the end, it spits it all into the Asana. So the Asana task isn't even created until it's over.,Does that make sense? A little lost, to be honest. But yeah, type Form, and you're starting a project. Yeah, so sorry. And then you enter in the details. Basically, a new client comes in.,Instead of going into Asana, All it is is a new client onboarding type form and the type form, each page on the type, cause you know how a type form, it's like each page is different. Yeah. So each page is one step and they have to go one by one and they can't go to the next page until they've like done that thing until they've completed all the steps. And then, uh, when they're done, it's, it's, it's like, you know, spits out it using Zapier, we can sync it up with your Asana and create a new task with the final conclusion of them wrapping that up.

 And then what we could even do is have it make it so that it puts all their responses into the Asana for you to review and it notifies you, and just to make sure they set it up properly.,Does that make sense?,Yeah.,Yeah. Like each one of these steps, would be one page on the type form. And then they have to write in a note that says, like, here's how I did it. You know what I mean?,Maybe?,Yeah.,One way that we could do it. Yeah, I think the confusion is, like, try to put blockers. I some of them are like skipped around because it should be like, okay I do this thing first and then this thing and then this thing and I think You know that is part of it. It's also been rushed and I know Preston was talking about like having a month and a month for what sorry to Like because we saw the client it's like yeah, we'll be ready in a week, which is kind of crazy.

 Oh Yeah, which puts us under? A lot of pressure. So you're like forced, plus you're managing all the other things. People have a lot of clients at this point. And so...,So the Typeform wouldn't work then because it's actually a month-long process then. They're not just going to go in and fill out this form in one day and then it's all done. It's a process. Yeah.,Yeah.,Okay.,So Asana probably is better, but it looks like maybe we just need to optimize it better.,Yeah, I've been wanting to. Okay. Yeah. It needs to be optimized for sure. Google Docs thing I've never really been fond of but it was just a way to get like Yeah, because at one point we had this other girl who's not with us now But she helped get some things out of my mind of like, okay, what do we do here? And after we do this, we do that and I was just like Bam Bam it lives in a Google Doc hasn't left the Google Doc.

 Yeah, got it. Okay, so Yeah, so I just need a of tell people like, once we once we have that it's like, everything's in Asana. You know, here's how to navigate through it.,Can you walk me through the process right now?,Yeah.,And also outline like what are the issues? What do we need to fix?,Yeah, that would be a good exercise for me too. Okay.,So, We're going to use this template.,So lately, usually what I'll do is I'll assign each person, some of them have due dates already installed, but, uh, you know, I'll assign myself or the account manager, the proper things. Um, and so that first thing would be creating an audit, excuse me.,Yeah.,Which, um, at this point it is now, but, um, but that's another issue is that there's a disconnect there, right?,Like between what you can do, what they're promising and like, right. What sales?,Yeah, you mean outside of Asana, just like what?,Yeah, like in other words, the sales department is going and selling business and then people are coming in. But is there a disconnect between what they're selling and what you're doing?,Much less so. Definitely used to be a bigger problem. I think where it is a bigger problem is when it's not some of like our niche stuff. And, you know, our like our bread and butter, if you will, works at certain, like, it works at 60K. If you don't have 60K, 55K, maybe, it doesn't work. But we were saying, hey, it was being sold like, oh, you only have 30K? Yeah, we're gonna get you this result.

 It really works at 60K. They don't say that part. But they had learned, because we have gotten some of those 30Ks not done well. So we need to find a strategy that works.,Okay.,Um, so yeah, it's better, um, than it used to be.,Okay, cool.,But they, it essentially has to be me or Preston or Sam, um, doing the audit. Salespeople aren't trained to do any of the auditing and they don't really know how to forecast like a realistic picture without my help, which is fine. I get that, but all right. Okay.,So you do that initial audit proposal and then you go into. And then the sales thing.,Um, yeah, deal sign, uh, attend pre-internal kickoff call. So Kim coordinates, uh, you know, like me, it was mostly her and Nick, who's going to be the account manager for another account. Anyways, we talk, about the stuff that they talked about in sales and how things are going to go. We have a questionnaire, so they should have filled out the questionnaire.,Sure, this is in big red. It's the latest one done.,And yeah, maybe this doesn't need to live in a Google Doc. But it has a bunch of different information and this is a client Yes, and I also asked a real one.,That's one filled out. Yeah, we're seeing them.,Okay.,Yeah So you have to create a new one every time?,Yeah, we have like a one and we copy duplicate, you know, there's Google Forms, yeah, okay Cool. All right, so you fill that out.,Sorry to keep distracting. No, no keep moving.,Yeah, for sure. Um, and then Where does that go?,Does that go to an account manager?,So yeah, Kim typically sends it to us and then we put it in a folder and so This this should probably be actually this is yeah pretty on-boarding So then we look at there's this website built with basically I tried to scan their website for stuff I know they're using so I can get access to it Okay Look at their target. I keep fucking perfect. Um See if they've been doing ads and stuff to kind of just get in my head and when I'm talking to them Have a better idea of what they've done already if they haven't listed it.

 Yeah the deal So yeah, those are the steps They need legit scripts as part of it kickoff meeting Schedule that legit scripts. That's it legit. So Addiction treatment is a really protected. Oh, this is compliance.,Yeah. Okay.,Um, and so here's a template, um, which I just updated actually, uh, recently, um, on an email. So like here's instructions on how to get access, um, or grant access to us with any of these different things. Um, nice. Good job on that. Um, and then this could probably, probably go since I just updated that. That is a larger doc, which platforms are changing, so I don't know if it's up to date. And then kickoff meeting.

,So this is things they ought to talk about in the kickoff meeting.,And then this is applying that compliance thing to the account. Channel in Slack, client folder, reports we use, get them in there. And different people are assigned all these different things.,This is really a sub-task of this. Who gets assigned all these?,Is it just different people depending on phase or something? Yeah, it's kind of a little bit of a process for me that could probably be But yeah, I'll go through and sign him. He needs to do this this day.,What's Session Buddy?,Session Buddy is awesome, man. It's a way that I have found myself to work way more efficiently. So you're at your bar and you love calling me up out of nowhere to ask how your ad account is. And she's like, hey, what's going on? I'm like, hey, well, I'm doing pretty good. Blah blah blah, here's everything that I need access to, to the account. Here is, so I asked that, yeah, they set up these tabs.

 This is the way I like to work. Keaton has his own little thing that works, so that's completely fine. But yeah, try to make it a point. So here's their, Here's the sheet, the call tracking metric stuff with the filters that I like, the campaign, everything. So what does Session Buddy do? Save the session.,This is a window so it saves that window so I can close it.,I mean I have a hell of a lot of windows open. Oh, I see.,So like for each client they have their own session, basically like thing going on.,Yeah, so you need to have them all open at the same time. There's other ways to do this. But yeah, like this is home base for me. This is always open. And my stuff gets gnarly. Okay, cool.,I got you now. That's sick. I had never heard of that. That's awesome.,Yeah, there's other browsers that do this in their own way. Chrome might even do it now, but I've done this. Well, I do a lot of tab grouping. Yeah, that's what Keaton does.,I do that kind of stuff. And then I have different, every email has its own set of browsers for me. Stuff like that. Cause I have different companies and stuff like that. So it's like, I'll have different browsers. Like this is my personal company with all the different tabs.,Chrome and stuff. Yeah. Yeah. Um, yeah, that works. Um, I don't know how the, I don't know how resource efficient that is, but that way I can close this.,Yeah.,That's awesome. Now they have like, they'll, put tabs to rest and shit. Anyways, so that's what that is.,Um, yeah. Okay. So what are the issues then?,Um, like where's the ball getting dropped?,So like, I hate to like call specific personnel and I know Nick, that's what we're here for. You're a director, man.,Yeah. It's business. Nick is what we do. Uh, he was the one that was just here.,Yeah. Okay. Yeah. He's, he's a really smart dude. Um, but he's been doing this for a long time. And so, you know, none of this was there when he started. Um, and I mean, kind of the same thing, but anyways, it's, uh, some of like the, basically the landing page checklist thing, like it wasn't done at all for one last client. Um, there was some tracking shit that was missed. Um, He understands the ads.

 He is Nick Nick Petsch Jeff Jeff Cavish. Yeah and so Yeah, there was a like little ball drop there, but he has I mean to his defense Yeah, he has a lot of clients that are just signing and so I don't know but hard to keep an eye on things and know exactly But dude didn't make the checklist and we had and I hate the fact that it's again in that that Google Doc Yeah, but yeah, he didn't do that.,Well, maybe what we can do You're off next week, right?,Um, I mean pretty much the standard days that I'm off.,Yeah, so why don't 24th 25th, um How about January, we lock in a day to sit down for an hour and get this hashed out. And I can help you with it to whatever extent I can. Do you want to do that?,Yeah. Okay.,So first week of Jan could be like Honestly, Wednesday or Thursday morning.,It's like, I have your calendar.,First or second. Oh wait, that's going to be new year's day. So let's just push it to the next week.,So we'll do Tuesday morning.,Um, or Tuesday.,11 after your refined call.,Yeah, I I Would say I would skip that one, but I feel like I owe them Keaton's been doing fairly decent with I mean, he's doing great with the communication there, but I think we need to do a little better There's other things he's talking about.,So anyways, you have to refine call Works for me All right, so we'll work on getting that nail down and then after that on the... Where did that meeting go?,Okay, that's Tuesday. I'm lost right now.,I'm in December as well. All right, here we go. So then the next day, can we have a meeting to roll some heads? Everyone you have to do this checklist?,Uh, sure.,Wednesday.,Sure. Is there a time that everyone's open? Um, what's your whole team?,Bobby? Yeah, Bobby. Sam.,Oh, Larry. Okay.,So it looks like 11 on Wednesday works. Cool. It doesn't even we'll make it an hour but we don't have to use the whole hour. That sound good?,Sounds good.,What do we want to call this?,Process training?,Yeah, sure. OK, and we're going to do it. Is everyone going to be in the office? What do you guys do? I don't know. Is it hybrid?,So, I mean, Nick lives in Pennsylvania. Babby lives in Mexico. So it'll be here and over Google.,So there we go.,Sam and Keaton should be here.,All right. So then we're going to get that nailed down Tuesday. Wednesday, we're going to roll some heads, make it happen.,And then moving forward, we just enforce.,That's it. All right, cool. So then. Yeah, I really want to work with you on. Just like some leadership training and some sort of goal setting for you personally, because I want to hear more about like what are your career aspirations like, What do you want to be doing like, I want to get you out of Feeling like you're in the trenches all the time and just trying to survive and I want to get you into like thriving, leading, feeling like you're growing in the company and that your department's growing, because that's the whole goal behind all this, right?

,Yeah.,So can you kind of give me some thoughts on like that and like where you want to go, where you see yourself a year from now, ideally, what do you feel like could be holding you back from those goals? Like, maybe you can kind of lay some of that out for me, if you don't mind.,Yeah, I mean, Yeah. What I've kind of like, what I would love to do is to, yeah, not really do as much of the, obviously a client facing day to day, helping with all that stuff and this should help. And then getting to a place where I'm trying to come up with different strategies doing a better job at I Mean we're gonna have the associate directors talk to The Like the clients and stuff. So I don't know if I'd be doing much of that.

 But I mean, it would be cool to just Be a larger part of I Mean even an almost stale part to stand like, you know, I get on the strategy call And you know come up with strategies and I really enjoy doing that And I and I like seeing it through and having success So Yeah, and I Want the team to grow and us to You know Have a good name in the space and my name be tied to it So, yeah.,Okay.,Um, one thing I was curious about, why is Sam handling hiring for your department? I'm just curious.,Um, I think she just had the time for it and wanted to do it and help out and I don't really care to, I mean, I interviewed a guy this morning. Okay. Um, and she kind of did like the screening.,And so that was a process we came up with and you know, I don't really care who does it. I was just curious how that came about. Um, yeah, so I think just from a couple of days of observation, I think like you have like super deep knowledge and skills. That wasn't documented and that was a huge pain point. So hopefully we figured that out with Claude. And the reason that's a negative is because it's keeping you in the trenches, right?

 We need to get you out of the trenches. So another thing that's keeping you in the trenches is management. And I think the way you're currently managing people is making your life harder on yourself. I haven't worked with you very long, so I'm not sure. For what the ins and outs are of it. But I just know for sure that we can get you really humming in terms of how you manage people and making your knowledge transfer happen easier and building greater respect in your team.

 So anyway, are you open to working with me on that and growing in that area? OK, cool. That's good. Yeah. To a point where what I envision for you is paid media basically outpacing every other department would be amazing.,I felt we have the potential to do that for sure. Totally.,The fact that it's grown so fast already is a really good sign. So I think it could outpace everything. I think you could do really well. I think you could be making a ton of money in the company. I think the only thing that I see holding you back is being stuck in the trenches, but it's not the trenches that is causing that to happen. It's your brain. It's the way you're managing. It's the way you're reading.

 It's the way you're thinking about work. And so what I want to work with you on is trying to get you to think more about systems and how you can work less. Because when you work less, that opens up more room for creativity.,My day feels so chaotic that It's hard for me to like let that Creativity out sometimes, you know, there's I'm like bouncing back and forth between things Yep, and you know, I'm in all these different channels and yeah people ask certain things and You know, so go in there and give You know my two cents when they asked for it. And the whole Claude process, I think will help tremendously. And then you sent that video the other day, or last night.

 And yeah, I watched it. And there's definitely been points where I've given the way they described is like a half response because I have been scared to fail. So, yeah, I mean, hopefully everyone on my team. What are you scared of failing? What exactly would you fail in? Accounts failing, you know, like there's that number we're looking at and yeah, we've done good this year. But we could have done a lot better.

 And I don't think we could have saved all those accounts, but there was, you know, the little stuff slipped through the cracks, um, stuff that if, um, I were more free, uh, you know, at the time and we had stuff like what we're trying to set up, you know, I'd be able to tackle, you know, this, this and that, that may have been a reason why we lost a number of those big clients. And then, uh, Yeah.

,Do you think the things that fall through the cracks, are they sometimes things that clients ask for and then we just forget to do it?,Or is it usually like internal things that we already should be doing, but we just don't do it?,The latter.,Okay. Yeah. Got it. Yeah, sometimes I mean, there are the things that clients ask for that, you know, like, I don't know, video creation. There's one client that Keaton's managing and they're asking for all sorts of different creative stuff. We've been able to tackle it on.,It's good.,Hi, on the list of destiny.,No, we talked about it.,What is that? So he, Kyle Henry. Yeah. Yeah. Yeah, also owns a billing company and stuff. One of our big struggles is being able to get enough of those like sales qualified viable VOBs. Anyways, we use business to business data with the data that they have to target on Facebook.,Oh, the thing we've been working on all morning.,Yeah. Okay, cool. Yeah.,Sorry, no, you're good sidetracked But yeah, I mean there's Sorry, go back to the original question. I know we're talking about like things that clients out for I'm just trying to identify Where we can fix things to make it better.,That's all and I think Yeah, I mean there's I want you to start thinking about how to change your brain. Like one thing that I had to learn as I was building businesses was not just how am I getting work done, but how am I changing how I think about work? And like the more efficient you can become, even if it means like sacrificing for a minute now is going to help you. And so like thinking about paying your future self, things like that, like one of the most life-changing books, it's like probably the most life-changing book I've ever read.

 And it's like, you know, boring book I've ever read, but it was the most life-changing book, was Getting Things Done. And it's literally just about keeping inbox zero, like having no emails in your inbox, having no unread slacks, having nothing, and having allocated times to deal with that. Time blocking, things like that, because it sounds like you're really flustered a lot through the day.,Yeah, some days more than others. I think I've been flustered more of the, not today as much, but yeah, the past couple of days.,Yeah. So I mean, there's ways to fix all that kind of stuff. And we need to get your head out of the trenches and into a more elevated level. But all we need to do is implement systems. We need systems and processes and checklists, which we're going to work on and fix. But I just think start. Start thinking about how you can change your brain and your approach and your thinking about everything you're doing.

 How you communicate to people. How do you execute work? How do you respond to questions? How do you do everything? And just looking for efficiencies. Anytime you're doing something, ask yourself, how could I do this once now and then never have to do it again? You know what I mean? Just like we did with Quad here. How do I record one video and then never have to do this again? You know what I mean?

 How do I create a system on my calendar so I can set this one event and I never have to deal with that again? How do I respond to this email in a way that I never have to respond again? You know, like you were talking about the half answers is a good example. Like, how do I make sure I respond to this in a way that it's evergreen? It's going to live forever, you know? And I do agree that you need to be more on the sales side, too.

 I agree. I think that when we're onboarding and selling clients, you need to be involved in that process and coming in with the big guns of like, Hey, I already did a bunch of research on you guys. I know everything there is to know about you outside of being in your ad account. Here's all the things I found. Here's how we're going to fix it. You know, and then relaying that quick, easily to your department through a system that you put in place.

 Um, one thing I think we need to roll out immediately is read AI for your whole team. It's basically like a call recorder.,Okay.,Uh, is you guys use meet geek, right?,Yeah.,So is this the one you used?,I remember talking to Preston about it cause I liked it. I was, you got a new one.,Yeah.,You use a different one last time.,Really?,Was I on circle back? Yeah. Okay. So the reason I changed back to read is multiple reasons. Circle back was cool for a minute, but I learned that the integrations weren't as good It doesn't connect with a peer and stuff is good. So read is better So I was testing circle back for a while, but read has been the one I've been with a lot longer Okay, before that I was on fireflies before that. I was on otter I tried everything.

,Yeah, I remember choosing I like me geek, but I do Think it can be better in a lot of ways.,So show me Yeah, so for example, you can go into a call Uh, and it'll actually See you guys, yeah It'll coach you on how you did It'll talk to you about your charisma your bias questions asked and this will help you with client calls and your team because you can monitor their calls Another thing though is you can grab the transcript And one thing I did What I did was I created a... What I did was I took all my read calls, all my emails, and all my slacks, right?

 Basically everything I'm doing digitally, put it into a project that updates in live time. And now Cloud knows essentially everything there is to know about me and every meeting I'm in and everything. Even right now, I'm recording our meeting because I want to be able to remember back, was there any tasks I needed to do? Was there anything I need to remember? I want Cloud to be able to know that. Why isn't Cloud loading?

 What's going on here?,It's tweaking.,Information denied.,OK.,JD's world right here. I'll just say like what?,Yeah, it's basically going to go through. This is a,I just updated it today, so it's only grabbing my slacks right now. But I have another one on my other cloud account that's email specific, that's read specific, that's slack specific. And so basically, my point is, is it all pipes in into this cloud project right here. And this has everything I'm doing. I don't even go in. It's just literally as a database, right? So now my point is, is like when you pipe in all your information into one place, then you can execute project way, way quicker and way easier because I can have a meeting with Preston about like a bunch of really complicated stuff.

 And then I can just go into cloud later and be like, okay, we talked about doing all that stuff. Go ahead and create the document around that. Or I need an email for the team or I need, And it already knows everything. I don't have to think through anything. So I'm using ways to use tech to not have to think, basically. You know what I mean? The less time you can spend actually working, the more time you can do more things.

 And so I really think that we should get everyone on a read, because you can then also pipe things into Asana. So you can actually tell Zapier. Like, hey, when action items come out of my read, send them into Asana for myself. Does that make sense?,I'm probably going to take off, too.,Yeah. You guys doing good?,Yeah.,Yep. We're going to get that list, too.,Yeah, it's going to fucking change everything.,And some of the stuff that we're talking about right now. I shouldn't use the word some.,Yeah.,I'm sure you talked to Preston about the whole read AI thing.,Not really.,Yeah. Yeah. So the reason this is cool is like, we can we can set up our whole team on this. And then the reason it's dope is because you can get on a sales call with the sales team, do an entire thing, not have to take a single note.,Be present, be present.,It's going to spit out action items. And then you just literally like forward this entire brief to your account manager. And then they're as good as if they were on the call themselves. They can even go back and watch it. And then those action items are ready to go. And like, no one ever misses a beat. It's all like totally synced up, connected. Um, Very cool. You could even be doing your questionnaire, bro on the call on the onboarding call typing it in and then yeah, you can literally just ask them the questions They're gonna answer it and it's all gonna get transcribed and then pumped out and sent into your sauna task, you know So let's just start working together on how we can do all this stuff Because it's gonna make it like It's gonna blow your mind out of your skull.

,Yeah sounds fast It sounds like you said yesterday, you know, sounds like stuff I wish we'd done a while ago. And, you know, next time is now. Yeah, totally.,Yeah.,But just focus on your mindset to focus on being positive, hopeful, like really like you're the head of the you're the head of the ship of your little department. Right. So it's like if you're feeling hopeless, if you're feeling negative, if you're feeling like you're drowning, the whole team's going to feel that way. It's just how it is like when you're when you're leading your energy goes it starts at the top.

 That's what the thing and so Your team is gonna be as successful as you can think and believe and it's gonna ooze out on them They're gonna have more pride in their work.,And so I just really want you to focus on like that Pride excitement hope it's gonna happen. So Yeah, I don't want to sound like too Too negative and perhaps I have been Because I'm just trying to Express to you kind of how I felt so we can solve problems totally And yeah, I mean, I'd hope the team doesn't think I sound you know all that negative so I would implore you to ask them and because I But I know you know if I'm asking like how can I be better or whatever, it's going to be hard for them to say that to my face.

 But yeah. I agree with everything you said.,The thing about your team is you don't always want their feedback. I think a lot of times managers over-index on how much feedback they take from their team, but sometimes feedback has limited purpose when it comes to the lower team. Feedback for the lower team team is, do you feel supported? Do you feel like you have the resources you need? Can you execute your work? And are you like, generally like happy?

 You know what I mean? That's the only feedback you need from them. The best place to get feedback as a leader is from another leader that's observing. You know what I mean? Because they can actually see the full picture. Because if you only ever asked your team for feedback, they're never going to be happy. Like literally, you know what I mean? It's going to be hard. Like not everyone's always happy in business.

 And what you have to do is set your mind like steel on your vision and help people to understand what that vision is too, by being very comprehensive and robust and how you talk about it. And then that's going to permeate them. You know what I mean? And so if your vision is on the issues too much, everyone's vision is going to be on the issues. Your vision is on The success you're gonna have and These issues are nothing.

 They're literally stepping stones towards the success. That's how your team is gonna feel too You know what I mean? And so I'm not even saying that you've been negative What I Am saying is I think it's an area that you could grow in is casting vision for your team and Almost like think of your team as like a little company in the company And like you have the ability to literally blow it out of the water with that team And if you do blow it out of the water, it's not only going to be really exciting for you, but it's exciting for everyone in the whole company.

 And you're going to earn a lot of respect. You're probably going to earn more money. And it's going to take your career to new heights. You know what I mean? Not everyone is motivated to do that, though. So that's a decision you have to make. But think of yourself as like the captain of the little ship that you have. And you're thinking, OK, I'm trying to get from Great Britain to the Americas, you know I'm not gonna focus on all the scurvy on the fact that we're running out of food the fact that one of our sales broke off I'm gonna focus on there's the horizon.

 I'm gonna focus on the direction. Where are we going? How do we stay positive? How do we keep people alive? That's the main thing, you know what I mean? And then solving problems as you can but like focus on like where you're going, you know Those are just my thoughts But yeah, I'm excited to get a bunch of this knocked out. I think we're actually gonna turn your NSMs around way quicker than anyone thinks, to be honest.

,I know we have the potential to do it and the knowledge and the ability.,Yeah, totally. A lot of it is just the vision and believing that you can. I'm not joking. Like if you can see something and envision it like it's literally possible, but if you can't it's not gonna happen you know, and that's one thing I see that a lot of people run into like Even people are trying to start their own business, you know, if they can't envision something It's not gonna happen and it really goes back to like faith.

 Faith is what brings what is not real into what is real and so When you can picture your NSM's turning around and visualize and visualize that and picture where you're gonna be in six months and 12 months. And then all you're doing is aligning your current reality with that reality because you're so locked in on that. It's literally going to happen. You know what I mean? It's all about just, oh, that's my vision.

 That's where I'm trying to get to. What's keeping me from that? What are the roadblocks?,And how do we knock those out?,So there are no roadblocks that can keep you from it. Like we're going to do it. It's just a matter of how fast can we move everyone be and how adaptable can everyone be to innovate, you know.,So that's literally the only pullback. Yeah, cool.,You're going into the... I am.,I should probably take off.,Yeah, me too. Go take a shower.

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan and Preston
Meeting Participants:Jordan Dahlquist
Start Time: 2024-12-20T11:41:51-08:00
End Time: 2024-12-20T14:28:15-08:00
Transcript: When hit a good stopping point, let's jump into some stuff. Thank you. Thank you. Silence. Silence. Thank you.,Yeah. You get it. I just need. It'll be, I can show you. It's not hiring. Okay, cool. Or you can always go to the eye and make sure it's in there somewhere. Let's see if it works.,Okay, I'm going to.,Okay. So, yeah. Oh my god.,Just completed.,But,Sickly sick sick.,and the Again, yeah, that's cool. We're just staying at the hotel right now. I probably have a lot of friends here still, right? She can go do stuff. Cool.,Okay. Okay.,There it is.,It says it did, but I can't find the sheet that it made. There's no error. I don't really want to hit any of them.,that's 1.,30.,Bye.,and the Earth to Major Tom. I'm ready. I'm ready too. Let's do this. Okay, so this is my agenda of discussion. It doesn't all have to get done in this conversation, but SOPs need to get done.,We're already like working on that, right? At some point I need to get depth understanding of the NSM goals, the CSAT goals, where it currently stands, our financials, like, I need to have a deeper picture. I've just gotten like overview so far. And just discussing strategy around that. I want to talk about sometime in January doing like, just AI basic AI training for like everyone in whole company because like I feel like everyone does a little bit but they're like there's a lot that we could help to make their jobs a little bit faster.

 Talk about, I want to talk about the eight-week sprint plan and get that like refined out to be exactly what you want. Figure out my employment agreement since that's right around the corner like what are we doing? How's that gonna work out? And then discuss the design department if we Okay, so those are my my goals. So As far as what's most important, maybe it's the eight-week sprint or in like deliverables for January or it could be Climate or it could be going into like the deep.

,I would love to go into these details of like some financials all that to those all three are important to me so let's Just so that you can have an overview I'm I'm gonna Work on and like also sharing those sheets with me because a lot of those I don't even know I'm gonna work on that vision deck and get it done Probably by this time next week because I'll not be in the office. I was hoping I'd get more on it, but Obviously So when you say sheets aren't shared with you, do you have the shared drive?

 Lipser? Yeah. Everything's in there. Oh, cool. So you search like, uh, NSM dashboard. Okay. Not seeing it.,It's a spreadsheet, right? Um, anything? Oh, whoops.,I don't even know about visibility file.,Yeah.,I don't know why. Because this guy's the fucking owner of it. So you need to duplicate it? Create our own? Yeah, but it's got scripts that run on it. And different things. And he didn't even fucking help create it. I don't know why he's the owner. Can you call him?,Or just say, can you bring in your ownership?,What does Sam ask him?,So maybe this is where we should go. Do you need to take five minutes to respond to some people? No, she's overwhelming. OK.,I'm sorry. No.,It's just because I'm, when I'm in the office. Okay, so we are going to go to shared drives. And then I will put a shared drive right here. I'm going to call it visibility. Okay, systems. Create that, and we should add Jordan to our push. Push, add members. And let's put sessions in.,Sessions.,And then, I think what we do, I'm going to create a new folder for the speech department.,See you in a bit, radio. Bye.,I'm not seeing that folder still.,Oh, there it is.,So you created that outside of WebServe? Is that right?,Am I understanding?,Yeah, I created it and it's on shared drive. Okay, cool. Just because more privacy. Yeah, we can we can share. So I don't have this, you're going to work on getting the sheets moved in there, so that'll help. Well, let's copy the sheet. So let's file. Make copy.,watching.,That's nice too, if you want one.,Well, you've got it on.,I'm pretty hot.,I'm pretty crazy with that kind of stuff. That's good. Keeps me from getting worms. Should I cut to that, but it's all good.,I put it in there, but we'll need to put it in the logger. Mm hmm.,Because it's like live feeding from somewhere. Yeah, because the data is updating from somewhere, is everything. Mm hmm.,Where do you put it?,OK, yeah. So do we even have one for the other departments yet or not?,Not for NSMs. They don't do anything like that. They should. Should. But it wouldn't be relevant on a monthly basis. They need to set... Quarterly or something? Probably one set of quarterly business review. Okay. But SEO's got major problems. But they're not like... Materially affecting our company, but they will at one point if it grows too much and we don't address it, but there's no middle managers of any kind.

,We'll continue working on that. And then we should probably, I mean, it's not going to mean anything.,Everybody access.,So everything is being focused on retention. The QPT department has the most structure, but the most problems, and it's more of like a systemic issue. But is that because of bad marriage? Because it is so crazy yeah, but I That doesn't mean that we're not going to be able to do it, right? Our goal is to get to 94% eventually, so the targets are 94% net revenue retention. On a quarter by quarter basis, because that's when we do bonuses.

 But in what we originally talked about, we talked about it on a monthly basis. I think it's just going to help awareness. Muddy the waters. Well, yeah, because No, no, no, I mean net retained revenue Because Because it just is I Okay.,I think I messed something up. We're. You.,What are you doing? Trying to set goals? No, this is a thing that my friend built and I was checking it out. Okay, cool. So, let's just make a doc. What? For what? Just kind of outlining these things. Oh, sure. So, goals maybe? Share with you. So, so, NRR. So, create and deploy revenue. Visibility.,So it sounds like you don't have that in place financially though, right?,Kind of, like here, check it out. So quick folks. The revenue is easy. We're the thing that we really don't have in place is more of is more of like drew really hit down so far.,But I've got to keep surveying.,That can be really hard too. So, yeah. So, let's just go into a, you know. So, we can do, we have to run it on approval for this because I don't know. Yeah. I don't want to penalize them if our clients totally are behind. We're just going to, we just, you know, they're X number of days behind me. But here you can see the revenue by month by department very easily, right? Yeah. Big media, SEO. Great.

 Can you export that to me so I can, you want a P&L? Sure. Yep. I mean, I just feel like anything I can do to build a bigger picture right now is helpful. Is there an NRR column we can create or should we just measure that?,I guess that's what our sheet will do.,Oh, man. Is there a way what? Nothing. I was just having a brain fart. Have these communicate? Yeah. Yeah.,But we don't have the systems built.,So I can get you into QuickBooks and we can just build those.,And if we're going to, if we're building a system, that's great.,We'll just wait until the system's done. Right. But a long time. It's just so we're trying to classify things so that we can just drill down a few more levels. Right. Yeah. So right now I can drill down to our departments. Soon, I'll be able to drill down to our employees. Right. Like who the to account manager. Yeah. So that's what's being built right now. That'll be awesome. But it'll be client.

 And then it'll be perfect. Okay, so we've got our numbers.,You're building a system who's building that is that Seth or or who's... Nobody's building.,And our specific, our accountants or bookkeepers, we're doing advisory with them to work to make more and more powerful reports so that we can make better decisions. So they're doing that.,My question is, how do we get that info into our NSF spreadsheet so that I can know what we're measuring?,It's easy I can punch in the numbers manually no like I could Like run report and sync data Mm-hmm export to Google Sheets. Oh cool it And then we can sync it.,Exactly. Let's freaking do it.,Let's make it happen right now, Gavin. So that I can do. But it's going to take some messing around with like what filters we want on the report.,Well, I just would love to get it done. Toenail.,It was not a toenail, it was like,,I'm messing it up. It's not a piece of the bread.,It's a bread, yeah. I'm just joking.,It would just be cool to have it done by January so that we can start hitting hard, really measuring.,Yeah. Yeah, I agree. I just don't disagree at all. But export faster. OK, allow. Or you could make me an admin.,Admin on QuickBooks and I can start.,Yeah, we're gonna do all this stuff too. You can be an admin on QuickBooks. Okay, here it is. Like how are you getting this like what oh is that pulling from these is that connected to this yeah so check it out they're supposed to update it every okay we got tabs and then so every Friday it will run Okay. And it'll say... Where do they put in their numbers? Here?,Right here. Monthly NSMs.,Can you just explain what every tab is to me?,So sheet 28 is nothing.,I was just checking.,So monthly NSMs is where they punch in their shit. They put their numbers in. That's the only thing anyone has to enter.,Alright, cool. So they're putting in all this stuff. And everything else happens. Got it.,Okay, here's a question for you that I thought about yesterday when you were talking about is like How do we know where if they're putting in honest data? Because as we get bigger Trust system isn't always going to be super good Like they may not be they may be like all crap.,I had a horrible month I'm just kind of like fudging number. This is what we need to do with it, right? Yeah, we need to make a dashboard Using this sheet They get shared with the client during the project phase. Because basically what it'll do is it should be external visibility. This is our internal visibility system.,Do you have the external viz sheet example from distortion?,The director? Yeah. They use that. This isn't created yet.,They're working on it, but it's they're building it for us Yeah for our marketing efforts amazing. Yeah Yeah, so I'm just trying to identify what things do I need to build what's being built like, So I'm asking tons of questions.,We basically have to do it all because fucking nobody takes a role of like like doing it You're doing this though Yeah, they're all trying to directives doing it for our marketing we pay them to do our LinkedIn marketing,gets their way better But they're not doing it for paid media like for our team We're just seeing how they're doing it and we're grabbing it For us.,Yeah, I pay them for coaching and they don't care.,They'll share stuff with I want to see the I want to see their client facing Transparency sheet.,Okay.,Once I have ours built. We'll just use it. Yeah, but it's really really easy. Got it I'm just all about basically basically what it's it's gonna do Where did the NSM cheat go? I think it's There yeah, so Basically, I would take the active Or maybe it would just track a quarter because so you can pull all these. Oh, that's fancy. So like, okay, this is what clients get in Q1. Didn't really do it in Q2.

 Started doing it a little bit in Q3, but it wasn't accurate.,And now Q4, like as of yesterday, we're finally like doing it.,Yep. Okay. Got it. And I don't know. Know how this is going to change once we finish q4 if we're just going to have to empty this out and restart it or if it doesn't for us I think it does it for us because okay and then what's next account status uh account status is just if you want to see like quickly who's who's missing their nsms this is Just to help people to meet close or close under project.

,Yeah.,So these ones are outdated targets.,These are clients that turned. Yeah. Wow. This is so cool.,All right. And then as leaderboard associate director board. So why? Oh, because this is just paid media. So we have Sam and Mitch. Why is it Sam to isn't Mitch? Like in charge?,They're both acting as associate directors right now.,But everyone told me Mitch is the boss. Is that not true?,He's acting as an associate director, but he is, his title is director. That's the boss. So he's in charge of Samantha, but they both have the same title. He is in charge of Samantha, but what we're trying to do is bring an associate director, they're interviewing for it now, and that person will become the boss of, I think Mitch is in charge of Nick, and that's really it right now. So we're short an associate director, and we're short a account manager.

,So you're gonna have a third person besides Mitch and Sam, that's another associate director.,Mitch will step away from associate directors. And then it's going to be his problem to make sure this all gets in order. And then what's his title? That's the director of paid media. Got it.,OK.,His title's not changing. And it's just never done.,So he's still the director, but he's still doing the associate stuff.,I got you now. Yeah. Because we just started putting together this structure. Got it. OK. And so how it works is there's a portfolio.,So and so one question associate directors.,Yeah, there's a portfolio. So you go on an NSM So you'll see Mitch is actually managing a client Sam is Keaton's associate director. Okay, Sam is actually managing that client Okay, Sam is Bobby and Keaton's director. Okay, you'll see if it says Nick Mitch is the associate director that the changed their name on here, it does it automatically. Got it.,Yeah. Sick. Yeah. So, okay. And then strategists, leaderboard, this is like, this is everybody putting them all against each other.,Yeah. So Fabby's like winning right now? Potentially. In terms of performance in Q4?,She handles like some of the shittiest clients.,So she's amazing? No. And she has the worst clients, wouldn't that mean she's doing good? I just mean like small clients. Oh, they're easy clients.,Yeah. So Fabi's not good. She could be, but I don't know. I wouldn't want her to manage my ass. But look, so create super happy. The people that love Fabi, love Fabi. Okay. So they're meeting. Okay. This is a decent client. This is actually a decent client, so it might be unfair. This is a little bit messy because this is a legacy deal. I'm wondering if it's churned or what's up. She's not editing them, which leads me to believe that maybe there's an issue.

 This one is a TMS client, and we don't want TMS clients anymore. So that's... Is that a type of insurance or something? Cranial magnetic stimulation. So we had this partnership with this medical device company called Nero stuff. They had all these clients and they're small clients. They're like, Oh, you should make an offering two grand a month, blah, blah, blah. We sold it to like 50 people. Wow.

 Like, uh, two years ago. Okay. And then we're like, this fucking sucks. Yeah. Way too much. Uh, and over time we lost some, but there's like four or five, pay your odds. That we either need to fire or just give to one account manager. Potentially that would. And then client month over month.,So this is showing specific clients how much they won or missed. And then, wow, so much red. By a lot. Percent miss All right, and then but that's the just quarter over quarter.,It's measuring. All right All right, these are all our clients paid media we don't any more than that. Nope. Those are not all of our clients.,I don't know I need to fix that Oh all there we go, it's on the wrong setting. All right Wow, so this whole quarter is really bad.,All right, but it's, it's honestly, yeah, it's not the whole quarter. Like, we rolled this out kind of at the end of Q3. It's not even fully rolled out. It is fully rolled out, but, but just barely. So, like, the historical data is no good. So it's just no bueno. But this, this is accurate. Three weeks yeah this is where we are yeah that's real life anything before that like we need to delete all that old shit like so it's not distracting us well I think this is gonna reset right for the new,year yeah okay and then overview we could go back and delete all the old shit client travel so this is measuring how many directors went and saw the client? Yep.,Last travel date. Is this? We haven't used it yet. Okay. But again, literally everything you do on this sheet is in here. So like, if you wanted to figure out last travel, we may have deleted that row.,like how many times because what if you don't we want to know like if we saw a client three times in a year versus just the last time we saw them or do you not care uh I do care uh it's just a lot to roll out right we can evolve yeah you're right yeah okay all right so that helps me yep so that's that so and then for the this NRR one, this is where we need to start punching in all the numbers. And so did you say you're going to sync this up somehow?

,Or do we have to manually update everything? Well, we don't have a finance team. Directive does. And so, I mean, we've got a wish list, you know, trying to get there. So we start more elementary than they do. OK, we can. We don't need to say, OK, paid media to SEO, paid media to performance design. We can just say paid media cross sold X number of dollars this month. No one one roll up per department.

 That's the job of the director would be enough.,Yeah.,Yeah. So I can simplify this down way. So we could say, This needs to say like December.,Yep.,So we need to measure upsells and cross-sells per department. Sure. Could I just share this whole shit with them or do you want to keep this kind of private? No, no, no. I don't want to keep it private. The only thing that I kind of want to keep private is expenses that we invest in other shit that's not related to Oh, OK. And I don't care if you know about that, but but I don't want to like public to the whole.

,Yeah, that makes sense.,Or is it like huge amounts? Is that why? No, not really. I mean, it's a lot over a course of a year. You know, you know.,Well, then that would mean this should not be public because this is oh, no, this is literally just, you know, gravity. Yeah. So this is good.,I, that's why I'm trying to classify everything because I do want to share expenses, but only as they're applicable. Right. Totally. Like, so, so this guy I have in New York could help with a lot of this stuff if you want it. I can show you the stuff that's going out to other businesses.,You could act as like a finance debt. Okay.,Well, we can, we can look into it. Think it's going to be necessary to do those things. But there's, there's, but yeah, these are the things I want you to be thinking about. And in, in one way, I think maybe, you know, the link building thing was was maybe the wrong first thing, because it sets a precedent that you're going to be working hands on trying to trying to roll out services with like individuals, I want you to to get the directors to do that.

 I want you to track the performance. I want you to optimize the performance. I want you to have the directors report to you and I want you to hold them accountable.,I totally understand that. I guess that's what I'm trying to break through to right now, because I'm stuck at this little ceiling where I don't have access to stuff and I don't have the information about it either to get to that level.,So let's share the actual working file of the NSM forward with you. Okay. Because this is the one they work off. Cool. Share JD. And then, you know, we're not trying to any access from you but like let's uh let's just like go back to report list. Open up P&L. I can show you. So uh investments outside services there it is so um okay so it's like 70k over here no it's like 900k but this is the payments to kyle and myself we just pay ourselves as contractors so we have another contract level that we can We get charged, uh, like expenses too.

,So, so your outsiders is basically you're part of that cost basically.,Yeah. So it's like 400,000 this past year that we've invested into. No, no, no. This is LS is, uh, logical software, software company we've been trying to build. Oh, okay. Cool. Uh, SG was sunset guns. Then these are consultancy contractors that maybe were associated with those things. Let's see what they were. No, this is not. We're moving. These are web server related. So that's, you know, we're trying to clean all this up.

 Yeah, but for sure. So this $93,000 out the door was not to webserve. This $24,000 was not to webserve. There's probably another $150,000. So it's not a ton.,You shouldn't make that a big thing for other people though.,And these I don't care about. That's just us paying ourselves. So what Kyle and I do is We'd pay ourselves 4% of the revenue as our kind of target because we're trying to grow the business. It motivates us and it keeps our capital retention up. So yeah. That's awesome, man. I like it. So that's our target. So it's good. Good stuff. So nothing, nothing like, there's nothing all that weird here. Just, just basically, you know, probably the cleanest thing to do would be to in these outside services.

 I don't even need to work on those.,I just wanted to know how do I get the information into these sheets so that they're accurate.,get you access. That's my main thing. Cool. I can just get you access to this.,Mitch sent some random screenshots over to Laurent and told him to go into Slack but then he has no access to Slack or anything like that so I don't know why. I don't know what that was all about.,I was probably like, what the heck?,And then I responded to Mitch and I was like, are you sure he has access to our Slack? And then he said, no, he does not. And then I was like, OK.,you I was like, I don't understand Uh, yeah, but the point of these, so you're in here now. Okay. Point of, um, uh, I mean, if you look at it, it's just like web serve, which isn't right, but it's But your tax guy is sort of helping with all that stuff, right?,Okay, he's great.,Yeah, so you guys are good. We're just It's much money out of California In a way that mm-hmm doesn't raise any like red flags because they're vicious to totally I get it Eventually, you couldn't you just make it an Austin company with a California location, but like what you're like is we're trying to make, you know, not a ton of money.,Yeah. That's good. Yeah.,That's our account balance growing by that much. It's not really like, well, we, we could make an opposite company, but the California would not be cool. They'd come out with me and Kyle. Why?,We're just moving whole thing. You're, you're living there. Yeah. I don't understand.,I agree. I agree with you, but California does not. We've got fucking 30 employees, you know, 20 of them in California, you know, they're, they're, uh, got it. And we get, we get fucking sued by them. So it's just stuff No, we're moving that direction. Okay.,Is that why that one girl's from Austin? Are you trying to hire in Austin now?,I really don't. Okay, here's an idea.,What if we made it a goal over the next year, like all new US-based hires are in Austin? That would make sense. And try to merge it so that it becomes more balanced, if not even like leaning more towards Austin. Yeah, that makes a lot of sense.,Because then this would become a satellite location, and then you're Yeah. So, we've talked about it quite a bit. For example, Sam's hiring right now.,Why are we not hiring in Austin?,We should be hiring in Austin. Not Orange County. I don't disagree. Or out of country, or out of state, or, you know, basically anywhere but here. But that's just one part. They'll say, okay, We'll look at where all your clients are basically they want to come after you for any They might have a list of 10 things, right? And you know if six of them are true that they think the money's theirs It's bullshit.

 You know what? And we could we could just move the company to Austin Immediately stop paying them and there's a chance nothing would happen, but it's not a good chance. It's gonna be You're not a betting man So what we're doing is over the course of like two to three years we're we're Gonna merge over there in that direction. Okay, but the money what we're doing right now Once it doesn't make very much money.

 Yeah, which is perfect. That's how you want it the the Powell company and the McHenry company. Yeah money Yeah. And so we've put agreements between those companies and WebServe to legitimize our relationship. My question is, how did Bastion do?,Because I worked at this huge agency called Bastion, and they were technically out of like Pennsylvania. There's not a single human in Pennsylvania from that company. Totally. And they're making like $10 million plus. But did they start in Pennsylvania?,Yes. That's the thing. California's been getting money.,So the transition is the issue. Exactly. We never started in California.,Right. It would have never been on the radar. I got you. Yeah. Okay. That makes sense.,Okay, so next. So now I have access to all that. I can start working on spreadsheets. I can do that kind of stuff. So where do I get the CSAT responses for the tracker?,So it's being built. Got it. OK.,When it's done, can you make sure I get it?,Yeah, but it's really important that we bring Laurent in to define our project phases. And we want a CSAT to come at the end of it. Well, we need to get Laurent what he needs.,So maybe you should just send him something.,I did. Oh, you did? Okay, I didn't see anything go through. Yeah. Okay. So yeah, you've got quick folks. One thing that's going to be important to understand about upsells is so because customize this. Let's just do like a filter. And let's do. So look, they added vendor employee class product service. So let's just go to We're going for it, going for it. This is where we make, this is where we actually see the ad spend line on.

 So this, what you're spending on ads, WebServe? No, this is our percentage of ad spend. So we build $103,000 in ad spend. After rolling that out this year, we could have done way better. But if you're paid media accounting, your ad spend contributes positively to your NRR, right? So like, let's say you lose... So you want to charge a fee plus percent of ad spend, is that what you're saying?,Yeah.,Yeah, yeah, yeah. So we'll do a flat fee, and each calendar month, if you go over what that fee comes The fee is basically the minimum. So if you're a paid media manager, and now you're responsible for making up for a loss, then you've got a couple of things that you can do. You can cross-sell your clients, or you can get them to grow their budget, so long as their contract is one that accounts for that.

 So, you've probably covered, how we try to do it is figure out what they've spent on an average calendar month the last 90 days. And we'll say, okay, you've covered up to this amount. For overages, you're at 12%. So, yeah. Or whatever, it's not always 12%. Here, I'll show you. So we have a sliding scale. Yeah, it works kind of like the IRS.,Because the more they spend, the cheaper you should get, right?,Yeah. So here's the pricing model. So for the first 20 percent, you're paying three K no matter what. Or first 30 K. Yeah, totally. Or six K. That first 30,000. The next one's at 13 percent. So that next $30,000 and $3,900, right? And then 10% anything. Monthly? Yeah. So like, if your last three months, you spent 50k on average. Yeah. Our sales team, they can discount this. But not all. Right. So that's, that's our and a And so I can hit my target of, of, you know, revenue retention.

 So I'm just saying that this ad spend line item, as this gets cleaner, it's going to get easier.,This is all in by 2026.,We're going to have such a cool picture. Yeah.,Everything.,Yeah. It's going to be amazing.,Cool.,And then, um, Last three things was going over the eight week sprint. Yeah, let's let's go over that.,This is just a cloud thing that I punched out real quick.,I haven't like taken time to go through every detail. But if you want to look through it, this is based on the directive stuff that you sent.,Yep.,There's probably some little things But it's a framework.,You should make them do this so that they have to like, get you what they have and you can see how they're tracking it. That is what they have to do. But like, you're running into some things where, you know, it's becoming hard for them to do it because, yeah, because, hey, I'm trying to compile these department metrics and struggling here. Okay, well, look, we're working on this visibility systems dealio, like, like, it's all gonna live here.

 And like, next year, you're not gonna have this issue. Let's get the best that we can. Yeah. So vision and core opportunities. You just have to make sure that they're focus on growing the department. And things that we can do to grow the department are going to be around retention, that's in their control. And then, and then cross sales and upsells. So we just got to make sure that we have to make sure that that's like, in their minds.

 Yep. Like, in other words, what do you want them to do out of that?,Like, here's how I'm going to cross sell my clients.,Here's when, here's why. I think you kind of need to work with them to create a system because right now. That makes sense. On the paid media side, it's the associate directors that need to do it. Right. The SEO side, we don't have associate directors. So we need to prove some of this stuff out and then we need to move to So Trevor's department needs development, whereas the paid media department needs to take the fucking stuff that they have, put it into action.

 Because they're like, oh, we're so busy with this, that, and the other, and we don't care about what your plan is. We're just gonna click on books.,I keep hearing from you and Mitch that he works really hard, but to me, Trevor is the that works hard. To me, Mitch doesn't work that hard. Maybe he works fast, but does he actually work hard?,He's here long hours. He is? He's doing a lot of things he shouldn't be doing. Okay. He does work hard. Okay, that's good.,I need to hear that, because like, just from observation, I'm not seeing that energy.,Okay, well, he's... But I've only been here two days. He works long hours. He's here till 7 p.m. Every single night. He's, you know, and the Ready to do it.,All right. And then third is service offering review. Yep. Analyze current offering performance, identify optimization, define ideal client profiles, and then deliver an analysis, client segmentation, optimization recommendations, blah, blah, blah.,Does that sound good? Yep.,For week three? Week four. So the marketing strategy piece may rip out entirely. Okay.,Because this is to market their own department, right?,Which actually they shouldn't be super involved but it kind of falls on like the hey like You're not really a director and in your director in the name. Oh, oh, yeah, Dino. Mm-hmm a dino Like an avatar no remember there the Rhinos Republic and name only, they made a big thing about the Senate rhinos.,I have no idea.,That's like a big political talking point. Really? Like the last five years, they call them rhinos. Somehow I missed that.,Yeah.,I don't know. Sorry.,What do you mean?,I don't really care. So you're saying... But now they're dynames. Got it. Okay. We've got dynames. False names. Yeah. Okay. Well, let's just leave it for now. And if we get to week four that's not making sense yet, you can pivot. And then sales strategy, define sales process role. This is, I wish we could honestly do this sooner, but I do think it's inappropriate. I actually, can we just, can we just change out week four with week five?

 Because I'd rather hit this way sooner.,Gotta hit that, yo. So in that, I want them to think about how their actual processes can align better with the promises of sales and what they can do to collaborate.,Yep, I already have so many answers on how to fix that.,It all answers itself. Week three goes well, it all answers itself. Yeah, it's gonna be really good because I can't wait for that and then marketing strategies like whatever KPI development.,I kind of want to just get rid of marketing strategies.,I think it's dumb Right now it's just too much Seven weeks Yeah. Perfect. Then they're going to have to present like a vision deck. And so I'm going to try and get ahead. Mine's going to be more broad strokes. And then they need to get specific and it just needs, it needs to go on.,Right. So this roadmap, we're talking like KPIs, they want to hit sales numbers.,Um, what else do you want to get out of that? We need leading and lagging indicators, like goals, leading and lagging goals for every person. At least every role.,Yes.,And we need to turn that into a bonus structure to. Refinement and presentation is just like, OK. Yeah, exactly. Yep. All right, cool. Yeah, so mine's going to be broad strokes, and then you guys are going to get into the specifics, and it should hopefully align. This is going to be amazing.,I cannot wait for this.,Do you want to talk next about compensation? Sure. Which I think we're on the same page about, other than what's the findings of your bonus structure?,Yeah, it sounds like we're on the same page As far as salary, 250k a year, and then bonus structure, you had discussed something based on hitting NSMs.,What we talked about is a $100,000 bonus split up month by month if you're able to achieve zero, like no loss, no gain in any given month, which right now, like $100,000 bonus is very realistic because we lost a million dollars. So, you know, that's paying you 10% of the result there. And that's not realistic.,You will, but I don't think you're going to. I think if he just kept moving forward and implemented some of these things, you'd hit it fucking three times this year, and it'd be a fucking 25-thousand dollar bonus. But we may have to define it better. We have a fucking basically a month to do it. Yeah, and so I'm I want it to be what's our current nr You want it to be zero well or better we lost So like look Here's kind of decreased revenue, lost clients, and so I think it's somewhere in the realm of about, you know, 85%.

 But we've had months over 90. Yeah. Wait, so you want me to get it to 100?,No, wait, I'm trying to understand how you're tracking this. I'm sorry. If I'm like flow right now.,So That's just some quick books like clients that we've lost.,With cross selling and upselling, you're saying you don't want to lose any, but you lost a million dollars this year.,Basically, what I'm saying is if you can fucking keep that million dollars, we'll give you $100,000 of it. Right. Which is pretty normal. Yeah. That's what you would do with that. However, I agree that It's impossible.,Is it incremental though, or do I have to actually? Well, that's like that's what we needed to hit the moon before I get anything, you know, so Like if I saved you $800,000 do I get 10%?,My initial thing was hey, we're We're going to run this every single month. Yeah. And every month that you hit it, you're going to get the fucking $8,000 bonus. And so it is incremental. And some months, some months we just don't lose any clients. Right. And some months we lose a ton of clients. Yeah, totally. And on those months I pay you. I'm just joking. Yes. No, so I don't think it's the right structure.

 Because we don't even have a good base. I guess.,Yeah.,Like, where are we at? Like, I'd love to see how if let's just pretend I worked the last month.,tracking some stuff, but they were tracking it wrong. Okay. So new 3,000 and this quarterly retention is calculated entirely wrong because Sam made this. Because that's saying right now that you kept almost 100% of your clients.,Yes, absolutely wrong.,But how many did we actually keep?,Reality What's the real number?,Well this this was managed up until Jim So but this is on a number of clients. It has nothing to do with money. That's the thing So, how do we get how do we know they say?,Hey, we didn't lose a client and just show me like let's just say today you and me are meeting up to assess my November Commission and our inner Do we know?,Yeah, yeah, yeah, yeah. So what you would do, we have to build a tracking system. And I know how the tracking system will work. OK. But so ideally, we would go, OK, So, that in this report. So, we would go.,I can't do it because I need to find out last month's revenue on accrual. My department. So it just, it lacks the sophistication that it needs. So how we would calculate it though, and I could do it, it would just, it would take a lot of time. So I could say, okay, so this $296,000, bam, this report tells me what was there in October. There was That's a pretty straightforward number. There was 56 in October, right?

 I think this month there was, where did you go then, huh? I think you had to close the panel, close the little drop down maybe. Just hit that a little. Maybe, I don't know.,I don't know why it's showing different.,We have to assess the clients that.,All right, so all you're trying to say is you want to get it to zero loss and if I can get it to zero or If I can get it to zero, that's when I get a commission base. But if I don't get it to zero, there's nothing.,But I don't like that as much because we pay everybody here quarterly bonuses. So in a quarter that you hit twice, you get a $16,000 bonus. So that would work for us, but I don't think it's good. Got it.,I think we can do better. How do we go from 8 to 10? I mean, how do we go from 10 to 8?,What do you mean?,I don't know. We were saying 10, and now we're saying 8.,I'm just, like, getting confused with numbers. No, we're saying $100,000 a year. Right. So whatever $100,000 divided by 12 is, it's $8,000 something. Got it. OK.,That would be a monthly bonus. I see what you're saying now. So if you hit it every month, it would be worth $100,000. I got what you're saying now.,if we paid $250,000 and you hit it 12 out of 12 months, your pay would be $350,000.,Because if we hit it every month, that means by the end of the year you would have retained a million dollars.,Exactly.,And if we're not hitting it, you're not retaining that money. Exactly. So my question is, can we make it more incremental based on what was retained versus a baseline that we started from instead of just Like, if it's 50%...,Yeah, yeah, yeah, but the bonus would have to be smaller. That's what I'm saying.,If it's 50%, can I get 4K?,I think we need...,Or something like that. The baseline is...,If we had the baseline... Yeah. So I think that's what you need to work on. Let's go to another conference room, because there's a white board. Okay.,I like that you have a black Santa. Do you think he knew, like, was he joking or was he just, like, was he being dry or was he just not even, like, doesn't even notice? Absolutely being dry. I'm still learning, everyone.,He made me crack up yesterday about something. I don't even remember what it was, but I was like, is that dry humor?,It was like so funny.,And it's so low-key. It's hilarious. Dude, and he'll say little things on client calls, just so nonchalantly, and it's fucking hilarious. We're in a call, and he's explaining heroin outreach to people. And he's like, well, let me say a question. In life, you know, um, you know, what is this? It's like, no, it's like, uh, we'll have, like, Gary Tunker from DMRA. And he's like, yeah, it's an indication of a fucking, uh, you know, mental disorder.

 And it's like, blow right over it, but it'll say something fucking hilarious. Really? Super smart. Yeah.,And no one will understand. They'll understand what it's explaining.,but they don't catch the joke. Something was a sign of a mental disorder.,Were you just like dying on the call? That's so funny man.,He said he said people that that's where my wife went to recovery where new life spirit bottom right kind of So, here we go, you've got SEO enjoy you need to know You have no associated directories. So you need, so you got T, no one to process or upsell. And then you have A and one, you need to know client And then you need to know their revenue. For all of their clients. And then you just need the tokens, right?

 Yep. Any day, right? So this has to happen every month. Yeah. So, um, so that's, so like Veronica would be an account manager. Yeah. This will be like starting. That's a calculation, right? Yeah. And then here, Is the new month? Yeah So nrr Equals Uh starting revenue Minus loss. So that's generally what it is. So you need a monthly total of everybody's clients, how much they're paying, you need to know if that Changes and win.

 Mm-hmm And we have like are you in a HubSpot? Yeah, so I'm going to have Some of this data is like pretty close to your fingertips cool But it's Seth's job to maintain this data in there. Okay But what doesn't show on here? Is that ad spin lineup So it's quick, you know, it's hard to pull all this together.,Yeah.,And like the changes that happen in the business in real time. Right. Like, so if you go into reports, let's go to dashboards, type in a name. So let's think of an SEO person. So Krista, so Christa cool. So let's go day range last month. Okay. Well, that does not work. Oh, I think the date range is all time probably because you have some advanced filters on maybe.,Nope.,Oh, delete it.,There we go. That's what it was. No. No, it's not. What? West 365. So, this one, she Basically lose anyway, it's churned but it's actually an upsell But it's not perfect but so these are active though But I think it's filtering on closed state so if client predated that which I see a,running history of Wait, so we have no history of legit NRR tracking. We have no idea then. No. Got it.,Yeah. Yeah. All right.,Well, I guess I'm just like scared to like build my entire commission on something that we know, like it's just like pie in the sky, you know?,Well, we have no idea. We do have data on it, because it's just revenue retention. Right. It's just not the net, because we're not tracking cross-sells and upsells. And honestly, it's no one's job. Nobody owns that tax. So it's your job to make that people's job. So right now we have So here's the thing like I can I Could start training people on how to do that.,I can start making it happen How do I know that I can actually fill that gap by with the cross selling it up something? Like how do I know there's that much available?,Real estate to fill a million dollar gap That's a big gap, you know Absolutely So the million-dollar thing we know how many how many clients we lost like yeah when we lost them As well as it should have been now they do it on a monthly basis Seth has to be with Jordan to make sure that his HubSpot data is His accurate, so let's go just to There's a question Create a report.,Yep.,I think that What I'm gonna be bringing to the table isn't purely based on an error and isn't purely Benefiting the company through an error. I think that's a big part of it. So but I think the NSM's You could say are 50% of the value that I would be helping with drive web support don't you think?,You can close this little box. No. The NSMs. Because if everyone's hitting their NSMs, that means They're not gonna, dude. They're just not. But we could probably get 80% of it.,Well, that's what I'm saying. 70% Whatever, I'm not saying hitting all, but I'm saying like, if we're doing really great compared to how we used to, that's a huge leap forward for the success of the company and the ability for it to scale.,But if I'm gonna pay you a bonus, it has to be relative to something Monetary target that I can track. No, I get it. I can't be Can't be something narrative-based thing Right, like okay, so let's say We want to make a hundred thousand dollar bonus for this man We want to represent a million dollars Yeah I understand what you're saying And I'm,not saying- I just think that positive NSM growth, if you're hitting like 80%, like a majority of 2025, that's actually gonna look like a huge dollar amount to you that may not represent NRR. It may look like- How does it not represent NRR? It may look like new client, it may come like by word of mouth, it could be like all kinds of stuff. You know what I mean? Like if the departments are performing better, we're gonna be able to sell in more I'm actually going to help incoming sales grow and happen.

,Absolutely. And I want to compensate you for that. Right. But I'm not looking for that as the focus for you. Okay. Not that I don't think it ever could be or should be. Okay. I've got a big problem, right?,Got a big problem.,Yeah, and that problem is not in the sense right and so the reason I started looking for Somebody to fill this role was because I was starting to try to implement nsms Yeah, I was starting to try and you know figure out how I get from where we are right now Revenue retention and I want net revenue retention to be our North Star metric and as an agency. So I figured a head of ops, which you want to be COO, great.

 But that means that at some point, there's going to be somebody doing what I need you to do right now. And at that point, I think you go all over the sales. Where? I guess that's where Sales is an option, but it's not the low-hanging fruit right now. It's not the priority.,It's like all of our sales are less valuable.,And so I don't want to bring in the biggest business that we possibly can and just fuck it.,No, I get it.,I guess I'm just like, um. Let's see what we can do in a month. Yeah. And, and how, how well we can define it. Totally. If we have a system for tracking NRR, we can fill that system in. Yeah. Six months back. Okay. Got it.,Yeah.,You can backfill the data. Yeah.,We might, we might miss several things, but we can at least get super exact for last 3 or 4 months. And then NSMs are a tool to help you increase NRR. And NSMs are a tool for Mitch. And if you can help Mitch do better there, you're going to get closer to your goal. Yeah, I get it. I totally get it.,I disagree with you, but I don't want that to be your job. You don't want it to be my focus right now. It should be part of the focus. That's why I wanted to have this convo.,Understand like What's gonna What's gonna tell me if I if I succeeded mm-hmm in 2025 is Is if we're able to roll out robust and our tracking mm-hmm and we're able to make progress on it Yeah I guess the,issue I'm having is I genuinely feel like I could just be doing way more for you. I'm worried that I'm going to be underutilized. And that's genuinely how I'm feeling. I'm worried that... Well, let's just check the boxes. Yeah, we'll just do it.,And then let's get you doing that well. Then let's hire a fucking head of ops.,Sure. Yeah, yeah. Slip that in person.,But it's really, really important to me. Yeah. And so I don't disagree with you. No, totally. I want you to bring all of your experience to the table. Totally.,I just like I have a ton of experience. I know I'm expensive and I just want you to get like everything you can out of it. That's like my whole goal. And so if you just want me to like bore down on this one thing, like I'll do that. You know, I just I feel like there's other things I could be working on at the same time is all I'm saying. But maybe that's not true. Maybe I'm still like out of the loop and not totally understanding everything and maybe once I get in the trenches like there's a lot more to it, you know, but So like maybe I'm used to being overworked and You,should work with Shannon to roll out new services. Yeah, totally. Yeah, cuz you're gonna be hampered and you're fucking in our focus, right?,because I'm seeing all these opportunities.,But you're going to need those opportunities to hit the goal, won't you?,Is Shannon one of these NRRs we're tracking? Does her department fall into this?,It is if we get recurring revenue. We don't have recurring revenue in design.,Except for a couple of these little web maintenance packages.,Yeah.,So here's the issue that I'm just talking here.,Yeah.,I'm gonna help Shannon to just a freaking blow out this design department and it's gonna start cranking out a bunch of money Yeah, but I'm not gonna get bonus on that like absolutely it might help the media the paid media and like help them improve their innards because they have better ads but like No, we're gonna do way more than that.,You know what I mean?,We're not getting paid for that Well, we need to though.,We're gonna start getting paid for it But how does it not show up on It's not recurring like you said though, it's like you just told me that.,It's not right now.,As soon as we implement a CRO service or an offering, it has to be recurring. Otherwise, I don't want to deal with it. Not necessarily.,Like the web design stuff, that was a whole other conversation I wanted to have with you about that. I think you're way understaffed. Charging for web design.,I think we could be doing way bigger projects. I agree. I agree with you. But the net retained revenue is only a measure of recurring revenue. So if you work with Shannon to roll out a service that's converging So it doesn't have to be that like that was for social media. This is for advertising. You don't need new ads every week, you know what I mean?,So it may not be recurring. You might just make your ads and they're going to work and that's it. And you maybe revisit them in six months, you know? Okay. So I'm not trying to get in the minutiae. My point is, you know, Well, your point is you're saying it's all going to fall into NRR anyway.,It doesn't matter.,Like, cause it's a cross sell. Like my point is, is what if I help Shannon win a $30,000 website deal? And it's like a two month project. She makes 30 K. What if I land like four of those in a year? And I'm like, Hey, I made you a hundred grand on these websites, but I'm not like getting bonus on any of this stuff. Cause I don't know. I don't know. I don't know. I'm only getting on record revenue.

,You know, I mean like am I missing that is it my off on that? I Think a little bit because Just so you can understand like why we sell websites for what we do. Yeah is It's not necessary that it's like the right thing or whatever. It's because what was happening, we used to have four designers. And we would sell $60,000 or $70,000 in a month. Then we'd have two months in a row where we sold $20,000.

 So over the course of a year, but it was up and down and up and down. And being that the rest of the operations weren't super tight, the end result was like wild slings. And so what we decided we were going to do do is make the website design department as small as possible. And again, I think we made the wrong decision, but that was the decision that we made. And so that even in a month where it brought in zero dollars, which we wanted to avoid and we did, this year there was maybe one month that the web design department It cost us barely more than we made.

 But it used to be that at least four or five months a year, we were spending more money than we made. Over the course of a year, it was always a slight winner.,But this year was more predictable. We made money every single month except for one.,It only made 400K. We made more than that in a year by a good amount before. Okay, so I guess what I'm realizing, what I'm trying to say is I'm a little bit siloed in this NRR thing.,Sorry, if I'm being like annoying, by the way, just let me know. I don't think you're siloed.,So hear me out.,I'm siloed into NRR, but if you're going to gain $2 million in revenue in the next year, that's like huge growth to the business that I'm responsible for making Yeah. But I'm only like siloed into this NRR thing.,Does that make sense? But NRR is the whole thing. We want recurring revenue across the organization. That's our lifeblood, right? Yeah. So if you rolled out a new design service, I want it to be recurring. Yeah.,What I'm saying though is I'm saving you the millions you would have lost, but also the company is able to grow the $2 million on top of that.,Am I off on that? No. Okay. But the $250k is for something.,Sure. I guess what I'm saying is, I feel like this bonus structure works better for a I think it's wrong.,I don't think we're in the right bonus structure necessarily. OK. Yeah.,And so then I was like, well, just now I had this idea. Well, because the deal is, is like, this is like my seventh agency I've been in now, right? And so it's like, it's my first. But you've been grinding at one agency for a long time, whereas I've been jumping agencies every two to three years, you know? So. Yeah. My point is, I wanna feel excited about the whole thing, growing the whole thing. I wanna be excited that three years from now, we've added 15 million in revenue while I worked here.

 And I don't wanna just be like, oh, I'm only getting rewarded on NRR. You know what I mean? That's my only point. And maybe I'm talking way too big and far down the line, but I'm just like,,So the reason that it doesn't matter that our sales team really well, it's because we can't get this right. If we can get this right, we can move on. I'm not tied to your focus always being NRR.,Okay, so that's what I'm saying.,The whole service side of our agency, I do think their focus does need to be NRR. Right.,So here's my thought, is why don't we... I will focus on NRR, believe me. That's my But like, what if we back off even, we can even back off the bonus on that, but I want to get bonus on overall growth too. And like performance of the company. Right.,Because like, how do you think we do that?,I'm trying to think through it right now. I'm literally having these ideas as I'm talking to you. I don't, I don't know.,I'm just, I'm like just now even understanding what it was that we were doing. So $9 million. That's that's. Uh, ARR. Mm-hmm. That's Michael. I'm totally happy to get bonuses on what our website Yeah, my point wasn't even the website my point was the overarching But the way that we grow mm-hmm is by when we add one client, it's there tomorrow. Totally. With websites, that's just not the case. So do I want to sell bigger, better websites?

 Yes. I've sold a $100,000 website before to a big fucking multi-billion dollar company. Yeah. I get it. That's great. We're not even good at pricing that out, scoping that out. Right. Do I want to be better at scoping that out? Do I want to be a better fit for those people? But the way that I see the websites is as a way to bring people in. It's another capability that can get somebody into a recurring client.

 So I just don't think it serves our long-term interest unless it wants a segue.,So how do I get a bonus on plus growth? Like, for example, you're bonusing me on what you save from a baseline. Like, you just got done losing a million. And I'm hopefully going to recover that million for you over the next year. And you're going to bonus me 100 grand, like, just in a perfect world. Yeah, yeah. And then, but what if, like, what if I also Help the departments get to a place where they could actually take on another three million in revenue over the next year.

 You know what I mean?,So it's like I'm only being bonused on like the Saving of money not on the actual growth potential of the company Yeah, so that's all I'm saying. Let's talk about it though.,Yeah, so In a scenario like Uh and by the way, I just I want to say first of all, dude, like I had a conversation with a friend of mine when he joined my first agency that I built and he wanted like equity in my company and He wanted all this stuff and it like really turned me off and I ended up actually having to fire him and so I Don't you know at all feel like I'm Pressuring you trying to take advantage of you I don't think so.

 I don't at all. Okay. I agree with him. I don't want any hard feelings here. I'm a hundred percent just trying to share my thoughts. That's all.,And I want the company success. You know, that's like literally my main goal. Okay. So I need this person, right? Who is P stands for person who is in charge of any, any director that provides services. Yep. So, you know, maybe at one point we'll, we'll grow really big and let's say there's a finance director, uh, people ops director, uh, there's, you know, um, uh, marketing ops director, there's a sales director.

,This person that I need doesn't come over here, right? And this person needs to focus on NRR because I want these people focused on NRR. And so it's not that you have to be this person forever, but that's the person I think I need.,Okay.,So here's my, here's my thought though is like why can't we have that like this is me yeah and I'm here yes and I'm fixing all this but while I'm at it I'm not only keeping them from losing money,like these guys are all losing money yep I'm keeping them from losing money but actually sales is over Sending money to Jordan. And if I don't do this, those sales can't keep coming in because we're doing shitty work.,And like all this, but I'm only getting bonus on what I say to you, not the upside potential of all the new business that you could bring in.,Right. Fair.,That's what I'm trying to say.,However, Okay.,Again, I could be like totally brain farting at home.,I have no idea. We can still bonus this person on that stuff. Okay. Because if NRR grows, like if the total dollar amount of it grows. Yeah. Like say it goes from six to nine in the next Zero becomes more valuable, right? Because like, so NRR, if we retain 94% of it, 94% of what? Is that 94% of January's revenue or December's revenue? 94% is now, because that's really what I want the company to hit, right?

 Yeah. People on 12 month contracts, so that any given month 10% is up for renewal. Right? Yeah. And I want to win 70% of those renewals. Yep. Right. And so cool. We If we win 70% of the renewals, then everybody should be happy. But if 94% right now is, what's 94% of 500,000? It's 30,000 months, it's 470,000. So if we retain $470,000, that's great. But if this becomes a million at the end of the year, that's worth $940,000.

 So there is a way for us, if we can track this, to say that, We'll give you an 8K every month that you have it be zero. Plus, we'll give you 1% of the NRR growth, so long as you hit certain targets. Okay, what's the growth here? It's the growth of 470. What's 1% of 470,000? I don't know if 1% is the right number, because...,I get your point, you're just saying for sake of argument.,But we can, we can bonus. This is awesome, that's exactly what I was asking for.,Yeah, yeah, yeah.,It's just, if it's...,But we can't bonus on it if we don't make the... No, I get it, I get it. I totally get it. And also, if our NRR isn't doing It's not gonna work either. So like I get it. Yeah, the the deal is is I just don't want to be like capped anywhere I want to be like, let's go to the moon. You know what I mean?,Yeah, so that's all yeah, so But yeah, some kind of situation like that is exactly what I'm talking about. That would be awesome. Yeah, and so You know the the role is really It's a head of officer. Mm-hmm doesn't mean that You want the COO title, you get the COO title. Doesn't mean you can't become the COO. I need the COO. We're gonna call you the COO, but I need to get to this, right? And then from there, we can recruit the right guy.

 We can probably pay that guy less than you. We can probably pay him $130,000 plus $8,000 a month.,Like, here's my little, here's how much time I have Months right yeah, so like As far as like what I can tell being with Mitch meeting with Trevor being with Shannon if you're going on Here's my 100% maximum workload potential Based on what I'm hearing if this is literally all you want me to do Like we're right about it here cool and what I'm saying is There's still this little area of like what do you want me to be working on and I want to get bonus on that and so that's where this comes in it's like hey I don't want to be thinking a holistic approach to the entire company because sure I can just do this but it's like you brought a Ferrari to a uh snowbox race yeah yeah it's like yes I get that the Ferrari's going to win but it's like how do we maximize my time so I'm like yeah yeah I So,,I don't know if you're right or wrong Well, I don't have any wrong it's only gonna benefit you Because you don't pay me Yeah, it's I just want the ability to hit marks.,I don't want the marks to not exist so Okay, but here's where I'll all ties together.,If we make better service offerings, when we use Laurent's help or anyone's help, I just want to make the best in market offering for everything that we do. And if we make those, the sales conversation becomes easier. And I do think for the entire life of the company, we're going to need this person. We're going to need this person until they have 20 direct reports. They may never have 20 direct reports.

 However, that person's needed.,I just think you need to understand, the last company I built, we scaled it for 1 million ARR in three months, and I hired 60 people. I had 60 people in that company in three months. That's what I do.,That's what I can do.,We're gonna do this, and it's gonna go way faster And I'm just saying, like, I want to set the limits of potential really high, because I think we're going to go way farther than we think.,That's all I'm saying. Yeah. Well, the other thing, too, is me and Kyle are open to equity, to all of that. We just didn't want to define it before we have a good working relationship. And I'm not trying to ask for anything up front.,I'm just saying, if we hit number, let's just, in imaginary land, if we were to hit certain things and I'm having a more holistic approach to everything, how do we structure that? How would we structure that? So that's all. But I like what you were saying here.,This makes sense to me. So I like it. Yeah, so as long as we can get the recording, We can go back in time. And then we can have a baseline. And then we can say, okay, here's the sales, new sales that we brought in on a monthly basis, like for the last nine months. And if we average that out, it's this much per month. But in the first quarter, it was this. And in the last quarter, it was this. And so here's how it's growing already.

 Without you doing anything. And I'm just, I think you'll bring tons of value to the sales department. I just don't even want that value right now. Because this is going to be a heavy, heavy lift. You know, people are not going to need to get fired. People are going to need to get promoted. People are going to need to be like, hey dude, this is not your job anymore. This is your job now. And it's going to take a lot of organization of what we have here.

 I totally get it. We've got a lot of good people.,Well, I usually, I usually, oh, what's that?,Oh, yeah, it's over.,Yeah, I'm not going to have an issue with that stuff. Like my, in the past, my issue is not like doing all that stuff. My issue has honestly been usually steamrolling people. And pushing too hard. You know what I mean? And so I've had to reel it back over the years.,That's good. So we're going to get it done. I'm a little, I'm a little too soft. And I'm often in my own world. I get a lot done, but only under certain conditions. And I like exactly what you presented there.,So if you want to just out what that percentage looks like, That's all I need to know.,Okay, well, you know, one thing I like to do is make OTE, like, okay, what's the goal? And how much do you want to make in year one? So, if I don't want to cap it, because you can exceed the goals. Never put a cap. Yeah, like What I shoot for I make an MTE is a 64 split so 60 40 and 60 of it for pay as salary 40% of it Okay, if we can agree that this is what the company needs and this is a real estate target for you, then figure out what the number is.

 Let's say it's $400,000. This is Paul's OTE. We missed the mark a little. It's not 60-40, but that's his OTE. If he does that I get 2.3 million in bookings. So it is what it is. It's based on percentage.,It's 10% of whatever is retained. Is that what you're saying? Or what do you think? Our actual goal as a company is 94%.,That's what I want to get us to. So let's say you hit that. Maybe we bonus you on something else. Maybe that's the true false if you're eligible for the bonus. And maybe the bonus can be based on just the revenue. Like the actual retained revenue. Not the percent. Mm-hmm. So maybe hey just qualify for a bonus We need this and the bonus is some percentage of that revenue.,So I was thinking yeah, and what if we did a baseline like in other words Yeah, that'd be cool yeah because if it's a hundred grand Then it's 10% of 100 grand if it's 50 grand 10% whatever.,It's just flexible So here's Kevin's, which is...,What am I looking at? Kevin. Who's Kevin? Kevin Hall.,Yeah, that's over there.,Oh, Kevin! Okay. Got it. He needs to drag two million bookings from all of our markets. I thought he was in sales. I thought he was in...,He doesn't. Oh.,But he just has the ability. Okay. Marketing. Marketing. Generates leads. Got it. Okay. He gets meetings on, on Kim's calendar. Okay, cool. Uh, thinking about pulling away from that and doing ops. To be honest with you, if we built this out okay, he would be perfect. He could be that guy. Exactly. He's super smart and he would be very, very good. And he would be thrilled with it.,I feel like I, but the thing is, I want to give him sooner to start training him because he's going to need a lot of like leadership coaching and stuff.,Absolutely.,But the, because if you just airdrop him into that role in like a year from now, like he's not going to have a lot of the skills you need. Like he should start being involved on a small level.,You know what I mean? Yeah, yeah. Thanks for talking to me, Alice. Look at this.,I don't really read it.,So they have the marketing ops office.,What if we put him as Operations Assistant or something like that and we start getting him like involved in it, you know what I mean? Or like associate operations, I don't know, just sit in it. Or even like just a sub role. Associate director of ops.,Yeah.,Yeah.,And then I can start training him and all that stuff.,And I can bring him into the meetings.,And he already knows about NRR, he already knows about where the data is. He beats everybody. He's super legit. Yeah. Plus then if he gets good enough, just fire my ass and just put him right there. Well, there's, there's, I mean, yeah, I, I, um, and I've already been thinking about, about like the, The frustrating position that Kevin must be in. But I already have him doing a lot of the product offering piece.

 But he has no authority to bring it into the mix. So that's why we need to work together.,I need to be working with him.,That's what I'm getting. Yeah. I love that. Yeah. So really good. I like it right there with that.,So cool.,All right, so good.,What I'm thinking about is trying of figure out the right percentage.,Yeah, because we don't have to figure it out right now.,You can just, well, it's just, it's hard to get these things right. Yeah. So we got to get the NRM tracking in place. That'll be a, yeah. And then we have to do the strategy for the sprint. We'll get through the first couple weeks of it. Yep. But you guys should be working on in our dashboards and what you have mm-hmm is You can get Seth handling any data related tasks Cool, you can get Kevin sweet handling Yeah, so Seth reports to Kevin okay report to Kevin for data as well And then charge of marketing, but we're going to pull them into op stuff now.

,Yeah.,Can we go ahead and like talk to him about that and get that cranking?,Yeah, I've already talked to him about it, but I told him I was not sure that he'd support it. Yeah. So that, yeah, we can, we can get that cranking. I'm just going to lunch. I'll be back. All right. Remember your values. What? Remember your values. Remember who you are.,Are you I'm curious what you see me doing here like after we get this inner our thing figured out Well like what's your Let's just say it takes a year. What would you see me working on after that just out of curiosity?,Well we are gonna need to grow and scale the agency And Mean there's there's We're going to need traditional ceo part of how we're going to grow we're going to grow Valley finance internal we're going to Continue to Try and drive the ship and Cool So I mean Well, how can I get annoying to you?,because I just I don't think I'm full of ideas and I always want to like put my hand in too many pies you know and so if I'm ever like working on things you don't want me working on just,tell me you know I just want you to focus on the things that are gonna make the biggest difference first I will and then on a percent and then so like this this person is responsible for Maybe in collaboration with with some others like video video could be huge for us If we get it right And I know how to plug and play it right now, yeah, I'm just gonna recreate vids within web server Same exact thing and sell it fill it in So we just want to make more money.

 So we've got a cool platform. Totally. I'm all about the money, too. That's what excites me at the end of the day. Eventually, we would want to probably make a new methodology of how we go to market around a medical device. We've already had some success. Our LinkedIn strategy could work way better than it works in behavioral health. But I have a hard time going to these people and saying, hey, we're even remotely close to the best.

 So behavioral health has been pretty cool because I mean, our competition sucks. The SAS guys. So I want to fix our problems and be the best offering by miles. What's your long term? Are you just trying to get it to an X number and then sell it?,Or what are you trying to do? Not really.,Just keep it cash. I'm talking about an acquisition potentially. I have some experience with that like that's in Bastion.,That's how we Partially how we got to 10 million. Yes, we bought agencies. We bought like four agencies Either one I'm just saying I'm just saying it's a cool way to just add two million dollars like overnight like all of a sudden like And you've got more team members and more resources and,life. It's pretty cool It could also be rocky culturally, but yes Get through it so Yeah, I mean that's that's yeah, what do I want to do this year?,Yeah 10 million in two and a half years. I didn't mean like, I didn't mean that 10 million was like this like amazing thing.,I just meant like we did it really fast. Yeah. And then I want to get to, I want to get to 20 million. Yeah. And then potentially sell it or something. I don't really have a goal to sell it, but we have a billing company. We have a marketing company for behavioral health care. We have behavioral health care companies, and we have a software company for behavioral health care. You guys are doing so much.

 That's awesome. If we were to sell, we would say, hey, we have a platform.,Of all these services.,And we'd want to combine the whole thing. The billing company will take way less time to get to 10 million, but by the time they get to 10 million, we'll probably be at 15 or so. So let's say we had 25 million in ARR between those two. The software companies, I mean, it can grow huge, but we got to get it off the ground. So we've got a couple beta users and we plan to go to market with that in February.

 Nice. Which is cool.,Is that what Kyle kind of is helping to lead or?,Kyle helps with that a lot. But Kyle runs the billing company.,Got it.,So the billing company is great. It does well. It makes money. And it's still not that big, but he grew up a big billing company. They merged with another billing company and sold a product of private equity and they couldn't do billing for like three years And then once in three years was up. We started another one together. Wow That's so cool. So yeah, that's that's kind of Kyle's wheelhouse. Yeah But like the things that we're doing here with Claude you guys are like amazing man.

,Hey, you're just like you're just doing these things and just freaking grinding and I Killing it. It's like really cool.,There's something to it.,Like we believe that um I just feel like there's something you guys are doing that's unique to a lot of people and I'm not sure what it is yet well, but it seems like you guys have a A way that is unlike anyone that i've worked with so far and I have I can't really figure out what it is exactly but house seeker's park in his wood.,He's kind of a bad cop, I'm kind of a good cop, but we both bring kind of different things to the table in our park. But he doesn't That's fine. It's still not working. Do you want to get Kevin in here now?,quick powwow with him?,Yeah. I don't know. He was earlier. Kevin, do you have a minute?,The figures that. Right out of all of our programs.,That highlights something so big. What? Well, our clients, they want VOPs for about eight grand. And the real world cost across a huge data set is like $50,000. Wow. And people aren't really doing much better than us. Yeah. Our clients can go to a different competitor.,So I've been making this, essentially like I gathered all of our data from our PPC team that they've been tracking this year. And there's some clients that didn't have it, but so from like a month to month basis, we can track all this information. Like, you know, the calls are getting BOPs broken in a lead stage, the cost for each of those. And then I had this data set here, which is just, you know, tons of shit.

 Then for clients that were missing that I don't, you know, either the new tracking sheet hasn't been adopted by them. I just used essentially just chat GPT. I just took the CSV and told it to like analyze trends based on like spending. And so now I've added all these like predicted analysis of what we, what they could expect. And that'll give us a rough idea of this guy.,Dude I was just telling him like how much I love you, and I've only known you for like 24 hours Because I think I see it I just is that you, Devin Hall, know the most about how things are supposed to work, you know, more than the people that are doing the work, how things, how WebServe wants things to work, you know, what we want to become. You have the best grasp of anybody on what that is. You have essentially No real authority to Implement it.

 Yeah Obviously we're doing Marketing with interactive. There's an opportunity to take over to have them take over marketing option for way less than cost. Yeah and Beyond that you've got this truck in and what, like this goal that is real, but at the same time, goal, meaning you're OCD. You're, you know, what is it like 235 bucks? That's a great sound. It's like 235 bucks for proposal called health.

 That's how it breaks down. But there's so many things that we could potentially do better. And yeah, so I was meeting with Jordan, because I was like, okay, you've got a sales director, you've got maybe a finance director, people operations director, marketing operations Jordan's thing was like, hey, I can do so much more. This was Jordan's time, this was like having compensated for that. This is where I can extend.

 But anyways, what I was getting at, is what we're trying to do is give him a compensation structure. It's like, okay, you can get us to retain 100% of our revenue from a month so that essentially there's zero loss. Yeah through cross-selling upselling and better services then the opponents on that he said well I I can do so much more than that. I was like well this person that I was hiring for what I was looking for was a like director of ops and So these are our service directors these are you know Trevor, Mitch, Shannon, essentially.

 And if we added more services, this person's job would be to manage those people, right? And I was like, look, this is what I need. This is what I'm hiring for because I need to solve these things. So you've got Seth. You've got you. And we've got Jordan. And so, at least eventually, this person, you might be a better fit for that role long term. So the way that we see it right now is, Let's say the Associate Director of Ops that could potentially be part of Dog Mountain.

 KDF. And KDF could lock down the ops here and then in the capacity of COO, JD is the third, and can then become BAM, BAM, BAM. But really what we have to do is we have to, my vision is that we're going to template Not template, that's not a good word, but standardize our delivery so that it can be talked to anybody and that everybody agrees it's what it is. So Laurent and Garrett say, oh, I want to be blameless in disciplinary actions, whatever, because everybody knows everything.

 Everybody knows where everything is, and they didn't do it. You know, it's not my fault they're an idiot. You know, without blaming us, right? So you're fired, and it's your fault for being an idiot. It's not my fault for, you know, whatever. But anyways, it's not my fault you're an idiot. It's what? What uh they're getting at there but uh anyways uh yeah that's really yeah so basically what are you thinking is backfill the marketing side of things with what directive is offering for 5k it's honestly closer to what you're doing anyway you just don't have any authority yeah yeah It's like Kevin can't be that effective in what he already does because Kevin It's not respected as oh Kevin's the one that makes these things and Works with me to make sure that they're implemented across the board So basically the vision is you?

,work really closely together to roll out and our optimization tactics with all the department heads. And then you're there to help me develop it. We're going to work really close together. I'm going to be like heavily, heavily involved in making that happen, but I'm also going to enforce it. And then you help me with that. But then it also allows me to keep a more holistic approach over the rest of the company.

 Obviously our first sprint is going to be to solve that NRR issue. I'm not going to really, like Crescent doesn't want me to focus 1% of my energy on anything else. So we're going to go full bore on that. But this allows you to start getting in the trenches on the op side and like understanding how that's working. I'm going to be coaching you a ton because you're going to need leadership coaching on how to run these directors and all this kind of stuff.

 So I want to start getting you in there. So that then I can once we do solve the inner issue whether it takes six months or 12 months or whatever you're able to keep running with that and optimizing during that but I can also focus on other departments,too you know so that's the thought yeah I mean I think Preston knows from the two well three years I've been here I've certainly complained a whole lot about meeting operations so I'm very much And, you know, as much as I've tried to, like, slowly do things, obviously the issue of not having, holding weight. So I've always been on board with bricks, and I'm glad we're finally moving towards it.,So I think, you know, in terms of- I'm glad we somehow made it through the maze and came to the same conclusion. Yeah. That's awesome. Yeah. So I'm all for it.,I know there's, you know, there's certainly a lot of, like, response that are going to be outside of operations that realistically I probably still have to do.,Well, the thing is, that's why I say I'm going to be ultra heavily, this is going to be all I'm doing. It's more like, think of it more like you're almost shadowing while we're doing this stuff and helping me with certain things. But as it grows, it'll grow for you too. You know?,You know something that I've thought of No, because I'm not a mind reader.,is we can operationalize.,I told you about everything we have going on. For the billing company, if we share a client with the billing company, which brings us $10,000 in revenue, the same client brings a billing company like $40,000. But we haven't discovered Is it because you feel like it dilutes the authority or something as a billing company? Or like what do you mean? No, but it would be worth talking about because if you think about the platform that I described to you, which is software company, billing company, marketing company, the whole thing.

 If we can convert web serve clients to billing clients, I mean, I can get tens of millions of dollars from the same people that bought the company. Maybe even a hundred.,Let's freaking do it.,If we could get every single one of our clients to the billing company, I could get a hundred million dollars.,So why aren't we doing that?,Because I love marketing and I fucking hate billing. Well, don't we just send them over there?,We don't even have to do anything.,We just sell it and hand it off. Yeah, but it's worth not focusing on right this second. Okay. But it is... I don't know, I feel like a hundred million dollars is worth Because like, let's say their average client's 30k. We have a hundred clients. And,Do they always go on two and a half hour lunch breaks? Yeah. And who was it, Kim?,No, it was like Mitch, Fabi, and probably the other guys.,They normally don't. Most people eat lunch here. Fabi lives in Mexico. Oh, got it.,These people that are here. Just holiday vibes.,Yeah.,So they flew in from different places.,Got it. I'm not trying to make a big deal out of it.,I was just curious. Oh my gosh. That's good. I don't know. Like our clients represent like a hundred million dollars in EBITDA. That's crazy, bro.,What the heck? Great.,It's insane. But, uh, We've got a team of 100 people in india because it's pumpkin nothing.,Yeah Wow, uh, and what we get that's insane bro.,What we get Is between six and eight percent. It's commission based six and eight percent Of our collections. Yeah so For a big client, it's closer to six. Sometimes as low as five For a small client. Yeah, it's a We're redesigning the UFO that's a UFO with a raindrop spout for showering cows before we abduct them? Well, these are the line drills. So that's you, Shannon, and Trevor. Because basically, Jordan was like, well, I don't just want to focus on ops.

 I bring so much more to the table. And I was like, well, this is what I need. And then we got into the weeds a bit. This was his actually. But this is what I think it's going to take me. What do I do with this? You like it? See what I did? Receipt.,Look at that. No, it's a test tube.,It's like a... It's definitely a wiener. That's a sip. Snickers bar.,that's not like there's there's a ton of stuff that could be excluded and just quickly put together well all this all this yellow shit was like no one keeps track of this data so I went in and Essentially like it's all a predictive analysis of like potential so it's certainly not perfect But it's uh, it's our best we can do right now all part and you know, it's really a Yes, yeah, that's not it's not the best in the world but for what the data we have But I think with closer outliers, I should be closer to like that 14K per admin, maybe less.

,I just, there's a bunch of you.,All right, that's all you need me for, yeah? Am I good?,Am I free?,Am I staying?,Am I going? Do you like it? Is it interesting? Yeah? All right. What is this little stuff? Thanks for the ornaments on the tree, a little glitter.,Here's a rock for you. A what? Rock.,Glitter rock, but right now I'm looking at glitter rock.,This is pretty difficult to get it off.,It's working. I didn't think about that until I had to get my head in.,Why aren't you guys watching your hands off like that?,So we touched the glitter. Oh. We touched the rock and didn't work.,The glitter cracked rocks. Oh, thanks. OK. All right. Thanks, Ken. Yeah. Thank you. Should I should bring my computer in here?,Yeah, whatever.,Do you want to stay in here and I'll go over the other one or what do you want press?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah I already told them we're good to go now thanks Preston

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome! Strange some channels aren't working. There may be a workaround if you can't get it to work, lmk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Slack support might be able to help export it for us?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Haha yeah sleep is important

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: They just may not need a laptop is all

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Whatever you guys think is fine

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Like Tech stipend as needed or something

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We could keep it open

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Thanks for putting that together.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: This is great! Awesome job

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool! Can you guys both use the same PTO and Holiday sheet that <@U083E324RCL|Julia Gumeniuk> made and just add separate tabs for the link building team/ That way we can keep it centralized. thanks!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: There's a lot of slack apps out there

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or maybe there's a tool that can connect to our slack and grab the info

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Great question Aleks! Let me consult Preston on this and get back asap

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: But if not doing challenge then not as big of a deal

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome work

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: When you get to the point that you need to email people and move them into new sections let me know and I can send a loom on how to do it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We will need the emails templatized if we plan on doing the challenge so you can send it out to all the hundreds that apply

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah I think...I understand what you are saying. Fine with me

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah that sounds good! I totally trust you. Thanks Julia!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You too! Have a great Christmas!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Curious how you felt people handled it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you think the challenge worked ok before? Or do you want to review it again?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Lmk how I can help on this

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: If you get time we still need to finish instructions for Aleks: Otherwise who knows what she's working on... ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: If you get time this week could you explore this tool? Might be helpful, possibly better than Macaw too. ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or not showing up at all

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is it showing a message?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you send a video recording of the whole process?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hmmm strange

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is that something you could do?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Also this one: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: That sucks about LAX!!!!!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just working to keep Alek's team on track.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok gotcha, I didn't realize that was the. hold back. No worries!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is there a way to buy more?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maybe the 10k applies across the whole team, not 10k per member?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Have you tried support?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hmm

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Idk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can go in and take a look for you

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I get the login again?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Looks like you were on a personal plan and I moved it to a team plan

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hopefully that worked if you want to have them check again

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you show me what it shows here on this panel on their end? (when you click the profile image)

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: could fix it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm just wondering if they are on the personal account by accident and not the team account

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What you might try is removing them from the team and then re-adding them

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'd say next step remove and re-add

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah really strange

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Possible support will respond after the new years

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maybe they can share logins in the meantime?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Question - seems like paid media team is really busy so they quality of work goes down. The new hire should help this. But long term, why don't we use offshore talent for the day to day account optimizations, and then account maangers are only responsible for oversight, reporting, and client facing comms?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey hope you had a great Christmas

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What if we did this:
1. Hire 1 offshore Digital Advertising Analyst
2. Task them with:
    a. monitoring data, checking conversion logs, updating performance sheets, aligning call tracking.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: But would come with expectations that the AM's NSM's rise

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: They could probably do this for 2 AM's. This would free up some of the dead time they spend on that so they can focus on quality account setup, and better overall management and decision making.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok that's great. If they can do all of them then that's even better

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Salary for average analyst we could probably get under $1500/mo

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And then analysts focus on:
1. Data alignment
2. Sheet updating
3. Account analysis
4. Consulting AM for changes/recommendations

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: My goal would be that AM's focus purely on this:
1. Overarching decision making
2. Initial account setup (following best practices)
3. Client facing comms
4. Reporting (so they know their numbers)

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think that $1,500 allocation will result in a significant rise in NSMs and client retention rates

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maybe if you can lay out a bullet list

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: (Considering that we could have good documentation and training in place).

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What I would like to know/do is find out what task items can be done offshore, and what is necessary to do onshore.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I just got done hiring 8 people for the seo team

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Probably in Serbia or North Macedonia

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We would only hire someone with good english

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If time zone is an issue though we could look at Mexico - there's a lot of good english speakers there.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And most of their salaries are under 1500

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: they all have perfect english

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: With Serbs they end their day as we are starting. So there's not a lot of crossover, but usually just a bit. So if you need regular meetings with them or rapid communication response then it wouldn't work.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you think one analyst could manage every client?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: how many clinets are there total rn?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: That's 160 hours to improve NSMs and overall account health. Which we can provide guidance on.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So essentially hiring this person would free up 160 hours of our AM's time to focus on better work and take on more clients...

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeh we should def have a loom account

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: :sweat_smile:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool. their happiness is good, but better nsm's is what will make ME happy

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If not we can start one

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If we are paying for one let's get it setup

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah someone has the main account then probably

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You can delete old videos on your free account to free up space if you need

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: oh gotcha

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You can also start a google call by yourself, record, screenshare, record

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: I have a plan put together for our team meeting week after next. These are the items I want to work together on between now and our meeting with the team on the 8th: • Process Documentation Review ◦ Move all Google Doc processes into Asana (Wed Jan 1) ◦ Create standardized templates for (Fri Jan 3) ▪︎ Client onboarding ▪︎ Landing page setup verification ▪︎ Tracking implementation checklist ▪︎ Design handoff procedures ◦ Set up sequential task dependencies in Asana (Mon Jan 6) • Role Definition ◦ Clear delineation of responsibilities (Mon Jan 6) ▪︎ Account Managers: Day-to-day client management, implementation ▪︎ Associate Directors: Oversight, quality control, strategic guidance ▪︎ Director (Mitch): Department strategy, final approval on major changes ◦ Document approval chains and escalation procedures I can work with you closely on these items to make it as easy as possible. ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm thinking for standardized templates, we just use asana with dependencies

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey Preston, I'd like to present a quick case for adding an offshore paid media analyst:
• For just $1,500/month we get a full-time person handling all the daily account monitoring and tracking setups that are currently slipping through cracks and causing us to miss our NSM marks.
• This frees up 160 hours/month of AM time (that's like getting a free employee worth $60K/year)
• We're losing $1M+ to churn right now - if this person helps us retain even 15% more clients, that's $150K saved for an $18K investment

Bottom line: $18K/year investment to save $150K+ in revenue and make the team way more efficient. We can hire someone in Mexico to align with our timezones, Mitch thinks someone in Serbia would be fine too. Good english is of main importance.

Want to try it for 90 days and see the impact on retention numbers?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey <@U025QMUHGTD|Preston Powell>, I'd like to present a quick case for adding an offshore paid media analyst:
• For just $1,500/month we get a full-time person handling all the daily account monitoring and tracking setups that are currently slipping through cracks and causing us to miss our NSM marks.
• This frees up 160 hours/month of AM time (that's like getting a free employee worth $60K/year)
• We're losing $1M+ to churn right now - if this person helps us retain even 15% more clients, that's $150K saved for an $18K investment

Bottom line: $18K/year investment to save $150K+ in revenue and make the team way more efficient. We can hire someone in Mexico to align with our timezones, Mitch thinks someone in Serbia would be fine too. Good english is of main importance.

Want to try it for 90 days and see the impact on retention numbers?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool. So first item is moving all our processes into Asana. How should we approach that?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool. Do you want me to help tackle any part of this?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Hope you had a great Christmas! Would be great if we could connect about media dept. soon. Do any of these times (PST) work for you? December 27 (Friday): • 10:30am - 1:30pm December 30 (Monday): • 9:30am - 2pm December 31 (Tuesday): • 9:30am - 3pm January 1 (Wednesday): • 9:30am - 3pm January 2 (Thursday): • 9:30am - 3pm January 3 (Friday): • 9:45am - 1pm January 6 (Monday): • 9:30am - 2pm If it's easier, you can click on a slot below to book: [11:59 AM] Jordan Dahlquist Would like to go over your goals, any issues or pain points you see in the dept. etc. ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Hope you had a great Christmas! Would be great if we could connect about media dept. soon. Do any of these times (PST) work for you? December 27 (Friday): • 10:30am - 1:30pm December 30 (Monday): • 9:30am - 2pm December 31 (Tuesday): • 9:30am - 3pm January 1 (Wednesday): • 9:30am - 3pm January 2 (Thursday): • 9:30am - 3pm January 3 (Friday): • 9:45am - 1pm January 6 (Monday): • 9:30am - 2pm If it's easier, you can click on a slot below to book: ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Hope you had a great Christmas! Would be great if we could connect about media dept. soon. Do any of these times (PST) work for you? December 27 (Friday): • 10:30am - 1:30pm December 30 (Monday): • 9:30am - 2pm December 31 (Tuesday): • 9:30am - 3pm January 1 (Wednesday): • 9:30am - 3pm January 2 (Thursday): • 9:30am - 3pm January 3 (Friday): • 9:45am - 1pm January 6 (Monday): • 9:30am - 2pm If it's easier, you can click on a slot below to book: [11:59 AM] Jordan Dahlquist Would like to go over your goals, any issues or pain points you see in the dept. etc. ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Hope you had a great Christmas! Would be great if we could connect about media dept. soon. Do any of these times (PST) work for you? December 27 (Friday): • 10:30am - 1:30pm December 30 (Monday): • 9:30am - 2pm December 31 (Tuesday): • 9:30am - 3pm January 1 (Wednesday): • 9:30am - 3pm January 2 (Thursday): • 9:30am - 3pm January 3 (Friday): • 9:45am - 1pm January 6 (Monday): • 9:30am - 2pm If it's easier, you can click on a slot below to book: [11:59 AM] Jordan Dahlquist Would like to go over your goals, any issues or pain points you see in the dept. etc. ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Would like to go over your goals, any issues or pain points you see in the dept. etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Who else is on paid medai team besides sam, nick, fabi, keaton?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Hope you both had a great Christmas! Would be great if we could connect about design dept. soon. Do any of these times (PST) work for you? December 27 (Friday): • 10:30am - 1:30pm December 30 (Monday): • 9:30am - 2pm December 31 (Tuesday): • 9:30am - 3pm January 1 (Wednesday): • 9:30am - 3pm January 2 (Thursday): • 9:30am - 3pm January 3 (Friday): • 9:45am - 1pm If it's easier, you can click on a slot below to book: Would like to go over your goals, any issues or pain points you see in the dept. etc. ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah let's include that in

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool, I sent you an invite already

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Agree

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool. Maybe you can throw this in a loom video and then we will send it out to everyone

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you add Maria as well? Unless you don't think she's needed

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok perfect, we can leave her off then. Thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Great to hear

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Oh awesome!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Any specific time work best for you?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok great

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Morning! Sorry to do this to you, but could I move you to monday or tuesday next week? I ended up overbooking this morning. Thanks Do any of these times (PST) work for you? December 30 (Monday): • 9:30am - 10am • 10:30am - 2pm December 31 (Tuesday): • 10:45am - 3pm If it's easier, you can click on a slot below to book: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or if you want to book on link

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: thank you!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Webserv client standardization
Meeting Participants:Jordan Dahlquist,Laurent Matson,Mitch Marowitz,Preston Powell
Start Time: 2024-12-27T09:30:29-08:00
End Time: 2024-12-27T10:26:42-08:00
Transcript: I'm in Connecticut at the moment.,All right. Well, good afternoon to you.,Yeah. Where are you based, Mitch? Irvine. Right on.,Yeah, I'm actually at my house in Capo Beach, which is like San Clemente, if you know where that is.,That's good surf down there, I think.,Yeah. Yeah, it's actually really good surf lately on Christmas Eve. Me and my buddy went out there and it was it was kind of huge. We were like the only people in this massive stretch of maybe like a mile of beach. We were like the only ones out there. I lost a fin, which kind of sucks, but,Oh yeah, it's been massive. Huntington was like 8 to 10 foot.,I think the last few days.,Yeah, yeah, there's been a heavy storm. Yeah, that's the winter special right there. That's better than me donning my 7 mil trying to go in Rhode Island. Surfing the Slurpee that we get Yeah. Forget about that. It's tough. No way. I'm jealous of you warm weather folk right now. What's the temp like in Austin, Preston?,It's nice, dude. It's 70 right now.,I can feel the 70 just looking out that window. Well, right on. Well, appreciate y'all joining me on this day of holiday week. Um, hopefully you don't have too much going on outside of this meeting.,Not much.,I mean, uh, calendar has been pretty, pretty simple this week. Perfect. So yeah, I wanted to build on the conversation we had last time.,Uh, Mitch, we, we haven't spoke yet, so you'll, you'll get to take a look at what we've talked about a little bit about our methodology here. Um, and here's what we're trying to accomplish for, Um, Standardizing web serve, um, standardizing the client experience, kind of like looking at our end to end, uh, agency model in terms of like our service delivery model. So we'll take a look at that. I've seen a few assets from the team so far.

 I saw the proposal deck. Thanks for sharing that. Um, Mitch, you shared some screenshots of like process, uh, screen grabs in some docs and things like that. So, um, have a couple build questions from there to figure out what, what, what this could look like, And that's it. That's the agenda for today. So I don't know if we'll need a full hour, but I'll just dive in if that's cool with you guys. Yeah.

 Perfect. Let's do. Alright.,Cool. Alright, so I think I showed this some slides here to Preston.,I think last week or the week before, We don't need to spend too much time on all of them, but Mitch, I think it'll be a good just overview again for your sake.,And Mitch, you're running the paid media department, is that right? Yes. All right, perfect. And then just a little bit of back information. Paid media is where we have experienced the most churn, which I think is pretty normal, but there's the best room for improvement, especially in like delivering a similar experience, no matter who you work with, because right now, if you get if you get, you know, one of our better reps, like, you might be really happy.

 And that might not be true with the other ones. And then like standardizing the project phase, I think is really important. So that clients know what to expect and what window expected and there's been some like misalignment between sales and delivery because a client wants to launch their ads tomorrow and it's gonna take us a few weeks and I got a call on Christmas Eve from this guy and he's like oh I'm really unhappy because you guys are gonna miss the launch date by three days and I'm just like are you fucking kidding?

,Yeah, that guy Isaac That's like a lot of the issues we have like Fairly good documentation, but it's it's like band-aids and patchwork and I kind of just like add to it And edit things as I've gone along people,don't I don't know where it lives or what's expected of them either.,Yeah, so I think we would do better if we one, had more time, but two, if it wasn't this, if it was more polished and I guess steps, like if we knew more clearly, like you need to do all these things first, cause you can kind of jump around with the tasks that we have. And I'm sure you'll have, I'll let you do your thing, but there's like ideas on, like we use Asana, right? I already shared that. I think we can use Asana a lot better.

 And anyways, I don't want to talk too much.,I'll let you do your thing. That's great. No, I think that's very typical kind of agency growing pains that we'll talk about. So yeah, let's dive in. So yeah, A little bit about me, I covered this last time. This is what I do. I have a lot, this is my own methodology that I'll be going through. So in a way, the kind of work that I do for agencies is you're kind of getting a taste of it here in terms of how I organize and package my own methodologies.

 So yeah, so my mission here when I work with agencies and service-based firms is basically leveling up agency maturity and growth. So there's different tiers and growth stages that agencies live at. And generally they get to certain tiers because they get, get a great niche, right? Like healthcare. And then maybe they, they get a great, um, they have a certain like a growth lever working well for you, whether it's referrals or SEO or paid media, you get one or two service lines off the ground and that's awesome.

 You started to hit like five mil, maybe 10 million, uh, ARR. But then you kind of realize like, wait, we're not as efficient as we'd like to be. We have some level of client churn. Maybe we have a lot of like, things like assets and docs and things, but it's kind of like Frankenstein together. Like I'm hearing from your team. Right. And that kind of keeps agencies stuck at certain growth tiers. The idea here is you want to build the tier that you want to inhabit next.

 So if you want to be a 10 to 25 million agency, you have to build that framework to properly scale and step into it. Almost like an animal grows to the cage that it's in. Right. So to speak. You kind of need to build that bigger structure to step into. And that allows us to scale. So otherwise you kind of get, you're kind of stumbling in the same area for a long time, trying to like put out individual fires versus thinking holistically and kind of piecing things together.

 So usually it's a couple things in tandem that are allowing us to get into those different tiers of growth and revenue. And it's basically a completeness of vision. So how well do we understand to understand our products, our services, how well are they documented? It's that infrastructure piece paired with positioning and vision, basically. And then how well are we able to execute on that vision?

 So this is a useful exercise for web serve, too, to kind of think about where we are. And it's interesting. Sometimes agencies just know where they are. They're like, we're in the starter area. We have some ideas about what works in paid and SEO or maybe works for us. On it so-so, but the experience is very variable, kind of like what we're hearing here. Where other agencies are like, dude, we're visionaries.

 We have amazing completeness of vision. Maybe we're not executing, or maybe they think they're leaders. I do have a survey and a self-assessment for this process, and usually agencies are a little bit lower than they think in this matrix. But look, not everyone invests in the conversation you're having right now, or in product development, or in R&D, and D and that kind of stuff. So, um, this, you know, it's, it's pretty typical.

 So what allows us to get completeness of vision in ability to execute on the vision is a pretty simple model. You start with productization that then, uh, goes into marketing, how we sell and how we service. It's a through line through everything. Again, usually agencies are great in one area. Like they're really good at marketing and businesses come in, we turn them pretty quick. Maybe our sales is average.

 Service is super variable again. So ideally you want to start with a really firm understanding of our product, which is our positioning, our methodology, our services, pricing, everything that kind of goes in that. And again, it's a through line that we then carry through all the departments and everybody feels, you know, well enabled there. So what that ends up looking like is something like this.

 And we want to create this for web serve. It's a pretty simple framework, but it's taking that and just understanding what our flow is. Is. So it usually, again, starts with that productization work up front, like building our MVP. We already know a lot of what we do best in things like paid search, paid social, SEO, you know, brand, etc. We get that well organized, arm that, kind of equip our marketing team there, that drive sales, we get our leads coming in.

 And that sales line is kind of like the client experience. That's when it kicks off, it starts in sales. Everything after sales, by also sales, right? It's like onboarding strategy ongoing. If we have different phases there, that's still about like satisfying the client. Otherwise there's this idea of like, you know, what have you done for me lately? I'm getting bored. Are we hitting goals? Are we hitting an SMS?

 Should I look elsewhere? Um, so that is, is that, will you say this represents our phases right now in terms of like sales, onboarding, I think you said project phase. I know that's like a directive term. That's always kind of confused me as well. I feel like it's like a strategy phase. And then we have ongoing.,Right?,Would you say that's about right? Yeah, I mean, I just call it the project phase, because that's what they called it. Yeah, strategy makes makes sense to you know, the first month, let's just call it that.,Yeah. Cool.,Yeah. No, I, and I think with directive, we, uh, it was project phase because we had a separate strategy product and we didn't like want to bastardize the two, I guess. So we had project phase restaurant. I don't know. But yeah, first month, everything after that is kind of like, I call it continued success. Sometimes ongoing is not always like the sexiest form of that. Um, and then like underpins it.

 Right. So like understanding like our approach for people for like operations and utilization, our tech stack and how we leverage that appropriately. Like those can be whatever we want them to be, but typically you have at least those three kind of underpinning everything. But wanted to give you that example of that flow. Now the problem is when we're talking about things like retention specifically, sometimes we focus just in this phase and we're like, how do we retain clients?

 Like what's happening? And usually the problem is back here somewhere and it's because gotten full alignment about what we do and how we do it and gotten that documented to facilitate this being successful all the way through. So it is that kind of holistic viewpoint, again, that I want to emphasize. When we do it well, there is this multiplier effect across all agency metrics. Again, I find it hard to work on any one of these, like some, and they're all really important, right?

 Like how do we increase deal size? Or how do we get, how do we stop being commodity and stop being just like an execution partner and become more like a strategic partner? Or how do we get more referrals, right? It's hard to focus on any one of those. Usually it is kind of just like a rising tide lifts all ships kind of framework. And it's like, all right, how can we again start from the beginning and build this all the way through?

 So I'm not gonna spend a lot of time on these slides, but this is basically at the self-assessment part of it. Most agencies end up being in the zero to one to two, score here in terms of product marketing, sales, service, and the integration of all those things. Obviously, what we're trying to build is a four-star experience where we retain clients, we get a lot of referrals, we increase customer lifetime value in AOV over time.

 So let's dive into each of these. And I have a couple of questions for WebServe on this and based off what I've seen so far. So world-class productization, generally, we're mapping out a product suite. We're understanding the sub-services under each of those products. So for paid media, we might start there. Then we might understand that we have CRO, we have design, we have maybe copy, maybe landing page dev, anything that supports that main product line.

 Our methodology is our secret sauce. So how do we do it differently? What's our proprietary approach? That's really easy for the team because we want to boil that down to the five things that we do. Building, right? Maybe it's the way we like set up our campaigns, reporting, et cetera. We get really locked around those. And then there's some other kind of tangential ones that are important too, but we don't need to focus on too much right now.

 When we have these dialed in, that's really nice because it's really easy, I'll skip the survey, to build our sales documentation. And we talked a little bit about winning by design. So there's really two parts of sales, it's like our process. So like, what are our stages? Preston, you already have like the winning by design, like template that I saw. So we like, what is our intro to strategy to proposal call?

 Do we have assets aligned with each of those? Generally, as part of that product work, we end up having a really sweet capabilities deck that's like fully comprehensive, like all the nuts and bolts about who we are, who we serve, what we do, why it matters, how That ends up being the foundation for any proposal deck. It's really easy for the sales team to figure out how to customize that in like five different areas.

 And that's kind of like how product blends into sales, if you develop those things together. So what that would look like in an optimal, like, let's say table for web serve, is that you could go into Notion or a spreadsheet, and you'd have this table like fully mapped for you, right? And everything's all these links are actually real. So you go to paid media and you're like, sweet, let's read the positioning.

 Let's understand what each of our service lines do underneath that. Let's look at the capabilities deck, a recent proposal, an SOW aligned with it, and maybe our best like project phase or strategy example. Right. And that's, this is like ideal universe. This is where we want to get to across the entire business. That being said, where we are now, Like, and would this be a nice to have?,I love this slide right here a lot.,This is very cool. Just having it all mapped out. Yeah, we're, we're, um, you know, not nowhere, but pretty much, um, there's not any sort of organization here. Right. Uh, we have nothing on positioning. Um, the sub services are kind of bundled and not, not valued. In their in their own right. Yeah, capabilities. We have some like different capabilities decks that are still like works in progress, but they kind of always are.

 And then we've got a proposal and a few different scopes of work that will work with no strategy examples, so right.,OK, yeah, I think that's fair. And then there's a continuation there as we go into all the deliverables after strategy, like everything else ongoing, obviously that we'd want to carry through. But this is just like, it's a nice visual to kind of wrap our heads around, like what a nice outcome would be. I think my recommendation here, and we'll talk about two parts. The first part is really the upfront productization and sales approach.

 Like, cause I feel like we can check a few boxes at once with that and also also probably the winning by design element. My recommendation there is kind of what I talked about last time, but like those engagements that I've seen tend to be very long-term and kind of expensive. And for agencies that are, or any company that's just like bigger and more complex and more unwieldy, and they just need a lot of help.

 I feel like there's just a way more streamlined version of that, that we could create pretty quickly. So the recommendation here would be if paid media is the focus, like this is something that like Mitch and I and anyone else on the team could tackle first. Like, let's make this a priority and like, let's build that through line. So like, let's just get in like, again, positioning is like a one pager, right?

 Maybe we do one for each of the different service lines. We understand, um, the, the sub components of it. We build like a, the kind of the master capabilities deck for 2025, same thing with a proposal. Make sure the SOW aligns with all of that, and then finish off that project phase presentation. So we have an example of what great looks like for the team so they can have a great template that they can work with.

 Now, I think that's going to equip probably maybe the department that needs the most help. It's probably also a pretty big department, probably has the highest ceiling in terms of getting additional spend under management in 2025. And then you can really see looks like, and then we can be like, look, do we want to apply that to SEO, brand development strategy, et cetera. But that would be my recommendation to start out, would be like, let's build it like kind of soup to nuts, really strong, kind of from a foundational approach for paid media.

,OK. How hard is it to, if we added on new services down the road and stuff, how hard is it to add to this? Is it something that we can kind of manually update or do we have to re-engage you somehow or like what's the actual structure for it look like,,No, I think it's always kind of to Preston's point that they're all in a different state, like they're all evolving. I think that's the natural state of it. You should evolve, you should be able to add on service lines. I think for things like paid media, like it's, you know, we have a pretty clear understanding at this age of marketing, like what the components are within that. No matter what, it'll be probably 80% of what we want that to be.

 And then we can always build around the edges. I mean, certainly. I think for me, it's very fluid. Yeah. It's not closed off. It's not about creating a constraint. It's about like, we have some cool core pages. There's some cool stuff in that proposal. We've thought about the methodology. I think it's just like, let's extract that. Let's be our own best case study and tell that story the best possible way.

 That would be the point of this, this part of it. We're looking at the productization and sales approach.,Got it.,Okay.,So once we have that pretty locked in, we feel good. Um, we can move into, um, I'll skip marketing. We haven't talked about any marketing specific issues, but marketing loves this kind of work when you can kind of hand them over this kind of stuff that we talked about Um, they love it, right? They're going to have better positioning. Ideally it's mapped to different ICPs. Healthcare is probably going to have very different types of ICPs, you know, from treatment centers to anything else, right?

 There's probably different types. Um, so we could better get better alignment there, better align our services per ICP, um, and have a more proprietary approach there. So marketing does tend to love this work tends to make everything else, um, just work better here and more cohesive. Um, moving into operations, this is an example, but we want to map out, um, the deliverables that we offer and the in-platform expertise that we offer.

 Um, and I'll kind of go into that a little bit more, but for instance, like there's like 30 things on the slide that we could do in strategy phase, right? We might not need to do all 30. Mitch is probably like, holy crap. It's a lot of, it's a lot of stuff, but like we could look at this and be like, what eight things should point of view on? What deliverables should we have mapped out that look ultra premium that we have under each of these?

 And then similar, when we flip it after that first month and we go into execution, what does that look like, Do we have campaign activation? We're optimizing ongoing. We have that reporting moment, always on strategy, client services that we offer. What are those? We want to fully map these out. And again, it doesn't have to be 30 things, but there are a few that I think we would focus on at first.

 And we would want to start with, what do we do really well right now? We want to extract the best of what we do. There might be a couple of builds that we want to add to the roadmap. But in the beginning, it's extracting the best of what we do and just better consolidating it here. So what does that look like, Let's jump into the operational or service side. There's three things that we tend to need.

 And one is the in-platform expertise and execution. So how good is a web serve paid media strategist in meta or in Google, right? Usually it's going to be some mix of campaign analysis. They're looking for quick wins. They're optimizing spend. When they first take over an account, they're shutting off certain campaigns. Then they're building that new campaigns. They're monitoring. They're optimizing them ongoing, right?

 It's kind of a simplified version of what they need to do in platform. But that's important. The client doesn't always see this stuff. So I, ideally, like, honestly, the best thing we can do here is we hire people that are like 80% of the way there. Right. Mitch, how easy would life be if we just hired people that were like pretty good at in platform, um, add, add setup and management. Right. Totally.

 Yeah. Big part of the equation here are the equation. Moving outside of in platform is the client side piece. And I really want to delineate the two because they're different, right? You can have someone that's awesome. Like you ever work with like the gamer type mindset, paid media strategist. That's like, like a wizard, like in meta or LinkedIn or whatever. And they're like, Holy crap. Like they're so good at it.

 They've like gamified it, but then you put them in front of a client and it's kind of like, it's not great. Right. They're not selling the value. They don't have a great strategy presentation. They're not like thinking sales led approach here. You know, the reporting's not great. They're not tying it back to like, why are we here? And like, why should we do this again next year? So things like that could be, yeah, the initial strategy presentation is important.

 Do we have a really nice campaign media plan, maybe a financial model, things like that are really important client deliverables. The most important ones to me are like how we show up at our key If you boil it down, a strategist only has like maybe five touch points with a client per quarter, usually. I don't know if that's web service approach. We can map that out, but it's usually like a daily Slack or a weekly Slack update.

 It's like bi-weekly meetings. It's a monthly report, a quarterly QBR. In the third QBR of every year, if it's an annual contract, should be like a renewal QBR, where we're doing it three months before they have to renew. They're planning out their budget. We get in there early. We talk about what the next 12 months are gonna look like, right? If we do those things well, we show up in those moments with the right collateral and the right message, you'll work new clients most of the time, right?

 And I think that's where we fail a lot. It's like we either have people that are too in platform or maybe they're more client side, but they're not piecing it together. Does that make sense as a framework? Totally, yeah. Sweet. So that's two. The third one here, the final one, is just the integration of those things. So the process and workflows that bring them together. So it's one thing to tell your team to do these things or where the documents are, but it's like, all right, what is my QBR approach?

 What do I do? Is there an asana with it? Is there a loom video and a training piece on our master template? What's the handoff look like between sales to onboarding to project phase, right? That's a process. There's not going to be a lot of processes, but there probably are like five to 10 really important ones, right? That we want to get mapped out and accessible and trained on. Um, and then like, it's really nice when you get the same, have you noticed how you get the same question?

 Like 90% of the time. And you can just send them ocean link, right? And be like, here you go. It's like notion links. You're just sending out. The training session that ideally we recorded and they can access over and over again.,Yeah, we're working on improving that right now. And Jordan helped me set up a Cloud project so the team can just ask Cloud and it's stuff that we've documented. So that's partially built out, but will be finished soon. Because, yeah, that takes up a lot of time.,Yeah. I love the clod approach. That's great. Of course, it's only as good as the inputs, right?,And we probably feed it. But we are. I need to be refined, but we'll see. Yeah. It'll take some debugging. But basically, we took every Loon training video Mitch has made and just put the transcript scripts into the project.,And it seems to work.,Probably about six new videos since that talk, just like two whatever that was.,Yeah. It's kind of cool.,That's great.,Yeah.,And again, I think if I was going to break these down, like for in platform, if there was like a silver bullet to this, I'd be like hire people that are like 80% of the way there. And for client side, like over index here in terms of deliverable development and training and stuff like that is the kind of focus.,Yeah. If we can make our in platform more scientific too, like we're reading that I love the point that it made about not hiring superstars, rock stars, but really nailing the science of how and why you do it. So you could basically hire a monkey with a keyboard and read the instructions. I would love to have that level of granular process laid out.,personally attacked.,That would be ideal. Yeah. If we can hire monkeys, we'll be all set.,Yeah.,So yeah, and ultimately, kind of the checklist for that operational piece, is it documented? Is it accessible? Are we training on it? Is it integrated? Is it continuously improving? The final one is usually a major miss. Which actually, if I come back to here, sorry, I'll give you the eye test for a second. The point is ongoing should tie back into product, right? This is such a big open loop or broken loop that I see.

 Usually your superstars are creating better versions of everything you have, but you might not know it, and you ultimately need that to be feeded to product to build that into our marketing and our sales so sales can start showing our best work more consistently. The rest of the team can benefit from the best work we're creating here. So that can simply be a best work in Notion file that everyone can go to by department in like Mitch, like in your all hands or once a week, whatever it is, you're like, hey, have we developed anything here?

 Like, do we have a new case study? We have to feed that back to the marketing team or back to product, right? So those loops are super important. So yeah, we'll look on each of those here. So in terms of in-platform, so getting to that A, A-plus level platform expertise and execution, again, understanding what we need to know from a in-platform expertise approach, Loom videos. Sounds like we're on track with that idea, at least.

 And organizing those in Notion, of course. There's kind of an adoption piece of this as well, which is how do we make sure things happen, which is kind of a whole other part of this. I have a philosophy on that, that I've seen work, but it includes like, you know, communicating the why effectively, giving them access. Like a lot of times it's about middle management and how we manage people, setting owners to it, like some kind of checkpoints or gatekeeper to it.

 It's kind of a, it's kind of a process, but you want these things to be ingrained in company culture. Moving into client side. It's really nice when you end up with. With a, with a value chain that looks like this, right? So I'm talking about all your deliverables in a row. And obviously I gave an example of like, you know, five things that would be important. This is an example of one I've done for an agency where I've, I've taken it end to end and we've gone from R and D to marketing to sales, right?

 So that's all that upfront work. And then we kept going into onboarding strategy, et cetera. And the team, this is like so many more hours were given back to the team and the executives. Like once we had all this done, because it was just mapped out. They could go to it. They could use the master templates. They knew what great... And actually, a weird thing happens where teams use Asana less, and I like Asana, but I don't always like to spend...

 I spend more time outside of Asana once I see it in there, and they end up reverse engineering to the deliverable. So they need the Asana less when they just know what a great QBR looks like, They can open and be like, sweet, I need to get these numbers, and kind of fill out this stuff to make it, and so on. So ideally, this is where we can come.,One of the issues, and I know this is probably partially because of all our processes are disjointed, but some of the important processes that Mitch has tried to roll out with the team, they just aren't doing, or they're not doing it completely. There's no dependencies. And so what I'm curious about is how do you create this in a way that it actually maybe has dependencies within Asana or something?

 How do we enforce it? Do we create systems to enforce it?,Or do we just tell them you better do it? It's both. It's both. But yeah, the management team is liable in the beginning, if we haven't been effective and cleared our communication within like expectation setting. And usually a level of like, visibility and transparency leads to accountability. And I think and by that, I mean, we need some level of like, like the NSM tracker, like, right, I don't know if you're using like directives model there, but we created a leaderboard for that.

 It was very visual. Everybody's name was on it. All the clients were on it. All the goals were on it. And all of a sudden NSMs went from like 30% to like 70%, right? Like literally when we rolled it out over the next like two months, because it was visible, right? It was like, look, this matters to us. This is a core OKR for the group. We're going to monitor this. And by the way, this isn't to like measure you in a like, you know, big brother type way.

 This is to support you. Like we want to like who needs more help and where executives can step in, right?,Yeah. So my question is a bit more practical too. Like I see all these great docs. This is super sick. What you have here, you know, how does that then trans like, how does Asana play with this in terms of tasking and stuff?,Yeah.,I mean, I, there, there are two different things, I guess, like for instance, this is a deliverable map, you know, where you would have all that in one area. Asana is more about like tasks. So, You might have an Asana per any one of these like project phase probably needs an Asana, right? That's like its own Asana board. Got it. Ongoing probably doesn't need an Asana, right? But like they need to be able to do the client work ongoing and show up in the moments with really good deliverables.

 So you don't want to over Asana. It's just that certain phases or processes need one. Yeah. But again, like it's actually a good question. I wonder like how many you would actually need for that. Like churn would be one like that's an important moment. If there's a churn moment you want to have a post-mortem Yeah group to come together and be like why that happened and then once you start going through that process you realize I don't want to have any more post-mortems Return approach to figure out why clients turn the beginning and let's be proactive there And now that comes that ties back into like an NSM tracker and things like that and like a client health measurement score Basically, which allows us to see clients that, you know, maybe we haven't heard positive feedback in a minute.

 Right.,So think of like, also, how do we centralize it? Because one thing I hate is having a team have to go into like 50 different places for different things. And knowing all this, there's a lot of like head knowledge of like, Oh, where's that doc? Where's that doc? Where do I track this? And it's like, how do we make it just an absolute no brainer, you know, like someone could just come in day one and know like, Oh, this is how it works, you know?

,I think that brings me to this slide.,Yeah.,A notion wiki. Yeah. Um, I think, yeah, I think Preston, you told me you had seen the one I built for directive. Um, extensive, um, you know, six service lines, you know, working also with like HR and like, everything's kind of in there now. And it's easy. Like if you're on the paid media team or in this case, like the SEO team, you know, it's an example, but you, you come in here, like, you know, what's happening with team admin, you have all your your project files, there's one for project phase, there's one for ongoing, you know, QB ours, and things are listed in there.

 It's just accessible, right? It's all in there. That's the way that I kind of bring it together. Okay, cool. And this is where you're trying to consolidate away from the Google Docs, like, I can't find anything in Google, right? Like, I have so much stuff in there, literally not find anything ever. It's the worst. I don't know what is going on with that. Yeah, OK. Yeah, the Slack tags, too, is actually kind of a cool idea, but probably gets a little bit unwieldy, right, as you probably experience as you try to add more and more per channel, right?

 What do you mean Slack tags? Oh, like something that, did you mention you had a pinned in Slack? Oh, yeah, pins.,OK, yeah.,I wasn't sure if there's another feature. You're talking about. Yeah, it is. We have like four different channels that they might need to sort through. And like Jordan said, it's kind of like head knowledge. They might not even know how to necessarily search for it. And so someone asked a question, and usually I can find it in Slack. If I can't, then what I have done is I made like a paid media library channel, but that's not nearly as good as this.

,If we could integrate this with our Cloud project, too, and then they can just ask Cloud questions, and it'll.,That was kind of where my head was going, too. I don't know how well Cloud could index this. I was actually thinking, I was looking into this the other day. I didn't make it too far. But you could probably just index, I mean, the search function is pretty good. Be good with in Notion, yeah?,Yeah. Sure.,It would definitely be way better to have it connect to Clawd, though, for sure. I'm getting off topic. Never mind. Sorry. I like how your head's going, though.,There's a way we could do it, for sure, though. It's doable. I agree. Yeah. And Notion's got decent AI now, too. I don't know if it's like the way Clawd operates, but it does have it.,There's a couple routes. We can already connect Notion to chat GPT. And we could also set up a webhook through make.com or Zapier. And then we could just have it auto feed into the project either directly, if that's possible, or indirectly through feeding all the information into a Google doc, because then the Google doc can connect directly with a cloud project. So it's definitely doable. And that would be sick, because then they can just be like, how do I do x, and it's only going to pull from this database only.

 It won't create new information.,Yeah. And ideally the notion is clear enough organized that they don't need that as much as they might need it. Right. Yeah. When it comes to like client deliverables and processes, like, cause we've already written it, it's there, it's accessible. This stuff about like kind of in platform expertise and just being good at different elements of their work. It's funny, like how, you're trying to figure out the right goals to set or optimize conversions or clicks or whatever.

 Can you go to YouTube and just watch the latest video of some guru talking about it? It's there. Usually for me, it's about gumption, enthusiasm. Will they take it upon themselves to figure things out? It's not for a lack of information. You know what I mean?,One of my goals is that we also, I want to connect our cloud projects with Slack. So they can basically have a conversation in Slack and it'll answer their questions, you know, instead of even having to go into the project. I think that would be great. Again, I'm getting way off topic.,I like it. That's actually cool. Cause that's like, I threw the gauntlet down at one point about like what the end outcome should be of this type of work. And it was that the executives could basically all be in Hawaii for like two weeks and nothing bad happens. Like, Like going along, we have a great assembly line. Everyone knows where to find stuff. Like we weren't at all. Right. And it kind of feels like that could, that could be the case with that.

 Um, love it anyway. Yeah. So in, in conclusion here, um, what we've talked about is my recommendation would be to focus a phase one on like streamlining the productization and sales and the element piece for at least one department. And it sounds like, you know, paid media probably has the most potential. Potential, probably has areas of churn as well. We could focus on that, button up our product that, you know, we already have some like outlines there from the proposal I've seen from the website.

 So I feel like we're in a good position to kind of put the bow on that. Create some really good sales enablement materials around that. I feel like we could also check the box of the winning by design piece of this at the same time, which is nice because we could just, you know, we want to make sure that we're developing the paid media in line with actual snail stages. So making sure we do have a good, uh, intro deck proposal, et cetera.

 Um, and then once we have that locked in, that methodology is also going to show us like what matters to us in terms of like our key deliverables or key processes. And then we'll, we'll kind of be in the driver's seat with that phase two and be able to standardize it. And that's more of an open box. And that's why I feel like phase one is important to give clarity to phase two. Because there's so much we could do there.

 And ultimately, we don't want to complicate anything. This is about simplifying things and just getting a really tight notion with the right deliverables and workflows in it at the end of the day. So yeah, I know I kind of sped through that.,But any questions?,Was that a useful overview or any notes on that?,I guess one question I have is, how much of your deliverables are theoretical and how much is actual development of the processes and writing out the actual steps and that kind of stuff. Like, what are you doing? What are we doing?,Yeah, it's a good question because I can work with internal teams. If you have people that you want to do certain things, you know, and I was talking to a guy once, he's like, look, if we, if someone can do it for like 50 bucks now or less, I'd like you to let me know. And then I'll get someone to do that kind of like on our team. That being said, a lot of this phase one activities are things I'm pretty hands-on with, in that also teams usually don't have the bandwidth for anyway.

 That's why I do this type of work. So I probably would be doing the writing, getting hands-on, building out these decks and the positioning in the winning by design approach, just because that's something I've done a few times and I'm pretty And I'm good at it. And I have a hard time getting someone else to do it to that level, to be honest. So this would be very hands-on in phase one. Phase two would be probably more directional.

 Mitch, you probably have a lot of these in different areas. So this would be more about understanding where we are from a mapping process. I could build a Notion framework. So I think it'd be a lot of support. But I probably don't need to write.,WHITEHEADed help with the Notion framework. They go in and plug in content.,Yeah.,Like the systems kind of like, what are the key systems? What could they look like, What documents or, or, um, kind of like, yeah, visible, visible, like frameworks do we need for these? And then we could figure out, all right, who's going to kind of color in the, the, the box. How do you like to handle nuanced processes?,Like you just get really granular, granular and break it all down. Like, how do you handle things where it's like case by case, I'm just curious.,Nuance processes, yeah.,I guess if it's important enough for us to want to processify it, then we kind of want to iron out the nuance. Like we want it to be pretty structured for the team. So it's like stupid proof, for lack of a better word. So that being said, I think if we want it to be, ultimately it's like we want the outcomes to be great. We want them to deliver great. Work consistently. So to me then it's less about sometimes like the one through five steps.

 It's about them understanding the why. So like that's the storytelling approach of this is so important. Like this is where you need to land. And at least for your best performers, they don't need to be told how to do something. They just need to be told like what outcome they need to hit. But you kind of need it for both parties, right? You need it for the people that need a process. You might not need it as much for people that Yeah.

,Um, yeah.,And then in terms of timeline, I feel like we can go through phase one pretty quick. I think, um, I don't feel like this would take more than three to four weeks. I'd say this would be like a discovery process, like gathering everything we have now talking with your leaders, anyone else who wants me to speak with and just, again, we're extracting like the best of web serve. And then we're telling that story in the best possible way.

 That's super crystal to clients and prospects, to our own team, to everything in a row. And I think from that process, we'll have a lot more information. So I'll be just under the hood a little bit more. I'll see more about like where things are to inform a phase two.,I can start literally in February, early February then.,Yeah. Yeah. And honestly, probably beforehand, because there's things that we'll be uncovering here that I don't need to build, but I could advise on and be like, look, I really think like, let's not wait for February or March to like work on churn, for instance. We can talk about churn, like right away, be like, look, do we have like expertise for churn that are really effective there so that those are already in process.

 Right. And like, again, like things will get better over time. In the beginning, it's like number one is habit formation, right? Let's like start doing this thing. Two is being effective at that habit. That's one way we could look at it. Makes sense.,Yeah.,I mean, I don't know about Preston and Mitch, but all this stuff, however we end up doing it, I want to get it done as fast as possible.,That'd be great.,Yeah, as fast as possible is good. Our training's super lacking, and this is gonna help inform that. And yeah, so I think our in-platform stuff is better than our client experience stuff by a lot.,Yeah. I'd agree.,But our in-platform stuff's still lacking.,Also agree.,Yeah.,And it helps with hiring too.,Right.,Once you have those competencies, like fully mapped, like, look, we really with our methodology, we really over index on these like three things. Then that's going to be easier to train. Yes. And give people a chance to like meet our new criteria or updated criteria. Some people might not make it though. Right. It just might not be their jam. And then that's like, you just need to hire some outside talent that really fits that profile.

 Um, and that kind of speaks to. Um, The metrics we want to hit. And ultimately for me, like I would want to get more concrete with like, all right, let's say we're at six to eight ARR. Like what's our goal? Like let's build, let's build a framework for that goal. Is it 12, 15 by the end of next year? Cause that'll help me dictate certain, um, you know, things that we build in certain metrics that we might want to target.

 Like with this engagement, less about marketing, it'll be more indirect. Like I mentioned for like the marketing. They'll just utilize what we have. But we'll see a real benefit under agency and team alignment, marketing and sales enabled, more efficient with hours, more streamlined.,And certainly on the sales and operational side, we'll see benefits here. So our goal for this year is to end the year with over 9 million in AR. I mean, our projections say that if we don't do anything better, we'll get to like 8.2. So with a little improvement, I think we could exceed that goal. But I wanted it to be realistic. And I would be happy if that's where we got. But I want a lot of the growth to come from client retention.

,Exactly.,a good place to start. Patch the barrel before you fill it up with more water, right?,Yeah, absolutely.,OK, well, excellent. Well, I know we're approaching time. But yeah, no, this was good. Any other questions or parting thoughts here? Pricing? Yeah, I didn't get that out yet. Yeah, so budget to this, there's a threshold for me, because I tend to go all out on this kind of work. Like, I don't, I don't cut corners really. So there, but I can, but I can be flexible in terms of like, if we're at a certain price point, you know, there's certain areas where I could provide it to your team.

 I could handle other areas for it. Um, but generally it's coming up like price points of like 20, 30, 40 K in those different tiers, depending on the way we kind of,On the lower end of that, I think we're, we're pretty good. You know, if you gave me, at 25K scope and you were willing to split it into two equal monthly payments of 12, five or something, I could do that. Okay. Or potentially we could pay the whole thing immediately. I just have to talk to my partner cause the end of year planning got a little bit, a little bit confusing just cause we moved from California and like California wants us to Not California, but our financial people or accountants want us to make a certain amount of money in California.

 We're trying to lose some money by the end of the year, but we have this phased approach to exiting the oppressive tax of California.,You and a lot of other people who are also going to Austin.,Not that any of that's important, but uh, but yeah, I mean 25k is in our budget much more than that probably Will be in our budget. Yeah, as long as it's piecemeal, you know, you know, um Yeah, so just just um, I don't know exactly Like yeah, what is that breakdown you're saying 20 30 40 but it would be great to know like what does,all that come with because Otherwise, we're just shooting in the dark on our end.,Yeah. Yeah, so I'll send across a scope that's more detailed in a Word doc so that there's everything in here that you would want to see. Yeah, that makes sense. That's kind of more like the sprint version of it, which I think works. I also work on retainer. A lot of times, I end up having that sprint and then developing retainer over time. So we don't need to start there. But I will say like, like, I tend to provide a lot of value up front.

 I'm like not trying to like profit that much in the initial sprints, because I ended up working with agencies for years.,So yeah, no, going into this, I talked to Garrett, he's like, Oh, it's, it's about 25k. And I was like, Okay, we can afford that. And then he connected us. And now we're here.,So Sounds like I need to give Garrett and my my sales Ballpark 25k. Yeah, you generally like these would be like 25k per phase Just to give you like visibility on that.,That's different phases So that let me work on the scope and I'll kind of figure out well, I think I think in phase two We're open to paying you a monthly retainer I'm saying we have appetite to spend what,you're you're looking for for phase one Yeah, it's interesting because I will say like in all like frankness I probably end up delivering more on retainers even if they're not like an entire year retainer just because like I'm on retainer for like 7k or whatever it is and to like just work a lot and like generate more work. So I was just telling that to another agency where they moved me to a retainer.

 I think I made less, but I probably worked equally the same amount.,Cool, give us a retainer. Well, you can definitely pay 7k a month.,I know, I know. I probably should better package my own pricing. I probably should take my own advice here.,Yeah, what the hell, Warrant?,Well, actually, on that, was this presentation useful? Did it kind of answer a lot of questions and show approaches that were useful here? Was there anything else that you'd like to see?,I'm excited to see the deliverables, but it answered a lot of questions, and I think it's well done.,Awesome.,Do we have a copy of it? You don't, but I can share.,That'd be awesome. Yeah, go back over and remind myself. It was excellent from a high-level view. But yeah, like Preston said, just some more solid deliverables. I totally believe that you work crazy hard, and it's going to be epic. I just would like to know, what are the actual outputs of this? What do they look like, Even maybe you can't share because of NDAs and whatnot, but some examples, this is what it would look like when it's done, just so I can get a vision of what we're talking about.

,Yep, absolutely.,Yeah, I have examples for pretty much everything there.,That would help me. I'd just love to see it.,Yeah, I probably wouldn't share those, because I am pretty good with the NDAs there. But maybe I could show those to you on another call. But in the meantime, I will line item everything in a scope, just so it's a lot more concrete with deliverables.,Certainly for phase one, where I think we have- It doesn't have to be like sharing an entire notion with me more of just like a screenshot of here's how we break out the home board. Here's an example of like one process and how I would approach describing each step or whatever.,Maybe some decks that you've done for the productization, just general stuff would be cool to see. Absolutely. Cool. Well, I think we're I think we're basically on the same page. And, you know, I, I value what I think. I think you have to offer.,Excellent. Well, thank you so much for meeting on this Friday. No, thank you. You guys are out Monday, Tuesday? Is Monday New Year's Eve?,Wednesday is. I'm working Monday, Tuesday.,No, we'll be there.,We'll be there New Year's Eve and we'll be there Monday. We just won't be there New Year's Day New Year's Day.,Just the just the Wednesday. Okay Right on I like Mitch I like how you're wearing a puffy like I just in California, that's awesome We can't hear you I don't know what happened Can you hear me now?,Yeah, I got this Costco for 17 bucks and it's like the best thing ever. Oh, is it a jury?,Oh That's awesome. Yeah. Oh, I love those. Yeah.,It's incredible.,I highly recommend.,I have Jerry style.,I could pick up like Marshall's or TJ Maxx. I don't know if you have those out there, but they're great. Um, good value.,Oh yeah. Um, anyway, uh, well, thanks a lot.,Appreciate that. I will send over some more, uh, items and yeah, let's catch up next. Oh, if we're trying to do a really quick Preston, if you're trying to do a end of year tax.,I think that's I think that's out the window. They want us to retain the money. So it's it's fine. We can spend it in January.,Okay, cool.,Right.,Yeah, cuz I know we just have two days for that.,Yeah, it's not a big deal. If it takes us however long we're Yeah. We are where we are.,All right. We'll have a fantastic weekend.,You as well.,Thank you so much. Appreciate it, Lauren. Thanks for your time, Ed.,All right. See ya.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's keep cranking

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Love it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah that's amazing

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Giroaeon2$

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: On the export page

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you show me what it looks like?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So why isn't slack just letting you export? I've done it before in past companies

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Directly

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm on a call

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah try it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: when you download

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So what happens

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan Dahlquist <> Samantha
Meeting Participants:Jordan Dahlquist,Sam O'Leary
Start Time: 2024-12-27T11:30:26-08:00
End Time: 2024-12-27T12:03:16-08:00
Transcript: Hey, what's up, Samantha? Hi, how are you?,Good.,Do you prefer Sam or Samantha? I don't know which one you go by.,I go by both, so.,Okay, cool. You prefer? Awesome. Cool, how was your Christmas?,It was good, relaxing, just getting over a cold though, so that was kind of unfortunate. Oh, dang it. Yeah.,I know Fabi was sick last week or whatever, so.,I know, I wonder if I got what she had, but I feel like everyone is sick around me. So I got it somehow. Mm-hmm. How was yours?,It was great just relaxing hanging out with family and pretty atypical American Christmas, you know Is all your family here? No, just my wife's family My family's kind of spread all over California and Arizona. Oh nice.,Yeah, pretty close though.,My family's kind of messed up That's why I like there's a lot of issues.,Is your wife's family good? They're chill.,Yeah, they're cool. Totally. Well, cool. Yeah, we don't even have to take the full 30 minutes. I'm working on a lot of planning and stuff for January, February for how we can improve each department's NRR and hit the better NSMs and all that kind of stuff. Stuff and wanted to just hear from the horse's mouth from each person kind of like any pain points, any goals they have. I just want to fully hear you out so that I can make sure I'm creating a plan that aligns with the team as well.

 So I guess my main questions are around, yeah, any low-hanging fruit issues you feel like could be resolved in the coming months, pain points you have, And then outside of pain points and things to fix, any goals that you have, like something you'd like to do, something you'd like to see grow in, something you'd like to see the team get better at, things like that. So yeah, I'll let you take it from there, if that sounds good.

,Okay, yeah. I think for me, I love the position that I'm in, and I feel like I've done a really good job of, it, the position was newer for the company.,I know with the, um, as your associate director, right?,Yeah. So I know what the consulting Preston was doing. Um, they, we established this kind of structure for the department and I think it's working really well having, um, my two account managers have that direct support for me. Um, and I've tried to build out processes, um, with them. As far as like managing them, checking in with them. And of course, you know, we're implementing the NSM or we did implement the NSM system.

 But I guess as far as like any more processes that you notice could be improved upon or that we're missing, because that was the one question I had asked Preston when he kind of established the structure was what if he could ask the guy that he was consulting with from directive, if like what their actual, you know, I guess processes are day to day with the account managers.,Yeah. Okay.,But I mean, I, I know I'm very familiar with everything that's happening with their accounts and the clients. And then, um, with the new NSM system, I'm scheduling out like, Monthly meetings with all of their clients as like a leadership sync So that's been really helpful That's great. I guess if there's anything else that I could be doing and then for the hiring processes Preston had asked me to do the training which I'm happy with but just want to let you know that that's how It's working in our department So, um, I, he, he initially was like, you can just do everything.

 Like Mitch doesn't have to be involved, but I wanted to keep him involved because he's the director. And obviously I want, if the role specifically we're hiring for now is another associate director, he and I are going to be reporting to Mitch. So he should have a say. So I did the first round interview and then any second round interviews I had him do. And we found someone which is I guess the plan still is, unless it changes, I would be, um, training him on all of the processes and onboarding with a couple of clients, but then he will be reporting to Mitch.

 So maybe figuring out a process of, you know, do I train him on all the processes and do the onboarding of a couple accounts with him and then switch over to the training of a couple of clients since he is going to be the director over him.,Got it.,So kind of, I don't know, I'm happy to do it, but I just wanted to like run that by you too.,Yeah. Well, I think it's probably going to be a combination because there's probably a lot of things that you know about this new role that you probably know better than Mitch in terms of what needs to kind of happen.,Right. Yeah. So the processes and everything I am taking on to train him on. So the process of the company in general, our department, and then of course the position, I guess more so for like onboarding of the clients. So the plan was is that we want the associate director to take on like two clients or three clients so that they can learn the entire process and then also how the management of them goes so that way they can offer the support for their account managers.

,Yeah they have to have. So what is the associate actually doing? So you're overseeing account managers and just supporting them them and like client facing?,So they're client facing. And then, um, I have about four clients of my own or three clients and then I'm offering support to them, the managers. And then, um, I am on the initial like onboarding calls to make sure everything goes smoothly. And then from there I stay on them or I join them if they're a little bit Rocky and they're having, um, performance.,Okay.,poor performance. And then in addition to that, once a month, I'm supposed to meet with all of the clients that are in my pod for like leadership syncs. Okay. Got it. I'm still working on scheduling all of those out. Cause we just started implementing that this past month.,And then what does it look like to support the account managers, like supporting them just like if they get overloaded, you jump in or what does that look like,,So, um, I just, touch in with them every day to see how they're doing and what accounts they need help on. And then they are communicating in all the client channels, updates. And then I, they check in with me too, with updates. And then if there are any issues, I help them kind of figure out what updates to do in the account to, you know, help the performance. And I will check in on them on my own to see where like different areas that can be improved.

 Page conversion, optimization, stuff like that. Got it.,Okay, cool. All righty. So yeah, you're going to be helping with the processes and then for the client onboarding, are they going to be clients that you're familiar with?,For the new associate director? Yeah. Yes, it's going to be more of the like addiction treatment clients that we receive Yeah, well, I imagine you could help with that onboarding.,I'm going to have Mitch really busy the next month or so. So I'm sure it could be a combination of him helping with that and jumping in. But to be honest, I'm going to have him really loaded down. We're about to invest a ton of money in productization and process development for every department. And it's going to be epic. It's going to blow your mind out of your skull. It's all done. And it's going to make us able to scale a lot better and a lot faster.

 And you won't have to do as much training and onboarding because it's all going to be documented. And all the things in that sense that we've needed for a long time are now going to get done in January, February. So that also means Mitch is going to be really busy with that. But I don't think he can't help at all. I just think if you could help with that.,It'd probably be a huge help, you know? No, for sure. I was already expecting to. I just wanted to make sure it aligned with like what you wanted.,So that's perfect. I'll be happy to do that. Okay. Thank you. And yeah, anything else you want to bring up?,No, that's pretty much it. We're going to, as you know, also hire an account manager. Um, I'm scheduling interviews for next week to find one.,Um, you, uh, posted it last week. How many applicants did you get? So on LinkedIn, let me check the updated number today. Well, you did, uh, for LinkedIn, you linked it back to the workable job, right? I didn't link it back yet. But I posted it, and I- Oh, no. That means it's not going to go in.,You can't get them over into Workable if you didn't do it at first. It says it paused anyway. So it was a free job post, and so it paused after 150 applicants, I think. Yeah. How many applicants we got. So I can do it again and then link it. Do I have to link it directly after or I have to link it first?,No, when you create it, like the very last step in LinkedIn is where do you want the applicants to go and it's either email or a web page. It's a drop down and you select web page and then you go to workable and you copy the job page where they can apply the workable job page.,Okay.,Paste that link into the LinkedIn job and And that way, when they apply, they're not applying on LinkedIn, they're gonna go to that workable job and then apply there.,So I, oh, okay. So I paste workable job page as the link. Yeah, exactly. LinkedIn.,You can get that link in the job on workable. I can show you if you don't know how to do it or if you get lost.,No, I remember that step, I just thought, it was better for them to apply directly on LinkedIn, but that makes sense that we want it all to go into workable. So I thought it was like connecting thing after the fact. I understand.,Apply workable because then they're in the workflow of doing the challenges and the interviews and like all that kind of stuff. If they're in LinkedIn, they're lost. Like we can't make them do all that stuff.,Okay, yes, that makes sense. So I only got 50 applicants because it was the free posting. So for here, it says that 7,845 are sourced but no applied yet. Do I have, is there something that we're supposed to be doing?,No, source just means, that means nothing. All it means is like workable has made a bunch of people, it's on job boards and that's like how many people are available to see it basically. Applied is where it's at. Actually went to the job, filled out their information and applied. And so right now you have zero applicants. Is there a way to invite people?,Yeah, you can go to find candidates.,I'll go back.,Yeah, just tap find candidates right there.,And then most the majority of the from your last one come from LinkedIn then?,Most of them, yeah. Unless you do a premium job paid board. Okay. So like where it says premium job boards, you can go in there and you can pay for some of these boards, like go down. So like you can do jobs by workable for 30 days, $75. You could do a LinkedIn one, but I don't recommend doing the LinkedIn Boost from here. I recommend doing what you did creating your own and then linking it to the job post But honestly the LinkedIn's worth that I've tested all these and like I don't think most of them I think most of them come,from this Post the one that I just posted and then instead of having it apply I'll put in that way you want to do it with screen share and I can just in case yes, cool Um and keep in,mind if we're gonna do the whole challenge process it usually takes minimum four weeks before you finally get down to your last batch of candidates. Okay. Um so if we're in like a major rush you know we shouldn't do that we should just start interviewing people but that's more time consuming. But if we're not in a rush then we can find someone better hopefully you know.,Yeah I will um be looking at the applicants as they come in and and I won't necessarily for the challenge. Necessarily, if I find really good applicants, then I can just...,Okay.,If that's the case, you might consider leaving it for now and just looking at those 50 that you got, right?,Because you might... Yeah. Yeah.,I also had the batch, like the 300 from last time too. Yeah. Okay. So I'm going to just take this...,The reason why I'm doing that is because Because you don't get to do the challenge, you don't get to see who's really putting in the energy. Because sometimes someone who looks really good on paper isn't good, you know, when they actually are doing something. So are you kind of in a hurry to get this person or do you think it's okay if we take a month, month and a half before we lock in someone?,No, I mean, we are in a hurry because we're onboarding a lot of clients and we don't really have, like our account managers are at max capacity. So I think we should still post the challenge, but can still reach out to people. Okay, yeah. Okay, cool. So we'll do both then. And don't forget, you have to send the challenge to them.,So you have to create an email that says like, invite some to the challenge, and you'll send them to a live word doc, Google Doc with the challenge in it.,Do you have a template from when you sent that?,No, but I can get it for you. I can, I can send you the one I used. And then do you still have the login to that old account? Did I give it?,I have your login for this one, but not for the old one. Is it like a, would it just be a different URL? It was the super hires one with super hires login.,Oh, let me see. Because if you have that you could actually go in and get everything you can get like everything I've ever. It would be really good for you to have. Let me see.,I think I do have it too. Okay.,He logged in. Nope. Nope. Gosh.,My computer is going. Is really glitchy. Bummer.,Yeah, so Jordan at SuperHires. Jordan.,SuperHires.ai.,Okay, it's not saved, but I'm pretty sure it's in the Slack. Type in, here, I'll give it to you. I think I know what it is.,There you go. It should be that one, hopefully. I don't think you're typing, just so you know.,I was copying and pasting it. Oh, I got it. Sometimes I know if you click away, then I'll be typing and nothing's going in. Oh, it didn't work.,I was wanting to do the recapture, so let me try again.,Oh, got it. Yes. OK, so close out. Last pass. Go up on the top right as soon as it moves.,All right. Yeah, hit that one. Hit Settings.,This will be good because you can copy everything out of here. Go to Templates. All right, and then in case templates down All right, so Go down a little further assessment Go up It's not showing My custom one that I've developed for some weird reason What keep coming down maybe it's at the bottom no Um, that's really weird all my templates are gone It's very strange Is the job still here because I could probably just copy and paste from Go down.

 That's not it. Go down to talent Wait, what? Oh, you're in WebServe right now. Look, it says WebServe. That's weird. I don't know why I keep doing this.,Remember when you sent me an invite and then it had me sign in, it automatically logged in as you.,Yeah. Let me see. Maybe an incognito window or something. Maybe it's caching something. I don't know.,It's really strange. Try again.,That's why there was nothing there is because we're still web serve Okay. Now this is the right one on the top right then settings Had me scared there. I thought I lost everything All right templates on the left up up up. Oh There you go templates All right communication templates and here you will see There's all different ones. So like the associate director paid media send challenge go up that one You can hit preview.

 This one is to send the challenge. And you can actually click the link and see the challenge that I sent and all that. You could send this as yourself. You could change it out for yourself. But this is written in a way to try to get people motivated to do it. The goal is to make it really compelling and not just like some random email from some weird company that wants them to do something. Directly from this platform?

 That's how it all works. Yeah. So you can do the entire process in here. So if you go over to Jobs, I'll just show you an example. So go to paid. Actually, go down to a one digital. Go ahead, that's fine. Just select the checkbox next to Tracy Hogg, for example. Uh-oh, where'd you go? You want me to look at the PR specialist? That works. Yeah, hit that one. So hit the checkbox next to Sam. So see the little drop?

 Oh, the job's closed out, but see where it says Move to Challenge, the little dropdown in the gray box? Yeah. So normally, you can hit that dropdown, and it's going to give you every template that you've created. And so the way you do this is you would just select the upper checkbox to select the entire list. So basically, you'd have five people in applied right now, and you just select all of them.

 And then you'd send, you'd, you'd say move to challenge set, and then you move them over there. But you want to send the email first. Otherwise, you'll lose them in the list. So you send the email, then you move them to challenge set. Does that make sense? Yeah. Because if you move the challenge set first, you don't know where they are in You just lost those people and you can't email them anymore because there's like, you know, a bunch of people in there.

 They're all mixed up. Okay. You sure that makes sense. You got it. I just want to understand. Cause what happens is you can lose people. You can email people twice. You can actually forget to email people and it gets really messy, really fast. Each step of the process, you're emailing them a template that you've pre-made. So it doesn't take any time. The whole idea is it's very fast and you're, you're messy.

 Emailing people and they either do the challenge or they won't. And then that's it. And then you can do the video interview, which I highly recommend to save time.,The idea is to get the absolute best possible person, you know? Okay, cool. So for the LinkedIn, I'm going to just start a new one and copy and paste all of this and then link it to, uh, Yeah, go ahead and just do it now we can have the,I did have the job posting but,OK, so I have the job posting link pulled up. And then I need to just copy and paste all of this.,OK. It didn't screen share, so I didn't see how you did it.,It's just this is the link, right?,This page? Got it, yeah.,So hit Share Job. Or yeah, that should be it. Yeah. I can't see the URL in my screen share, but I'm sure it's there.,Yeah, so apply.workmanager.,So then when you create it, when you post it, when you get to the last step, it'll like, where do people apply? Bye.,you. It hurts.,Cool. Can I see the first paragraph real quick? Just take a peek at it. Cool. That looks great. Awesome. All right. We can throw some than I usually do.,Let me pull up. The last one.,Trying to just find the range real quick of what we had. I think you said 70 to 100 Canadian, wasn't it? Yeah, I don't know if it was.,But that was the associate role, not the, this is a,This is a specialist.,Yeah, so it should be lower. I'm just looking at the candidate the previous job postings that I had because for some reason It's not showing me on LinkedIn. Thank you.,I had it posted on Indeed, though, too, so let me see.,you It was 75 to 100 because that's up to 70,000. The associate director was like 120, I believe. Oh, you mean it's up to 70 USD? Yes. So it was 75, I believe, 75,000, which is 52,000 USD, and then 100 Canadian dollar, 100,000, 69,400. So we'll do 75 to 100 range.,And then for this, I had three years of Google Ads.,Here's Facebook.,And then analytics. Okay, cool.,What was that last thing on the bottom? You go back. And it also has the link.,Right, right there.,So here you can click receive by, change that to that. Yeah, there you go. Perfect. And then is there any additional Any additional connection I have to do with LinkedIn and workable or that's just automatically going to go in because it's through the link.,Yeah, you're literally just sending people out of LinkedIn into workable. So it'll be direct.,Yep. Okay, cool. And then also.,Sweet.,So the next thing I would do when you get time in the next day or two is to go grab some templates out of the old workable and stick it in the new workable put it in your name and like you know that kind of thing yeah I want to do the login account okay cool and then also the challenge I recommend making it a leaving it as like a live google doc and then making it only view only for everyone do a view only link and the reason I do that is because sometimes I find that like there's an issue with the challenge and people start emailing me like crazy and like Oh, I don't know what to do with this part.

 So I mean something's wrong and then Or they're just really confused and like a lot of people are getting confused about the same thing I can just update the live doc and then I don't have to like resend the PDF to every single person again, you know And a lot of people try to reach out and say hey share the doc with me Like give me edit access so I can do it and I'm just like delete just,ignore people like that Are just your instructions for them? If they want to, like, make a copy and do their own, or are they just going to start from scratch in a new document? Is there instructions that tell them that?,There's supposed to be instructions in there. I think I said, like, well, there's instructions on how to submit it. It just says submit a PDF with your results. There's a lot of detail. I put a ton of detail in my challenges and my emails. Like, you'll see it all.,Okay. Yeah, I saw the document too, so I'll just use what the templates you have and then make sure that the links are still working and just replicate that.,Yeah and maybe take a peek through some of the other template emails because some of those might you might find useful for different phases. And I try to send challenges out every day but set a hard deadline like put it as to say so we could put it like January 20th as like the hard deadline. And then, but I send, I go in every day and I'll send challenges to anyone who is newly applied, if that makes sense.

 But then everyone has until January 20th and that's like the hard deadline. And then I usually don't bother sending challenge submissions or challenge invites less than two to three days before the final deadline, because it's just kind of too close and most people aren't going to be able to do it.,Okay.,Yeah, sounds good. Yeah, I'll work on that.,Okay.,And yeah, you just send it by you go to applied you hit the little checkbox for all people who've applied and send the template you made and Then you move them into challenge sent. Otherwise It gets really confusing. Like I said, so yes.,Okay.,All right Right on let me know if you have any questions. Okay.,Awesome.,Thank you so much.,All right. See ya.,Bye

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let me check with Jordan on this!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hi <@U05A4CDP37U|Jordan Pohl>! Do you have any ideas on this? Maybe we just pay her a little extra to cover the processing fees?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok yeah we maxed it out then.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Kind of like claude or GPT but it's for large documents

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You know what you should do is look into humata it's an AI tool that can pull from very very large document databases

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And every 100 pages we can press it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Another idea is take maybe 100 pages of what you have right now and have Claude compress it down by 50%, but maintain the important information.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Whatever you think is best

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: That could be great

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If it's your bank then I don't think I can help with that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U083E324RCL|Julia Gumeniuk> where is the withdrawal fee coming from? Your bank? Or rippling?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok gotcha. Rippling is the only tool we use, and it's Webserv policy not to deviate from it unless it's a single project for a vendor or something. So we don't have any other options for form of payment unfortunately.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Morning! Julia was asking if we can cover the $40 fee that rippling is charging her to withdraw her money each month. Do you want to do that?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sure! I'll ping him about that

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Are the offices open this morning at 8?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Nevermind I'm going to wfh

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hi Julia, we can meet you in the middle on the cost but that's the most Preston would like to offer.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U05A4CDP37U|Jordan Pohl> Can you add $20 to her pay per month to help cover fees? Thx

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeh wish we could do that for you but we have to manage a lot of contractors, so we have to keep everything centralized.

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan Dahlquist <> Fabiola Morales
Meeting Participants:Fabiola Morales,Jordan Dahlquist
Start Time: 2024-12-30T09:31:11-08:00
End Time: 2024-12-30T09:46:09-08:00
Transcript: Hey, good morning.,Hi, good morning, Jordan. How's it going?,I'm pretty good.,How about you? I'm good. I'm in El Salvador right now.,Wow. Awesome.,That's so cool. What are you doing down there? Visiting family or?,Yes, I'm spending, you know, here we celebrate Christmas and New Year's. Oh, yeah. So I'm spending the holidays with them. That's awesome.,Super cool. A pupusa for me while you're there.,I already did like three times. It's so horrible. Like I don't want pupusas anymore for now. So cool.,I love it. Well, thanks for jumping on with me real quick. Should be a pretty quick call. I'm just kind of working on some planning for each department going into the new year and just kind of wanted to have a quick connect, hear anything that you feel like we should be improving in the paid media department, any pain points you're experiencing, any room for growth that you could see in the department, kind of anything along those lines that you'd like to share, I'd love to hear about.

,And then I can kind of consider that as we move into the new year and start to optimize things. I think I lost you.,Are you there?,Well, you know, when I started, Yes, I'm here. Can you hear me?,No, I can it. I totally lost you for a minute. I think I can hear you now though.,Oh Okay, perfect That's weird. Um, no, I I was gonna say like I think one of my pain points is you know for me it became an issue at the beginning where I was like super excited to work at the company and I was giving it my all and then he came to a point where I was like I don't want to say Not paid attention to but like everything I gave as an idea was like oh Yeah, well, no, it's not gonna work or yeah, I know like it's too hard or no.

 Yeah, but uh, so it came to a point where I start I stopped Trying more, you know, I stopped trying to give more stuff like I was like, I Propose and I was not hurt. I said something I was like, no, it's not it's not it's not it's on Bible or no It's not important or no, it's not gonna work or no, it doesn't instead of being like oh like, you know, how can we do it? Etc, etc and i've seen that come like i've seen that um lately happen a little bit more than it used to because for example and I understand I understand it's not person's fault I understand that clients call you out of nowhere to say like hey things are not working like and you have to take something like immediately out of your pocket and be like okay offer you this right but um this miscommunication where the client it has to come to a point where it tells it tells Preston like, Oh, I do I have to come all over to call to call you for you to do something about it.

 And Preston is accepting our fault when we have been doing something about it, you know, just because it was not informed to him that I was actually doing something with the account doesn't mean that there was nothing being done, you know. And then, you know, proposing strategies and being like, immediately in that moment, and just be like, Oh, let's implement them. And And not being, I want to say consulted, but like, maybe instead of just being like, Oh yeah, this is what we're going to do immediately right now.

 Instead of being like, Oh, I know that the team is doing something. Let me reach out to them. And we can also like, I can bring some ideas to the table. Cause for example, I'm not going to lie to you with Prada house. It was a client that I never, never agreed on this tragedy that they did. I texted. And I was like, hey, you know, this is, um, do you agree with this tragedy? Cause I don't like, I don't think it's going to work.

 I don't, I don't believe it's going to work at Adam and it didn't work, you know, and I was proposing and everything that I was like, no, no, we're going to do like what we were done to do what we were said. Sorry.,We were set to do, you know, and it came up with that strategy.,Was that Mitch or Preston or, well, first we want to switch to maximize conversions that maximize conversions. And value that Sam and I were not okay with was Mitch. And I was like, Mitch, but this information is like, no, it's okay. I don't care, do it. And I'm like, okay, I'll do it. Fucked up the campaign. And then, you know, like, oh, let's restructure the whole account. And I was like, oh, this is not gonna work, you know?

 And I was like, it's not gonna work, it's not gonna work, it didn't work. And now finally, it was like, and it was until I raised my hand, it was like, Oh, why hasn't something been done before and I'm like it has been done before, you know Like we did stuff just because you didn't see it doesn't mean that it that it hasn't been done. You know It was going into Question, do you keep the client informed about what you're doing?

 And do you have the client was completely aware of what we were doing God was completely aware of it And at the same time the first week that things started going wrong. I raised my hand. I was like, hey, thanks, sweetie drastically like What can I cuz it came to a point like this account? I wanted to do it do everything perfectly specifically for grad house I wanted to do everything by the book because it was the first time I was given a new big account and we had this new like Way of doing things Disney procedure, etc stuff like that So I was like, I'm gonna do everything by the book and I'm gonna try to do my best, right?

 And that included not making any changes or any sudden changes without Informing or asking or anything like that because then I didn't want it to become You know like oh you shouldn't have done this you shouldn't have done this But I should have just gone with my God and I should have done what I always do and it's just like Take full ownership of the account. I will take responsibility for that I didn't take full ownership because I was like, oh this is how things are supposed to be now, right?

 Did the whole purpose was let's do cookie cutters type of stuff, but not all. It doesn't always work the same for one accounting within another. I don't know why they can have the same budget. They can be within the same area. We can do the same strategy. One account is going to get massage colors. One account is going to get real colors. Um, so I think that's the biggest pain point. And at the same time we are.

 Facing so many small things. And for example, when building out an account, oh, you have to do it within one week. And you're like, okay. But at the same time, I have to keep having my meetings. I need to keep doing changes for other accounts. I need to keep reading data, because it's not, oh, I'm just going to pause this keyword. It's like, why am I going to pause it? Like, I have to go through the last 30 days.

 I have to understand what's happening. I have to go through the search terms. I have to compare it with other accounts. With other times that are not. So I think right now, like, those are my two biggest pain points that I see that one is the lack of communication or even being open enough to be like, okay, let's try this. This last two weeks, I've seen difference after I brought it up after I told him like, hey, you know what, like, yeah, I did.

 I went up to press and I was like, hey, I didn't do anything because I felt like I was not because This was the strategy that I was told to do. And I did and I did. I was following instructions because I thought like I was trying to do the right thing, you know, and I was like, fuck this, I'm going to do whatever I want. And I built the dynamic keyword insertion campaign. Well, actually, I did build it, but I did an existing campaign and I just made small changes on it, even though they told me like, oh, build it from scratch.

 I was like, no, I'm not going to build it from scratch. I stood my ground and I was like, I'm going to do this and this is what I'm going to do. And I asked Mitch for help and Mitch was like, Oh, maybe you can add this. No, he first, he said, like, maybe you could do it this way. And I'm like, no, I want to do it this way. It's like, okay, maybe you can add this. And it's like, it's different when it's like, maybe you can add this to the companion.

 It's going to work versus not do something completely different of what you want. Right. I understand that it's also harder for me that I'm far, you know, trying to communicate with the team, et cetera, stuff like that. Right. Um, sometimes I feel like right now that Claude is really going to help. I understand that Mitch is always busy. By the way, I couldn't install it. I also share it to Mitch and he's like, that's weird.

 Um, install it, like create it. Let me just not install. Sorry. Like the document. Oh, you couldn't connect it.,Yeah.,I couldn't connect it.,I tried multiple times and I couldn't.,Yeah, send me a loom if you can. And I'll look at what it's showing. I don't I'm not sure why it wouldn't be connecting for you.,Oh, no worries. So yeah. Thank you. So yeah, I think that's those are the main two ones versus that I know that on both of them.,The first one was communication breakdown and like not consulting you on strategy.,What was the second And the second was like how fast we do things and like this feeling to designer I know that that has been that has been changed but then for example I've been telling them like we could get a PPC designer completely for half of the price with a Mexican designer or even like London Mary like Someone from here, you know, I think that's what we're gonna do.,Actually. I'm I launching job descriptions this week. What we're going to do or discussing is hiring a Google Ads analyst or something like that, where basically what they do is handle all the here. Let me just look up what we kind of outlined. Second, basically, it's someone that takes off, takes up all the data alignment, sheet updating and account analysis for you. And then all you have to worry about is client facing comms and strategy and reporting, but they can even help with building the reports, but you just need to be like involved in it.

,So, you know, your numbers and stuff, but yeah, I think like we are going to be in charge of implementing, like, like implementing, optimizing this tragedy too, right? Yeah. Okay.,That's can help you. By making recommendations and, you know, but they're not gonna do it themselves. Like they'll, they're basically gonna take up all the easy, like hard, like the mundane work is the idea. And then you get to focus on like the stuff that you're really good at is the main goal. What do you think about that?,I love that. Cause for example, I'm terrible at, I know what's happening on the campaigns. I understand what's going on. Like I know it, but I'm terrible at translating that information into a Google sheet, like copy and pasting, or showing how to screen? Yeah.,So I think we're going to hire one or two. We're going to hire one at first and see how it goes. And we actually think that one person could do this for all the accounts right now. And if they can't quite do it, then we'll hire another person also. But I'm going to start working on a job description for that this week and start advertising for that But we're gonna try to hire Possibly Eastern Europe.

,We'll see.,Do you think that? Time zone is gonna be an issue with this person Like do they need to be in the same or similar time zone or do you think it doesn't matter too much?,I think it does a little bit at least just a few hours that we know that they're gonna be available for sure Mm-hmm be the biggest issue but with you, California Yeah, so I mean in Serbia our 9 a.m.,is like their 6 p.m. So like this whole SEO and PR team that I built out we hired eight people and I can always touch base with them in the morning you know it's like their evening. Do you think that's enough or do you feel like it's really important that you have someone that's like really...,I think that also like sometimes the afternoon Not terrible because I really like the mornings are more we're just getting a hold of everything and we're And from there we start tasking out, you know, maybe at least the first,three hours Yeah, like from nine to So maybe someone like in latin america would be better than someone in our time zone similar Yeah, okay. Yeah, so I'll run job ads And see what we can come up with. Um, but yeah, that's gonna help hopefully help you guys a lot. As far as the communication issue stuff, I mean, I'm actually working a lot with Mitch right now. And a lot of that stuff, I think, is going to get worked out once we kind of improve on our systems, our processes.

 We need to also, one thing we're building out right now is a order of tasking. And how that all kind of works. So this is really helpful, though. I have my read AI here, so it's taking notes. And I'm going to definitely take all this into consideration as we're moving forward. So yeah, really appreciate it.,Thank you. I think just those are my two biggest issues, is communication and being, ideally, for me, a process would be like, oh, yes, let's Let me understand what they're doing. And maybe I can add or I can express why I wouldn't do it or why I would do it differently instead of, you know, plus whatever you have and do this, you know? And it went terrible. Yeah, totally.,I mean, it's not going to be easy, but I think we can improve it drastically, you know? And I also think that the team's going to get the bandwidth is going to get better, even though we are bringing on new clients. We're hiring a new associate director, manager, whatever associate paid media. Um, and then we're also going to be hiring this analytics person and then we're also hiring another paid media manager.

 So you're going to, there's going to be a lot of help coming for the paid media team over the next month or two. Yeah. Yeah, totally. So, all right, cool. Well, that's it. It. Anything else you want to add or share?,I think that's pretty much it.,Cool.,All right. Well, thanks for the time, Fabi.,Appreciate it. Thank you. Have a good day, Jordan.,You too. Enjoy El Salvador.,Thank you.,Bye.

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan Dahlquist <> Shannon
Meeting Participants:Jordan Dahlquist,Shannon Lee
Start Time: 2024-12-30T10:00:39-08:00
End Time: 2024-12-30T10:14:35-08:00
Transcript: or something like that. We're getting close. Yeah, yeah. Well, let me get my camera working. Sorry. Here we go. How was your weekend? It was good.,I was in Sacramento visiting family and so I drove back on Saturday. Cool.,Is that where you're from,Yeah.,Nice. That's awesome. Sacramento is a cool place. My brother lived there for a while. And I kind of grew up around the Central Valley. I was born in Visalia, and then I lived in Redding for five years. So yeah, I used to fly out of Sacramento all the time. Yeah. Right on. So yeah, for this call, it doesn't have to take super long. I'm just working on some planning for January and kind of what we're going to be working on and stuff.

 And we're going to be doing kind of like an eight-week sprint that I'm working on for each department, kind of just fix a lot of low hanging fruit, like things that we can easily fix and make work better and flow better and all that. So anyway, I just wanted to make sure I'm making a well-educated plan and not just running rogue. So I wanted to hear from the horse's mouth, from you, are there any challenges you're facing, any pain points, things that you feel like could improve?

 And I know I kind of already touched on this a bit in that one call that we had. I know you mentioned things like lack of communication between paid media, people not doing Asana properly, not getting the info you need.,Yeah.,And then rushing you. Yeah, I love the farm idea. I think it'll help a lot. Yeah. Yeah, we're we're I tried bringing it up with Mitch because it had happened again. And he's awesome. Kind of at a loss of what to do. So we'll see how the form thing goes. And then I told him, and maybe you have some insight on this too. And you could tell Mitch, but I was like, if, if this still happens with this implemented, I think there needs to be some kind of consequence.

 Like, it doesn't have to be like, you're fired, you know, not so extreme, but like, definitely have an effect, like the communication portion of their performance review or something.,Yeah, I agree. I'm not sure. That's why I think the form is going to help because we're going to make it so you can't fill it out wrong. Yeah. And so they either fill it out or they don't fill it out. And if they just don't fill it out, then that's on them. And that's going to get communicated.,Yeah. So I have high hopes for that. OK, cool. Other things, I don't know. I think there aren't any pain points in terms of like me and Maria's and how the department runs, I feel like, I feel like that's been pretty smooth. And I think most of the things comes like externally from other departments, whether it be, like one of the things I'm trying to minimize her responsibilities, because I think it's like, I'd rather be able to list out what she does and not add any baggage that doesn't sound related to her role at all.

 And yet she tells me that whenever she goes into the office, people come up to her and they ask her to do things like, Can you look into this for me? Hey, can you look into can you help me with this? To me, I feel like That shouldn't happen. Um I I don't want Is it because they're like coding questions or something that like Yeah, it's like technical problems. Um, which even then I'm like I don't want them to bother you with that.

 And even if that was part of her role, in my opinion, I feel like that should all go through me first.,Yeah.,And then ideally, like in the future, if we have like five people on the team, then I can decide like, OK, who has the capacity for this? And I'll give them that task to look into that.,What about Like, maybe this isn't a good idea actually, but just having like a, a general support channel or something where people can ask questions on Slack and then either you or her could answer. I mean, up to her in person, interrupting her, you know, being like, Hey, you can put it in the channel. And then if I think meeting with you in person would be good, then we can meet or something. You know what I mean?

,Yeah, that's amazing.,Maybe that can help, like just general, whatever the kind of things that they're coming up to you about are, you know, maybe that can help.,Yeah, I think that's, I can try that out. Yeah. And then in that same note, I feel like, I feel like sometimes both of us can't really deal with, what we need to do for clients because of these random requests and being pulled like this way and that way.,Can you just tell people to wait like that it's lower on the totem pole or is it not really work because they're urgent?,I think it doesn't really work because one it's urgent and two they're probably like a really important client that like pays a lot of money or something. That makes sense. I'm not really sure if it's like understaffing issue but it's like how you can't even really hire someone for that kind of role really like general support like it's like oh we forgot we need this random ad made or something or like what is it okay gotcha um honestly it's like anything at this point it feels like whenever anyone has a problem they ask me or maria like design related you mean design related like tech related, even sales asking me how much they should charge a client for something.

 Yeah, it just feels like anything. And I'm not sure. Okay, yeah.,I guess what I'm trying to figure out is how much of that is just the nature of being a department director. Like, you know, yeah, people are gonna come to you for kind of stuff and then how much is stuff that we can systematize to help make it easier, you know? One thing I was thinking is potentially doing some time blocking where like you have a certain amount of time dedicated each week to these random things coming in.

 Like maybe you allocate two hours on Tuesday and two hours on Thursday. And just that's your time that you already have blocked out for people that need last minute requests or something. Again, I'm just throwing out ideas. And then your other work just works around that. But it sounds like there's kind of a systemic issue of people just not planning ahead with the design assets they need and not getting you enough notice.

 So that's something we may have to kind of discuss with Mitch and figure out a better process there, you know? Cause there, yeah, there shouldn't be like a crazy amount of last minute stuff, you know? Should be the exception, not the norm. Okay, cool. Well, I'm doing a ton of work with Mitch right now and the whole paid media team. Like there's a ton of work going into helping them with their processes there's a lot that's going to improve.

 So yeah, that's exciting.,Yeah.,It's going to be a lot of work this first quarter and you know, this whole next year basically, but I think you're going to see a lot of really good progress. Um, but I think the best way to help me is just stay in communication about issues you're seeing. Like you can never bother me too much. Like I want to have a pulse on like what's happening. Are you still getting tons of last minute stuff? Like, uh, just keep me posted, you know, cause that's the only way that we can fix things and make things better.

 So the main things are too much last minute stuff, people asking Maria too many questions, and interrupting her in person, and then not filling out the forms properly. Anything else you would add to all that?,No. Yeah, I feel like the I feel like those are the main things. Okay, cuz yeah, I do believe and maybe Maria is coming back tomorrow and we meet but I can get her insight if she feels like there's anything operationally like internally and our department that she feels like Is a pain point to her.,Yeah. Yeah.,I Yeah, because from my point of view, it feels like we have a good handle on things. But yeah, it'd be good to get her opinion when she's back.,Yeah, cool. Well, yeah, let me know on that. So yeah, that's good. Let me consider all this and take it from there.,I could also get your input. I'm not sure if Preston's, he probably hasn't. But there's a new-ish role that we're trying to hammer out that is in charge of those PPC design requests, as long as AB testing and all of that stuff. Has he mentioned?,I haven't heard about that, no.,OK. OK, so I do need to work on that stuff. I'm not sure what the communication supposed to be anymore? Should I? With hiring? Yeah. Should I consult you for all that? Moving forward, you can talk to me about all that kind of stuff.,And then anything I need to talk to Preston about, I will. But yeah, basically, all I really need from you is just kind of a detailed description of what their day-to-day is, what their skills need to be. Is time zone important, or can I find someone that's in a more distant time zone. Yeah, just all that kind of information so that then I can write up a job description and post it for you. Yeah, and we can run a job hunt for you.

,Awesome. Thank you so much.,Yeah, absolutely.,Yeah, send all that over and I'll get it going for you. All right. Is there anything else? Or is slack slack is the best way to reach you if you have anything any updates Yep, I'm in slack all day every day 24 7 on my phone on my computer.,I'm, just kidding Yeah, you can definitely hit me up there. Uh, if you ever need a chat feel free to huddle me or uh, I can book a call with you and uh Yeah, feel free to reach out anytime. Definitely. All right. Yeah, and if you get any other follow-up thoughts or whatever feel free to shoot me a message.,Oh another question is there anything I should be working on in terms of like the getting the forms up and running or should I wait until you finalize your plans and everything?,Yeah I would start definitely uh thinking about it like what kind of questions you want in there and it would be very granular but not so granular that it's going to be a total pain in the ass for them to fill out every time you know so that final That fine medium of getting everything you need, but also hopefully not too big of a deal for the paid media team. I would also think about asking questions in a way where it's just a checkbox instead of making them type things in.

 Because what I've found is when it's something you have to type, people are really lazy, and they won't put in very much information, and there's not much context. So asking questions that give you context text without them having to type.,Yeah, makes it easier for them.,Select all the dimensions you need. And it's just a list of all dimensions. Or if it's just all, hit all. Don't ask them to type in dimensions. Things where it's like, you can make it very systematized, I would recommend doing that. But definitely think about it. And then I am going to work on, that'll be part of our eight-week sprint. We're going to be setting up forms. We're going to be documenting stuff.

 Creating any LinkedIn channels. We need to make all that kind of stuff. So Yeah, just hang on for now, but definitely if you want to think about it brainstorming. Yeah Yeah, all right, well cool thanks for your time Shannon really appreciate it for meeting you too see ya

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hope you had a great Christmas, and happy almost New Years.

I finished doing 1 on 1's with the entire paid media and design departments. Basically interviewed them looking for pain points, room for growth, etc.

This will educate my 8 week sprint plan that I will be rolling out later this week - with a primary goal of raising NSM's and increasing NRR through improved systems and department optimization.

Things are moving along really well so far! Let me know if you want to chat on Thursday before I roll out 8 week plan!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or tomorrow after 1030

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I could do anytime this morning

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Perfect thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: See you then

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What time works best and I'll fire over an invite?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We've spend over $1300 on boosting that so I don't think we should run any more ads for that role and just work with the apps we got

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I noticed the paid media role is closed on linkedin, were you able to find someone?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maybe only shows on your end when you create it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maybe since I didn't create it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Odd, it's showing no open roles on my end

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Want to make sure we get you someone good

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just to be sure we get a second set of eyes on it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I review message and challenge before you send out?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you need help prepareing the challenge and challenge message?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Kk cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: gotcha!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Looks like you have 82 applicants on workable, that's great!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok gotcha, that part is gtg then

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm working on hiring stuff rn if you want to send over a simple bullet list of who you are looking for

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Here's my 8-week strategy sprint about ready to go: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: stoked

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sounds great!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yes I'd like to make Kevin's role more official. So he knows his job.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Laurent's SOW looks pretty straight forward.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Here's an email draft for you:
```Subject: 2025 Department Optimization & 7-Week Sprint Initiative

Team,

I'm writing to share some important updates as we kick off 2025. As many of you know, Jordan Dahlquist has joined us full-time as COO and has been conducting 1:1s with team members across departments to understand our operational challenges and opportunities.

Starting January 1st, we're initiating a 7-week sprint focused on department optimization with the primary goal of increasing our Net Revenue Retention (NRR). Jordan will be working closely with world class productization strategist Laurent Matson to develop a comprehensive framework that will help standardize our processes, improve cross-department communication, and create more efficient workflows in the coming months.

Key updates:
- Jordan now has full authority to execute operational initiatives across all departments
- All department heads (Mitch, Shannon, Trevor) will now report directly to Jordan
- Department-related decisions and escalations should go to Jordan before coming to me
- The sprint will focus on implementing new systems, documentation, and processes to support our growth

Our goal for 2025 is to exceed $9M in ARR, with a significant portion of that growth coming from improved client retention. This sprint is designed to build the foundation we need to achieve this while maintaining our high standards of service delivery.

Jordan will be rolling out a detailed sprint plan to each department this week. Please give him your full support as we work to level up our operations.

Looking forward to seeing what we can accomplish together.

Best,
Preston```

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome thanks

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Thsi was my call with her this morning: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Fabiola Morales expressed her concerns regarding the paid media department, citing feelings of being undervalued and unheard, particularly when her proposed strategies were dismissed, which affected her motivation. She highlighted significant miscommunication, especially when clients escalated issues directly to Preston, and emphasized the need for improved collaboration among team members. Fabiola shared her experiences managing a new account, noting the challenges of adhering to strict procedures while trying to achieve optimal results, and the difficulties of balancing multiple responsibilities within tight timelines.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can meet now if you want

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Probably need it for all AM's

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U0106DW71NJ|Mitch Marowitz> let's add this to our list of things we are working on in the doc

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: @mith

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And need to re-communicate to existing clients

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: the entire onboarding process probably needs a revamp

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U0106DW71NJ|Mitch Marowitz> can you setup a weekly repeating call on Tuesdays with you, Me, and Sam for a time that works for ya'll?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Lmk if this works

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So we can cancel things we don't need etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is there a place where we keep track of subscriptions?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What I would love to do is build custom web based dashboards for every client.

So they have a login to a portal where they can access live time data, have a roadmap documented, a team outline of who does what, everything they would ever want to know.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: But that's fine for now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I prefer meeting swhen we are fresh int he AM

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Little late but that works!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: what's funnel

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We can sideline the convo in direct to not bother preston

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah we should look into that. I've used DashThis quite a bit

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: + have messages, alerts, timelines, benchmarks, etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We could pipe in data from everywhere

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And then the client can do everything from one place

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We could hire a guy to develop custom portals

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What would be epic is our own custom dashboards

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah we could pipe data in from a manual sheet tho

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: For now lets' focus on the important stuff we are working on

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We can figure that out down the road

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So that should work out perfect

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah it will take a month to find someone anyway

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Want to make sure I'm tracking subscriptions and deleting any we dont need

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I get access to our subscription tracker?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: YU8$p@!%X&KO7Qg8

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I built out a preliminary design dept. form, here's my login. Can you check it out today or tomorrow and we can start working on optimizing it together?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I also synced it up with your asana space so it will create a task and assign you as well as add maria as a follower.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You'll also get a slack notification DM

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can show you how, it can get messed up pretty easily if you're not careful

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can help if you need to add anything

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Check out the Logic section also, you may want to add to it

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Another cool ai dev app to check out ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I could try to go thru QuickBooks to look for subscriptions and add them to a sheet

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: How can we get that done?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yes! Was just asking about that yesterday that's perfect. Will add today thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's make it happen

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Welcome back! How was your vacay

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Made a sick Typeform for the design dept. for requests. Has dependancies and project categories etc. If you guys ever need something like this for your dept. let me know and we can get it built out.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Also I don't have access to NordVPN since I set it up with your emails - how much was that again?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hello! I'm updating our subscription tracker with the latest tools we signed up for. What is the total ongoing cost going to be for GPTZero so I can note that down?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I just need to add each one to our tracker sheet

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you have the pitchbox info we can add to the tracker?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Thank you!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Did you have a good Christmas?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Happy near year to you as well!!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey all - I went in and added every software sub I could find in QB. Now I just need each of you to go through and help me identify the yellow highlighted info.

Some of it we may not even need/be using.

Also, some things you can delete if it doesn't apply, like I see many charges from Connectively so I assume it's a per project fee not a subscription etc.

Can everyone take a peek this week so we can try to have it updated moving forward?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I also want to ensure everything is in Lastpass. I added all my subs to Lastpass now, but if you see anything missing please double check

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Should I send out a reminder cal invite to review subs? What do you think, monthly or quarterly?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hi Aleks! I'm updating our subscription tracker with any new tools. Can you send me the list of all tools we setup for you that we should add to our tracker? I'll also need the admin login. thanks!

For PR we had Claude, GPTzero, etc. but I can't remember if we had any tools setup for link dpt.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: to get it cleaned up

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: in the coming weeks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just would be nice to have eventually

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: No rush at all

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: But if not, then just put user email and then we at least know who owns it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Most platforms you can go into security settings and create an actual password

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It would be cheaper/better if we create a company Chat GPT account and then add team members under a main admin...

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Who owns the two Chat GPT accounts?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Good to keep it centralized because we could start doing company GPTS's

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: How about I go into the login one, and add Preston, Mitch, JD as members and then we can cancel the duplicates

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or did you talk to him already

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So he can be prepared with info

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Should we ask trevor to have a performance review ready for the call later for pr dpt?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: no worries! There's no rush, thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It's the same as any type of account where there's sub users

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Login would have it's own account, and then all the sub members are on the payment plan but each user's prompts and everything are totally private

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U025QMUHGTD|Preston Powell> nobody can see your prompts in a team account.

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: 1 on 1 Meeting - Jordan & Nick
Meeting Participants:Jordan Dahlquist,Nick Chepkevich
Start Time: 2024-12-31T09:58:37-08:00
End Time: 2024-12-31T10:09:10-08:00
Transcript: Hey, how's it going, Nick?,What's going on, Jordan?,How are you? Pretty good. Yeah, yeah. Doing great. Hope you had a good Christmas. Yeah, I did. It was awesome.,Nice. Just hanging out with the fam. Nothing too crazy.,That's all we did. Nice.,You got any big plans for tomorrow?,Just watching football, college football probably. Nice. Awesome. Cool.,So yeah, we'll jump right in. This call is pretty quick and easy. We don't even have to use the full 30 minutes. I basically just wanted to touch base and ask you if you have any feedback, pain points, anything you could share about the media department or web serve in general that you feel like could use optimization? Because we're going to be doing a seven-week sprint starting in January. And I'm going to be working with the department heads to roll out better systems, better processes, better everything.

 And so what I'm trying to do is identify pain points that are causing any issues for you in the day-to-day, things Might be causing clients to have a bad client experience that could be better Just anything like that So,you get I was thinking about this before the call because you kind of mentioned a bit about what it was about The only thing that really comes to mind and it's been It hasn't even been an issue like for a long period of time, but over the past month We've just had we only have two people on the design team and they've been on vacation like on and off for like a month And we've had to outsource some land and it's just, I've had like three or four new clients and I've had to get three or four landing page.

 That's been my biggest pain point recently. And you know, it's not their fault. You know, people go on vacation. We only have two people like it happens, but that's, that's been my biggest issue as of late.,Got it.,So slow turnaround or something. It's that, but I've, you know, I've been voicing that to like Mitch and Sam and I think they've honestly addressed it by basically one of the, one of our bigger problems is, actually was we would tell new clients we could have them a campaign, a landing page, everything dialed in in seven days. And I think we've decided, I think they're going to go with a month. I suggested two weeks, two weeks would have been plenty of time, but I think they're going to go with a month.

 So if that's the case, that addresses that whole issue right there.,Yeah.,Okay. Got it. It was just, you know, it was like sales people over promising and like, I get you have to do that to make a sale, but every once in a while, it kind of came back on the media team and,it just like made our lives a lot harder, you know? Yeah, that makes sense. Okay. And then have you been following their submission process too for a design element? Cause I know one frustration Shannon shared was, I don't know who, but just certain people not submitting their requests in a time, like with enough time or not providing all the info. So there's too much back and forth or I'm missing information.

,Yeah. So, I mean, I, I was always timely with it for sure. There were a few times where I, you know, I didn't have the info at the time it wasn't on there. So I I'm certainly a bit guilty of that. Um, but it was just like the whole thing in general in December was completely broken and, you know, not their fault, not our fault. It was just a big mix of things that kind of came together.,Got it. Okay. That's good to know. Um, but yeah, I think we are moving to a month, so that, that Yeah, at least then if we get it done quicker, we only look good to them. You know what I mean? That's what I've been saying for a while.,Yeah. Yeah. It's just like we promised it for a week and it's like, okay, that's great. Like that we can maybe get it done in a week, but we're rushed. The design team's rushed. We might not get out as good of a product. And then oftentimes we might be behind a day or two and then that looks bad. Yeah. Okay, so whereas we could just be up front and say hey, it's gonna take two three four weeks whatever and we're good Yeah, got it.

 And we're more than likely gonna be done early at that point.,So you're right It does nothing but make us look good. Yeah Okay, is there anything else you feel like could help you? Do you feel like you need more training in anything? Do you feel like you have enough resources software tools?,100% on that. I mean I've been in I've been doing this like addiction treatment advertising for so long that I don't like, I don't know, I know how to do most of it. Um, the training stuff, it's like, of course we're going to come across things that like, you know, a client, a new client might want on, let's say, let's call it CTM. Like they, we actually, so recently we had a scenario where a client wanted like their scoring to be able to be done on the phone.

 So instead of them going into CTM and marking stuff, they wanted like a dial menu. So after they hang up the call, they hit star and then they score one for a VOB two for a We've never done that but we had to figure it out and you know, Mitch has never done that either So it's like, you know, we just get it out together and that's fine But like anything that we like is our standard practice and all that I mean, I'm good on that as far as the training goes just yeah,,I've been here forever.,So Okay, great. And then how do you feel like things are going culturally your relationship with your team? Your relationship with Mitch anything you want to share kind of privately and that's I have no issues with that at all.,I You know, we and Mitch get along really well. We've been working together for a while. Sam's great. Keaton's great. Bobby's great. You know, I don't think anyone's like overbearing as far as, you know, you know, Mitch has a lot to deal with and he has to answer a lot of questions. I think people do their best to, you know, not overwhelm him with that kind of stuff. But I think everybody works pretty well together.

 OK, you know, we're implementing some new processes, obviously. Obviously, there's been some pain points. And I like so it's like the NSM dashboard, you know, I missed a week or two on that and I think Bobby did too and you know now It's dialed in it seems I'm hitting it every week. So it's just you know, cool. I wouldn't call that a pain point It's just adjusting the new processes. It's gonna take a little bit of time.

 Yeah, that makes sense It can be kind of a pain.,I know that for sure.,I wouldn't even call it a pain It's just you know, it's not been a part of our routine and now it's like, you know get it done so it's just you know, it's just something new and Yeah.,Do you feel like there's anything else besides the kickoff timeline that can help improve the client experience?,Let me rack my brain a bit. I don't know. I don't necessarily think so. I mean, it's just, we, there's some tough things like, you know, so on any addiction treatment campaigns, like we run different And the one we know works well and that we can get the results that we typically promise these clients, like it takes a minimum of like 50 to 60K. And I mean, I know this isn't going to change, but it's like we get a client for 15K.

 The odds are that we're not going to get those kinds of results for them. I mean, we could get lucky and make it happen. And you know, the first couple of months could look good, but it's just really, really hard to get done. But I mean, we're still going to take those clients. Is what it is.,Yeah.,I mean, it's definitely just, uh, it's hard. Like we, we've been, we, we get creative. We do some different things, you know, instead of doing that nationally, like near me campaign and all that, we'll do like some more localized stuff that's strictly, you know, say the company's based in orange County, we might advertise in San Diego and orange County. And it's just a lot tougher to, to make those accounts work.

 And I mean, that's nobody's fault. It's just, that's just the name of the game. And we're still going to take on those I mean, there's nothing we're gonna do. It's just yeah, it just sucks when you get a client and you know This is their budget and you can pretty much guarantee. They're not gonna be around in six months Yeah, that makes sense.,Okay All right.,Well, cool.,I think that's it man. I don't need to waste any more of your time That was pretty much it just wanted to Get it from the horse's mouth Anything you wanted to share so yeah, no doubt.,No as you know as everything goes, you know know, these are just, I feel like everything I mentioned is just, you know, normal pain points of any business. It's like, you know, there's nothing fundamentally broken. There's no severe culture is nothing like that. I don't think we all work pretty well together. I'm happy. I think most other people are happy. So nice. Yeah.,Well, great. It sounds good, man. Um, I appreciate your time and I'll let you go. And, uh, that was helpful.,Appreciate it. Of course. All right, man. All right. See you, Nick. All right. Have a happy new year. You too. See you.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ALso Qwoted? Do we pay for that?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ty!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So <@U0106DW71NJ|Mitch Marowitz> if there's something that could break, then we always use the Login user for that system so it's evergreen

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok we should get that added, could you? I don't haev the info and I don't see it on the card for some reason

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm getting applicants rolling in for the Paid Media Analyst role (<@U04EKCA5R5X|Sam O'Leary> if you aren't aware of this lmk).

We need to get a good challenge setup.

Do you have an idea for what we could make them do for the challenge?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: hey ya'll

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm free anytime if you want to jump in early

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: How about this:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Paid Media Data Analysis Challenge
The Task
You have a Google Sheet containing 6 months of campaign data across multiple ad accounts. Create a single-page analysis report that includes:
1. Calculate month-over-month performance metrics:
    ◦ Cost per lead
    ◦ ROAS
    ◦ Click-through rate
    ◦ Quality score averages
2. Create a summary identifying:
    ◦ Top 3 performing campaigns by ROAS
    ◦ Bottom 3 performing campaigns by CPA
    ◦ Most significant performance changes
3. Write 3 bullet points of actionable recommendations based on your findings
4. Provide a 4 minute max loom video interview of yourself answering these 4 questions:
    a. Why are you a fit for this role?
    b. Tell me about a time you solved a problem or created success for a client account.
    c. How do you like to manage your day to day work flow?
    d. Why are you looking for a job?

Submission Format
• Include a pdf document with your bullet points in your email submission
• Include link to interview in your email submission

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan & Preston Weekly Meeting
Meeting Participants:Jordan Dahlquist,Preston Powell
Start Time: 2024-12-31T10:56:30-08:00
End Time: 2024-12-31T12:00:00-08:00
Transcript: Hello. Hello.,Only you can make me whole. Only you can fill my soul.,Touch me. It's all I long for. It's all I long for. Hey, how's it going, man?,It's going good.,How are you? Really good.,Just cranking away on all kinds of stuff.,Cool, cool. So. Yeah, Trevor, was there anything on here outside of what we were supposed to talk about? I thought I got everything, but Yeah, not really.,I mean, there's like all kinds of things we could talk about, but I think you nailed the most important things right now.,OK, let's look at Lawrence thing again. Obviously, we got to at least ask him for a discount.,Yeah, I feel like, um, where'd the pricing go?,Is there any pricing in it at all?,Um, hang on. Yeah.,It's at the very bottom. Uh, very, very, well, almost second page from the bottom.,Oh, okay. Five weeks. OK.,So the thing is, I was reviewing it again this morning. And it's like, I'm sure it's going to be epic. And I'm sure we need it. But it's like phase one and two doesn't even really solve our immediate issues. But they help us get there. But that's 25k, and it's not even getting us to our main issue yet.,I think that's OK. Yeah. I don't know. I just want to spend a quarter getting to phase two. So that's all right. I think it'll be worth it.,Cool.,I'm just going to ask him. Cool.,Yeah, I think it's going to be great. We love your proposal, but have Let's look at it real quick Anything in there because I'm gonna ask him for five grand off anything that we're we want to trade So I don't I don't How important is positioning for,you right now?,I feel like that's less important, but beneficial, obviously.,I'm just going to say.,I got an idea.,Hey, instead of asking for something less for deliverables what if you just say like hey can you give me 5k off if I promise you a three-month retainer after phase one and two like we signed for a three-month retainer,now hey uh I'm I'm just gonna ask him this I'm gonna say since we're focusing so heavily on paid media and going into this we were thinking we would Let's focus on all service areas. Can we have 5k off? What do you think about that? I don't understand why he would. What did you say? I didn't really hear what you said outside of can we have 5k off? Since we're focusing on paid media, what? I don't know if there's anything else that you want to add.

 I thought that his proposal is for all the services. Kind of I mean, but the focus is paid media, which I think it needs to be anyway. But say that, though, from what I understand, right at the top. So blah, blah, blah. Wait, where did it go? Phase two, so Discovery phase is two weeks.,No, that's phase three. He missed. Oh, wait, I see.,Yeah, phase one and then phase two. Phase two, specific focus on paid media, right positioning one-pagers, detailed subservices and deliverables, create a capabilities deck, create proposal versions, deck, align assets with sales and client onboarding. Marketing, no. Much of the updated web service. Cool. Yep. So I think we're good. OK, so I was going to say it. We just want five. I want $5,000 off, and I want them to give us one payment now and the other payment at the end of the five weeks.

,The only thing I was going to say, though, is like, Just because paid media needs to get resolved, I don't feel like we should not work on the other services, though.,Okay, let's let's just bring that up.,I think I don't like equal energy into all of them and hopefully all of them get solved because they all have the same problems. They just don't all have the same symptoms.,You know, I'm saying.,Like, you know, our pain point right now is pain paid media, but in the big picture, we actually need it for everything really bad.,Yeah, no, I agree.,What I would almost say is like, I'm willing to pay the 25k, but I need it across all services. Or if you want to just focus on paid for now, I'll pay 15k. You know what I mean? Or something like that. I'm just like right now.,ideas but,We will have to do this and for SEO, and if that's the case, I don't know that I can afford 25K again. So if that's the case, I'm hoping we can get a little off the price, maybe 5K in the first phase, because I can't Yeah, that's insane. Honestly, like even the 25K like,,I don't want to shoot myself in the foot here, but it's like a lot of this stuff I was going to be doing anyway to help you.,Yeah, I think we kind of want him to work on on this anyway, though, just because he so freaking good at it. Yeah, no, he'll be amazing. It's like, it's gonna be epic. For sure. If we know because Cool.,Let's see what happens. All right, so we can cross that one off. Yeah Let me try and call him Just out of the blue or I'll text him actually Six four six six two zero Here he is. Three minutes for a call about proposal. We'll see if he answers that and then I'll just leave this drafted. I'm sure you will. Cool. So regarding like all hands meeting, I think that it's really important, but it got pretty messy last time because it was like a free-for-all.

 And so I think with the proper meeting agenda, and maybe you would be the one to run that, I think you need to come up with this structure. And then maybe we'll make a slide deck for running those meetings, just so that there's something on the screen, and we just go through it in order. And if people start talking out of turn, you're like, oh, yeah, yeah, you're going to be able to talk about that, just not right now.

 So I think that's you. And then I have a question on that before the next one.,Are you imagining? What I put here, going over NSMs, NRR, casting vision, updates. Is there anything else you would imagine coming out of that meeting?,Any goals you have? Yeah, so monthly, I probably want to talk about financial performance and NRR. The biggest thing I want to, I think NSM stuff would be for departmental meetings. Yeah. And so who's required to be on each one of them should be defined and we should present that to everybody. And then, yeah, so I think everything should be focused on client retention there. Casting vision, sharing updates, public announcements, resolutions, yep.

 And then there should be like an open dialogue for like, like, some like, blockers, you know, or like, hey, this client's not getting to hear because the landing page is delayed. Can we get updates on that?,That'd be a department thing, though, because like SEO doesn't want to hear about what's going on issues in paid media, you know.,That makes sense, except for maybe then there needs to be a cross-departmental weekly, one with SEO and design, and one with paid media and design, which I think that one could be pretty short. But just a weekly check in between those. What if we did a Slack?,Yeah, what if we did, for the cross-departmental ones, what if we did a Slack instead of a meeting.,What does that mean? I don't know.,Basically, they have to send an update in Slack on the status of their stuff.,And if a discussion needs to happen, then there's a thread started. Yeah, that makes sense. Okay. All right, cool. Wait, wait, wait, sorry. I was typing and I, so I don't get what this standup is. Mike, you're saying.,This whole thing started with saying you want to open dialogue time to discuss pain points with clients, right? And I was like, hey, I think that's not a good use of the entire company's time to do that on one call. And then I was like, then you were like, what if we do cross departmental meetings? And then I'm saying, I think that'll end up being too many meetings every week. I think it's like overkill.

 And so what I'm suggesting is a cross departmental slack stand up update. Basically, all it means is like, each department head sends an update about any issues that they're having with any of their clients to the other department heads who are related to it.,And it's like a weekly conversation they have via Slack. OK, that makes sense, but but it has to happen.,Yes, every week at the same time.,Yeah. OK, maybe there's a weekly update same time.,I think we just need to be clear that the full team call is not a time to discuss why a client is churning. Yeah. Or the ins and outs of anything. Really, this client will turn.,This client is onboarding blah, blah, you know, just like top. Yeah, just like, hey, like maybe. Yeah. All right, cool. And then for, yeah, meetings with associate directors and account managers weekly.,I definitely think that's good. It sounds like they do it a little bit, but it's not structured like you're saying, and it's not formatted or anything. It's just kind of random. So I think that's a really good.,initiative.,And I think, yeah, I think the associate directors need to be like, on that call, I want them to actually walk them through the ad accounts and walk them through the numbers and things like that. So it's like they're really aware.,What do you think should be because they need to get on a monthly Oh, and then we need to Laurent's going to help us with this, but interim format for what's it called? Client monthly review meetings?,Monthly.,Leadership sync. Cool, I mean I can help.,Yeah, Lauren will obviously help with that too.,But yeah, that's easy. We can get that done. Yeah, so that one needs to have. Uh. Happy Account manager issues with performance. Introduction of performance design. And then I think you want to talk about Kevin. Yeah, that'd be great.,He mentioned that his job title has changed 100 times, and he doesn't really know what he does, or he'd like some more definition.,Kevin's going to tell you that, though. Yeah Kevin always wanted a little bit more structure but but Kevin's valuable to us in a different way because He's like a multiple. Yeah, because because He can do SEO Design really well But he's really smart and can help us with all kinds of different things. So I would be OK with giving him a new title. But had we locked him down in a title, his potential would have been kind of compressed.

,That's why I think actually an operations title is better, because operations goes everywhere. It's like, basically, we're giving a title to what he's already doing.,Increasing as operations input Okay, what's uh, so you could be like associate director Something like that.,I don't know.,Yeah.,Yeah, I think that's a good title uh, let's let's uh figure out on next meeting though cool, sounds good just Just because there'll probably be be like a wrap up. OK, and then. So what are we going to do to begin tracking NRR?,That's a interesting question.,Well, we need solid numbers to be able to track it. And you created a 2025 NRR tracking that I have here. Where I'll send you the I'll slack you the link. Although I created it based on what your cousin or whatever sent you. OK, screenshots, but I don't know how to get the numbers in here. That's the next question, I guess.,Quickbooks. OK. Yeah, yeah, yeah, yeah. So. Well, I think we need to pull in Seth. Who's Seth? He's my brother, but I think it will be cool to work on in our tracking with us. Take data from QuickBooks and So let's try to do it for January, and let's just see what challenges we run into. Because ultimately, I don't think we're going to run into a ton of challenges. Yeah, because look, so you've got QuickBooks right.

 So if I go into if I go into QuickBooks, and I So let's look. Oh, we're pretty good. For some funding should I get it what available oh it's just for it's just money that'll come to us tomorrow. And they're like, oh, for 10 bucks, you can have it today. Yeah. Fucking dicks. I'll give you a hamburger today for a dollar tomorrow. Oh, wow. That looks bad. We're owed a lot of money. That's normal for this time of year, though.

,Everyone's like off their computers and not checking emails.,It's fine. It'll all come in. Yeah. It'll just make January look really great.,Maybe.,We'll see. So if I go to just reports and get a P&L, I think I can run a P&L by department. Oh, cool.,So it's already breaking.,So that should be pretty Pretty easy then. Yeah. You can just go to paid media and ad spend. OK. Hit run.,Hit run.,Hit run. Sorry.,I thought you were going to close it.,I had something in the way. Oh, OK. It wasn't showing up. So that doesn't look right. Yeah. But that's OK. Hang on, I'll be right back. Yep.,Hmm.,All right, I'm back. So this just shows growth. So basically, the thing that's tough here is, so here's all of them. And so you would have to go through here. You'd have to get information on what client was lost. Right. So does that make sense? Yeah, basically, you just have to go through and see why there's less money or more money and identify which client was there. But what I'd like to do is just change And then rather than that, we can just use a class rather than the service.

 Customize, filter by class. And then here's the good classes, paid media, run report, bam. So then let's customize it. Let's go months report. There we go. So we have the classes set up back to June. They go all the way back in time.,So basically, how do we know? So basically, my goal is to make it so that each month is the same or bigger than the month.,No. No, because like, so for NRR, right, let's say that paid media had $140,000, right? I'd say that they made up $8,000. They lost, you mean? Yeah. And yeah. Yeah. OK. OK, so who?,Can I get someone's help to track this to go in and figure all this out? Because this basically just takes a bunch of going in and bean counting.,Yeah. That's what Seth is going to do. OK. So let's say that last month's revenue was $140,000, and we lost $8K. Well, let's say we got $12,000 in new clients. We don't it. The PPC team doesn't get credit for that. They only get negative credit here. So that doesn't matter.,4k credit. The difference? No.,Because the PPC team didn't bring those clients. If they I see what you're saying cross sold or up sold So that goes away Let's say that this is 50 or let's say this is 20,000 Right and now I can add it so So last month's revenue really doesn't matter. It's really just a Yeah, it's just you start at zero You lose 8k and then you make 20k back so equals this plus this Plus this Yeah, so they Enter our 12 Okay, basically.

 Okay, I got you now.,Cool.,And then, so they offset this by doing this. Yes. And they offset this by not doing this, by retaining clients. Yeah, totally.,And there's zero of the cross and upsell happening right now, so we just- We're going to have to push really hard to get that happening. Also, we also need to be working on losing less clients, too. So it's like a two, we can attack it from two directions, right?,Yeah. Yeah. So that's cool. I think losing less clients is the most important. Yeah. Lose less clients.,And then the cherry on top is cross and upsell.,Yep.,All right, so how fast can Seth start getting this updated and done so that we're ready to start having these meetings?,Say that again? How fast can Seth get this cranked out so I can start having those discussions?,with the team?,We just have to structure it. So when you go back to this sheet, so these meetings you're talking about, this should be monthly. So maybe Maybe in week two so in week one We should be doing some sort of reconciliation of the prior month of the clients that churned and so like Here if you go back into there's a lot to it. Don't know the best way to do this But if we go to reports, let's create a report.

 It should be single object and that object should be deals. When we go in here, we should see Um... Uh... Oh wait, we should filter. Uh...,Date entered. And then. We should be able to see all of those. But they updated a bunch of them at the same time. Yeah, so it just looks like you lost a ton of clients in one month. Yeah, but that's because I haven't stayed on top of it.,That's a lifetime value? Like monthly value or what is because it says in company currency total contract value so like some of these were only worth 6500 bucks for an entire year or they just only lasted like one month basically no we changed,the way we reported they'd been here for a long time those ones so that was their monthly fee it was but we're not reporting that way anymore okay so it It'll be accurate. We're trying to do booked revenue. Got it. Yep.,Sounds like week one of each month, Seth just needs to go in, update, churn, crosssold or upsold. So how do we track cross sells and upsells? How does that get pulled for Seth? Is there like a...,We don't track... It at all right now.,Yes, I mean, how do we start tracking it?,I guess. Why don't we make the associate directors work on that because they're going to get paid for it.,Like the way you think?,Yeah, yeah, we're going to we're going to give them we got to come up with a bonus structure for that, too. I think we pay them. A flat amount like maybe. Let's do this. Well. One idea, because with operations.,The real goal is to drive efficiency in better systems.,I think we charge we pay them 3%, right? Of the booked revenue, so let's say 24,000 is the average. Performance design. Who's they? I don't know who they are. Wait, wait, wait. The associate directors. Okay. Yeah. That's a good bonus for their cross sell. Like Samantha or one of them, they get a 3% on any cross sells.,I think that might be too high.,Let's give them 2% Or should we just give them a bonus on their NRR That's a higher percentage it should be higher on NRR I agree with you.,Yeah, that's what we get out here cuz they're not We want them to stop losing clients and cross sell so we should motivate them on both Yeah, so if they get NRR to zero, I think we get give them,like thousands of dollars. If they get it to 94%, I think that's our goal, right? We want NRR to be 94%. And so if we're able to get our NRR to 94%, they should get a big bonus. And that bonus would Quarterly bonus it should also be going. It should be also spreading down to account managers because But remember their goals are different Yeah, their goals are around NSM attainment and CSAT scores Yeah, okay, I got you It's all gonna feed back to to the NRR though.

 Exactly. But we don't want them worried in the financial metrics of it all. We want the associate directors worried about that. That's really smart. Cool. So that the account managers can worry about, how are we getting results? Am I doing what it takes to make these clients happy and get them results? Yeah. OK, cool. OK, I like it.,That's awesome.,So the associate operations, you're saying you want to bonus him, too, somehow. Is that what you're saying?,Yeah.,Is that what you were saying? Or were you talking about the other associate directors?,Maybe I didn't. I mean, we can bonus him on the same day. It just has to be, well, it's less granular, right? Like if each account manager is worried about hitting 94% attainment, or each associate director, and, you know, higher up the chain, they're worried on their whole department hitting that as a department director. And then as operations directors, they're worried about every department hitting it.

 Yeah.,So they should get a bonus that's based on the performance of each department, I guess.,Yeah, I think so.,It's the same amount and the same structure, but it's like each department has its own bonus coming out of it for them.,Yeah, yeah. There's a lot here, Jordan. There's a lot. So cool. Well, I think we have just a general handle on it, at least. But yeah.,So could we have Seth start reconciling December next week? And then I could just kind of start really having those solid NRR numbers and being able to have those meetings?,Yeah. Yeah, totally. So we need to schedule a meeting with Seth, which I feel like I did. I think I scheduled a meeting with Seth and Kevin.,And then I think we need to give Kevin, oh, you to discuss it on the next meeting.,That's right. Oh wait, let's just do this here. I guess Kevin, JB, Seth, NRR, tracking, Yeah, we should work Seth's little butt off. And then once he starts doing good, we'll give him a proper salary. He makes like 60K or something. Oh, wow. He's our least paid employee, but it's the best job he's ever had. He's a young kid. He's super smart. He knows like Python, JavaScript and stuff. You know, he's never had a real job or anything.

,He's just like a computer guy. Yeah.,Cool.,So I just invited them to the end of the NRR tracking sheet so they can start perusing that.,I try not to fuck with Seth too much just because he's my brother and I want to be managed by other people and fired by other people. I just don't want to get involved.,Yeah, that's good.,Oh, yeah, and then for you.,I hope he doesn't get fired, but he seems pretty cool. I don't know. For our weekly meetings, do you like using Notion? Or I'm wondering if we could move our meeting agendas into a place where we can track how things are moving. And it could be Asana, it could be Notion, we could just use a Google Doc ongoing.,Do you have a preference? To track what?,You're in my meeting agendas and tasks.,You know, it's kind of cool if you add a a tab that's like a new tab. Let's do a, you can create a project tracker. Insert. Oh wait, let's, we can add it to our chat in Slack. Create a new tab. It'll be a list. I can't see what you're doing, but Create a new list. Untitled list. OK, open our chat.,You and me. Oh, I see.,This is sick. I love this. And then you can just add. You could add Dropdowns you can add whatever that way you can we can track it in here And then you can you can assign? Does that make sense yeah, I love it. It's not letting me edit it though Do I have to get It should I have you only access yeah I don't know, unflag?,It says I have view only, I can't edit anything.,Settings, share list. It might have sent you an email. There you go. Sick. All right, cool.,Love that. And then we could actually keep this Google Doc going that you put here, and we can add a new tab for every week.,And then for like our random notes and stuff, you know?,Yep.,And then, cool.,That works. Cool, man. Awesome. We didn't cover everything, though. So, the trash stuff.,What?,You need to write an email to the department directors also.,And then Trevor, yeah.,And your vision deck. Let me see the original one that Directive had because it was like super comprehensive.,I have it here if you want it.,I can grab it. Let's see. It's right here. I'll slide I got it open. OK.,The email kind of just is an outline of what I'm already going to have in the doc. That's good.,It should be the same. Yeah. So here to Sam. This email though right here is not this needs a lot of updating Yeah, I'm gonna got it quite a bit Sam Mitch Trevor Shannon for now, that's all we got and We're gonna bring Kevin into it Web serves. I'm just going to do 1 to 25 Strategic plan. Should I include salespeople?,I don't know.,It's up to you, because it would definitely be good. The thing is, it's structured more for delivery departments.,Yep.,I think sales would need like a separate sprint.,Yeah, for sure. I'm down to do that though. Let's do it. But first things first, let's knock this out of the park. Identify. Okay.,operational efficiency, cross-selling and upselling initiative, innovation and service offerings, marketing strategy development. Okay, week one.,Thank you. Okay.,Um I think it'd be good too If you want me to start taking over more stuff so that people are messaging you less you should probably Intro me in some way as like hey Jordan's coming in as ceo moving forward like if you have questions about stuff go to jordan first I don't know. I don't know to what level you want me to be taking over that kind of stuff, but well That's one thing we didn't hit this week either That decision making process.

,Yeah.,That's going to help a lot.,Yeah, that's really good.,Getting that rolled out with people.,Uh, we can start getting you more freed up Yep We can work on this later actually though because I can't do two things at once. So what's next? I gotta get ready for the next meeting here in like a couple minutes. Do you want to rewrite parts of this? These weeks are not set up right. Yeah, can you paste that whole thing over to me?,Or just email it to me?,Or just send it in Slack. All right. It's easier. And then, yeah, if you want to make the timeline and strategy template, just Button them up once you have them and then you can you can write how you want So the strategy template I made one I already have that but the timeline template There was no link to it and I don't know what that is Well, he lays out like what's going on each week But it wasn't all that relevant to us anyways, so it's just it's just a drill down on on this section under Timeline.

 So like this stuff, it's like just drilled down further. Yeah, I already have that in the,Yeah, I'll update that. Cool.,Yeah, however you want to do it. I don't know that it's like super important.,We don't need a whole other doc.,I just don't think we need a whole other doc for that, because it's already in the sprint. It's already there. Cool. It's already in the big doc.,I made cool. Well, then yeah, if you send that to me I'll send it out to everybody and we'll go from there cool radical All right Well, I'm excited tomorrow's my official first day full-time. So that's cool. Nice Heck yeah.,Well tomorrow we're closed It's gonna be an easy day. Yes Yeah I'm gonna go in the office on Thursday. Hopefully people should be there, right?,Trevor will be there Mitch is going to like somewhere out by like Joshua tree today after work He ran in some air B&B. So I think he's gonna Gonna go out there and do hippie shit For whatever people do out there I love it out there. It's beautiful, but but it's it's turned into such a weird like I Do sound baths and I'm so spiritual. It's like screw you dude perennial sunning It's where people are like there's a whole movement starting where people like sun their asshole.

 That's awesome, dude. Do you follow Chad goes deep on Instagram? Yeah, I do.,I don't I don't see it like an entire he did like a group perennial sunning in on the beach in San Diego.,That's amazing.,It was hilarious. That's good stuff. Yeah, that's quality entertainment right there.,All right, well, is there anything I can be doing anything I can do better in terms of communication with you or whatever? Do you have one on one going with all the department heads? Well, that's what this format stuff is going to help me figure out, like what I want to go over with them on one on one.,Yeah, because I think we're like ripping apart the whole. The whole like way we do things and I think it's really important for them to be accountable to you. So just yeah, Trevor Mitch, you gotta have a weekly one on one with them forever and it might not be as structured as you like it. You could tell him hey, I'm still working on the structure, but I think that's really, really important. Because you need to Shannon's gonna be in the weeds a lot until that department grows and I'm willing to invest a little bit there, but I need to smoke to clear, you know, we just cleared out all of our Accounts we signed some big accounts So So I don't know in the next month or so.

 We'll figure out what we can invest in and where And then but yeah, so for now Shannon It could be a informal just check-in but you're gonna need to roll out a CRO service with her as something that could be cross sold or or whatever you want to roll out whether that's videos and and CRO, whatever it is. But it's something that's easily cross sold to paid media. And I think design is gonna be your easiest thing in the world to cross sell.

,I agree. I really wanna get the video stuff going.,Like, when do you think we can do that? Are you thinking like in a month or sooner?,Well. Another thing though is that Shannon is gonna need some support. Because that'll add on more stuff. Yeah.,We're going to have to hire. We're going to have to come up with the whole plan so we can start.,So I have an idea for you. I have a friend in El Salvador. He used to run bids for me and his salary is like 3,500 a month and he's freaking awesome when it comes to managing animators video. He can be client facing. He has perfect English, like literally American English and Is he a designer himself? No, he's not. But he's a manager, like he can manage like 40 animators if he needs to. You know what I mean?

,Well, let's figure out, you know, where he fits into the company and hiring him. What if we bring him in part time because he only wants part time right now?,What if we bring him in halftime to work in the design department and build the video team and then we start rolling that service out like as quick as possible?,So you're telling me, though, that he wants It's $1,750 only for halftime? Probably, yeah.,OK.,And then he can help with, I already have all the animators from vid that can just literally bring some over.,Yeah, I'm not opposed to that. But just be aware that our client base isn't going to in line with animation as easily as some other client bases. Not saying that there's not a handful that will. Like why? Because they don't care. They spend big money on Google ads. Like our ideal client spends 200 grand on Google ads and literally doesn't care about anything else in the whole world. And this was like selling them conversion rate optimization and saying, Hey, videos come in here and, and helping with the creatives and all of that will help.

 But like, like think of Facebook, like the place where you are display or places where these ads actually would show up. Yeah, it makes up like 5% or less of all of the spend that we manage. Got it. So just so you're aware.,So it's like you're saying video isn't really going to help us at all in terms of making more money.,It absolutely could, and it would be a great capability to have. I just don't think we're set up to roll out a big video thing, but we are set up to roll out like actual conversion rate optimization and AB testing. And packaging it all up and including video. So it's not just like, hey, like adding deliverables, we have to make an offering that our clients will buy. And if we lead with animated video, I don't think it's going to resonate with the majority of them.

 I get what you're saying.,Looping it in with the CRO is what will sell.,Exactly. I can get anybody that's spending grand, 50 grand to spend $2,000 more if they think that they're just going to get one more admin per month because that would be like 10x worth it to them. But if they think, okay, we're going to make all these videos, they're going to wonder where the money is going to come from Yeah.,Because I know also Mitch was mentioning he's had several clients asking for video. And so I'm like- It does come up.,It does come up. I'm not saying it doesn't at all, but it's- majority it's and and we should have it and be able to sell and make money for it but I think like like if we think of like an offering that like yeah 90% or more of our clients will buy video it's not it yeah no we need rank lab CRO yeah exactly yeah all right I gotta go but I will talk to you shortly All right, see ya. Hey, happy new year.

,You too, man.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok thanks!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Read through this but it should be gtg:


```Dear Department Directors,
I'm excited to announce the launch of our collaborative effort to develop Webserv's 2025 strategic plan. This process is designed to be inclusive, leveraging your expertise and insights to shape our company's future. Here's what you need to know:
Objective
To create a comprehensive, bottom-up 2025 strategy that aligns all departments with our overall company vision.
Your Role
As department heads, you will play a crucial role in this process:
Develop a detailed growth plan for your department in 2025
Identify key growth drivers and opportunities
Identify critical moments and your involvement in the sales process
Assess your department's strengths, weaknesses, opportunities, and threats (SWOT)
Contribute to cross-departmental initiatives and synergies
What to Expect
Individual 1:1’s with JD to discuss your department's vision and challenges
Collaborative workshops to align departmental plans with the company-wide strategy
Opportunities to provide feedback on the overall strategic direction of the business
Key Focus Areas
Revenue growth strategies
Operational efficiency improvements
Cross-selling and upselling initiatives
Innovation in service offerings
Sales process enhancements
Timeline
Week 1 (Jan 6-10) - Review 2024 performance, create SWOT
Week 2 (Jan 13-17) - Identify 2025 Core Opportunities
Week 3 (Jan 20-24) - Analyze current offering performance
Week 4 (Jan 27-31) - Sales Strategy
Week 5 (Feb 3-7) - KPI Development
Week 6 (Feb 10-14) - 2025 Roadmap Development
Week 7 (Feb 17-21) - Refinement and Presentation
Resources:
- 7 Week Timeline Strategy
- Strategy document template
- Access to performance metrics and data
- Support from JD

Next Steps
Compile a summary of your department's 2024 performance to date (revenue to target, churn, new business) and spend time to prepare a preliminary SWOT analysis for your department. You should prepare for this SWOT workshop with me by reflecting on the question, what must be true for us to double the revenue of my division in the next 18 months.
I know this is a big ask for those of you who have not been involved in planning before but remember, this is a collaborative process. JD is here to support you and ensure your ideas and concerns are heard and integrated into our overall strategy.
My ask of you is that you come to each of the meetings prepared with the required pre-work done and ready for discussion.
Let's work together to shape an exciting and ambitious future for Webserv.```

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: May want to include something about how I'll be running this so they don't bother you with stuff

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm paying for my own loom, can I get an account plz?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I got an email but not a slack

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: joined thanks

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: me

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If not let's make one

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You, Trev, Shan

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: is there a dept. head channel?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: if so can you add me?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: thanks!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can we rename the group to dept-leaders

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: kk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: should I delete the 930am one I sent?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sure, I don't need it unless you do

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: or you want both?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: saw you sent another invite with sam

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan / Preston / Trevor (Guest Post Strategy)
Meeting Participants:Jordan Dahlquist,Preston Powell,Trevor Gage
Start Time: 2024-12-31T13:58:19-08:00
End Time: 2024-12-31T15:05:19-08:00
Transcript: Hey, Jordan.,Hey, how's it going, man?,Good, good.,How are you?,Yeah, pretty good. Just working on all kinds of fun stuff. Looks like it, yeah.,That's a big email we got there, so. Yeah, don't be overwhelmed by it.,It's going to be just like little chunks each week, so it's not going to be is I feel like the way that the email comes out sounds really big and daunting, but it'll be kind of like baby steps.,So yeah. Good.,Well, it's good to lay it all out so we know what the idea is.,Yeah, that's kind of the goal. And then each week we'll have little chunks that we can knock out and hopefully get it done on schedule. We can always be flexible. It was going to be an eight-week sprint. We ended up making it a seven-week sprint because I didn't need the eighth item. So that gives us kind of a weak buffer if we end up needing it.,Oh, nice. Yeah.,And yeah, I was just reading through your doc. That was cool. Thanks for putting that together.,Oh, yeah. I put that together when Preston started kind of just kind of talk broadly about what he wanted to do for the new year. A lot of it's kind of short sighted. I don't think it's as broad as he was thinking, but you know, I, I got to tackle little kind of things in, in, in kind of bite sized chunks.,So, yeah, it makes sense. I think some of that stuff is going to fall into our seven week sprint too. So yeah. Um, The seven-week sprint is going to be a lot of just documenting and planning. And then all of 2025 is where we map out where all that's going to happen, when we execute on everything, and how timelines, all that kind of stuff. But in the meantime, there's always stuff that we can do, too, as we've already been doing.

 Like, I've been working with Mitch a ton, and we've already sort of fixed a lot of little issues that was causing a lot of hang-ups, you know? So we can continue to do that kind of stuff.,Hello? Peek-a-boo. Your picture fell down. Wait, what? Said your picture fell down.,Oh, yeah. I thought something looked different.,I couldn't figure out what it was. It's a floor picture.,It looks like a countertop to me.,It looks like you have a piece of countertop on your wall, like granite or marble. Not quite, but cool. So for whatever reason, I'm just not really feeling this. So let's just get it over with. Yeah, so Jordan, the problem is that she's making some random list of link prospects, like a freaking idiot, which I hate to say, but then she's asking this blog about washing your dog. If they'll accept if they'll guess post and just like You think we'd paid money for a link there?

 Like I'd be totally open to maybe paying money for some of the links But they suck. Yeah, like why would we want to pay money for that trash?,So like this is just the way it is So we need to do one of two things from what I see it. One is fire her or move the entire team over to PR. Or option two is we create an exact step-by-step-by-step instructions on how to do exactly what you wanted to do. Yep, so here. And we actually started that.,Do you have that, Doc? I do.,So it's all about the prospecting, really. So should we buy? So the issue with Scrapebox is that this is a download. So let's say I wanted to do it it's a hundred bucks and it works for Windows and Mac but she would have to buy it and then I will have to buy it to demonstrate this but it's really really easy and I can spend 30 minutes with her to get it set up but but it's not hard you just put your search query in here and then from there you set up proxies because you need proxies so you need this thing and we could start with you know like 20 proxies it's like 44 bucks a month that'll probably be good And then Yeah, you just you just test on Google search to see what you're getting So, let's say it was a test about About So, I mean look should we just start writing this down on the dock or what's the best approach here to get that?

,executed?,Um, I just don't feel like you just write it down on the dock because I kind of feel like we need to at least get loom videos and like do it. Okay. But Trevor However, this one's always good. In URL links normally produces all kinds of great stuff. Yeah. Here's all these general...,Yeah. So... Yeah.,I mean, it's not very hard, but what Scrapebox does is it takes these results and you play around till you've got the right query. And that takes an understanding of this. So here's all the operators, right?,It seems to me like the best mode to get this relayed to her clearly would actually be like an hour call with her to demonstrate it and answer questions and then record it. Record the entire call. So maybe that's what we need to set up between you and her.,Yeah, but I think you guys have to be involved because ultimately like you guys You guys have to get an understanding if you're gonna say that, you know, she's doing good or failing. But yeah, so what she's trying to do is get, you know, 200 good prospects into a campaign, and that should probably take her an hour or two. Like, you know, she just launches like a million campaigns and each one's like really low quality trash.

 We just need like one good campaign for the whole month for a client, maybe two.,Mm-hmm. So what does Greg Fox do?,Because I see you, the operators, and then you're finding the links, and then Scrapebox play into this? That's how you're getting the journalist's info and reaching out to them or something?,This is not related to journalists at all. Or like, what is Scrapebox doing?,I just have no clue.,So let's say, like, if we gave some of these, these are pretty good. But we don't want to write for them. We don't want guest posts. We want resources, useful links and links. These are good. These are really good. This guy knows what it is that we're trying to do very well. Why don't you DM that guy and let's hire him? Just joking. Let's see.,He is only four months at RevGenius and he looks super legit.,Yeah, let's connect. Yep, bam. I hit him up. He knows. Yeah. Yeah. So anyways, what you would do. Let's just go like this. So super high level, why are super broad is let's just go. Let's go keyword depression. Bam, useful links. How many? Hundreds. So what Scrapebox does is it turns this into an Excel sheet that has information on the domain. So it would be, it'll spit out all the URLs it harvested.

 From the Google search. Yep. And if we wanted, we could use add-ons to. Okay. So what does that do to help us? What does that big list of links do?,What do we do with that then?,Well, you load it into your campaign in Pitchbox, and you would then email the admin.,Exactly.,But you have to identify a contact at each one. So does it scrape and pull their emails then too?,Is that kind of the point?,We used hunter.io to pull their emails, but she's doing something to pull their emails already. What's she doing to do that right now?,Do you know, Trevor? I don't. No, I don't know. I mean, they're, they're responding.,So like, whatever she's using is, is, I think, I think pitchbox even has something inside of it to do it.,And, and they have an integration with Is like all she's really missing is she's just running campaigns in the wrong way She just needs to be sending campaigns to the these lists these keywords resource Well, I showed her this,part though. So she wants to have a ton of success If she wants to have a ton of success She can just start by stealing the links from people that have already done it it. So again, addiction center.com, their whole business is a link building department. And I mean, there's obviously the people that create the website, but but the bulk of their team is like seven people doing link outreach every day for the past, you know, eight years.

 So anyways, let's go into. Mental health page. OK, let's see what they do about PTSD. OK, PTSD and addiction. Uh. And then OK, let's share this tab instead. Alright. Where are the links? Okay, here's the links. So that one has, you know, thousands. So you could just export this. Smoking meth. What the hell is this?,Okay, so I get the point, like you can actually go into a site that's already found all these resources and then just go to like contact those admins. And then you get bonus points.,Yeah.,So why doesn't she understand how to do this?,What's the disconnect? Because it doesn't I'm not even an SEO guy, but this doesn't sound too good.,I haven't explained it well, or she doesn't know what we're saying yet, or I think I think we went wrong because I was like, oh, that's so awesome. You were at this outreach place and like, bring some of your expertise into the mix. And now it's like, oh, shit, they failed financially because they spent a bunch of money creating fucking bullshit. Links and everything. She knows she knows how to use all the tools.

 Yeah, but like her whole procedure was trash I've been doing this for several years, but the wrong way the whole time. Yeah, and So yeah, it shouldn't be that hard. She knows how to use the tools. She's willing to work but yeah, our problem is If we don't have a backup for guest posts that we can pitch to people Is more valuable and all we have is PR. We've got a huge number of clients that have PR and guest posts and We're we can't we can't cross sell those people back to just PR.

 We're like great. It's so much better you're losing your guest posts and That's it. That's that's Yeah, that's that's our problem. So we need another solution Otherwise, we're gonna have to keep paying for guest posts and we have a solution solution. But for whatever reason, like, yeah, that's so different. All right.,Well, Trevor, I don't know if you have any input, but sounds like to me, we just need like to get on a call with her on Thursday or Friday morning. And sure, like we need to tell her it's like, forget everything you've ever learned. This is exactly what you're gonna do. And you're gonna show your team how to do it and then we'll just walk her through it on a call and like a 34 hour long call. Show her every detail, answer every question she has.

 And then if she can't do it after that, then we go from there, right?,Yeah. OK. Yeah, I think that's fine. And we'll buy her pitch box. We'll show her how to do it. We'll figure out how she's getting email contact. And then and then again, you know, I walked Michelle through setting up Pitchbox because she never worked with Pitchbox and worked with her to help kind of build these lists. But I didn't do the identifying of contacts. She did have a couple of things that helped.

 So part of it, like, you know, they're just sending out a mass email campaign, like what what's effective in this stuff, they need to, you know, each email and then and then they need to go to the website and They need to see if there's a contact form and they need to fill that out too with the same email that they're sending And that increased our results a lot But but yeah, they have what they need to do it.

 It's just they're like Oh mass trash We need to go lower volume higher quality and yeah we didn't communicate that in the beginning so that's what we need to do now we need to educate her and tell her like,this is exactly what we want you to do do not deviate we don't want anything that your old agency did throw out the window yeah yeah okay so um Trevor what are you do you have anything anything?,Yeah, so I just, so we got the two outreach teams, PR outreach and link builders. Outreach is pretty good to go. We've kind of removed the roadblocks there, the link builders, we obviously need to do this sit down to get them on board. Just in the short term here I just broke our clients down into groups here because I'm looking at this next month you know if we're gonna do guest posts we need to put in the order now.

 So this first section here is what I've organized them to order guest posts. These are the clients that get both guest posts and PR outreach. So these are the guest posts that we are gonna order. The second group is is what I've marked as get on PR outreach.,My understanding is Trinity group is canceled. So I look back at everything like you might have to talk with Jordan about it, but like, Like There should ended December 19th and that would have been their last date of service. OK. So just just. Sounds like They still want to tango, but like, I don't think we're billing them. Okay. So cool.,All right.,Um, so the second group is, is pretty big, right?,We got these 21 clients here. They're getting guest posts, but not PR outreach. So the idea there is to get these guys on PR outreach. So we have to do some work there. So we've got to put together. An explainer, a template that breaks down in a systematized way what PR outreach is. Looking back at this year in SEO, blah, blah, four algorithm updates, spam update, blah, blah, blah. It made the case for guest posts aren't as effective anymore.

 We need to switch over to PR outreach. It's more sustainable, higher quality, and more impactful. So I'll work on putting that together. Kevin might even be able to help me kind of juggle up make it look nice with his new kind of proposal template that he's putting together but so all these people we're gonna need to at the very least reach,out in January like we don't want to be too far behind when we hit him up Jordan yeah cuz we're gonna have to because they're it's contractually stipulated that they get guest posts.,So there's a contractual component of this where we need to adjust those contracts agreements. So I'll loop into Kim, possibly Chris, we said.,Our goal here is to get 12-month agreements and I thought about it. I think Kim is probably more appropriate at this point. We just want Chris to do his outreach and start signing new deals and he's doing good with that. I don't want to throw him too far off track until he's got some deals in the books. And this is easy money for any salesperson. And I want to give Chris easy money, but this is too easy.

,Fair enough. So these ones are the ones that we have to approach, get on board with the razzle dazzle proposal template And then Kim's going to lock them in hopefully for 12 months if possible. And there's Clinic Place Alps. They're just a weird case because they kind of were supposed to be getting PR outreach and it just didn't take, you know, their time zone wise, it wasn't working. So that just will need a little bit more of a zhuzh.

 Front Range and Newport Beach Recovery Centers don't need to change their things. We can. I think Front Range Clinics is now Port Clay Health, obviously.,It's kind of fertile ground for an upsell, but it's just not part of this. Hey, those links that you bought, what do you think about them?,Remember those crazy ones? I just did one for DG Roofing, too, because I kind of want to see what the impact is on a site that that is less established, less authority. I think they're, I mean, they're kind of shit, but they're also kind of clever. Yeah.,I don't know.,I mean, it's like, we'll just keep an eye on it.,Yeah.,Do we have a total? Oh, yeah, these ones. These ones all suck.,These are all 5k and under clients that I don't think should give PR outreach to yeah for gratis some of that's kind of hard you got wood dragon and therapeutic partners both a very little I think we need to,yeah I'm like pretty upset with the fact that they sold RNA therapeutic to a new 12-month agreement without talking to me about it Kind of bullshit.,Is it a 12 month agreement?,Yes, dude. It's a shit contract. Oh, okay. Um, yeah, they just, they resold it. I was going through the deals for, for like last month for November and they fucking signed a 12 month agreement for a thousand dollars, dude. What? Yeah, dude, they didn't, they didn't talk to me about it or thing. They just like slid it under the door.,Oh my gosh. I mean, you have a clause in your agreement that we can adjust any time, right?,As the agency?,No. Only for cause. It's fine. It's just one. I just don't want it to happen a bunch. The cause is we're losing money. Just joking. We'll just say that like we have certain minimums and and they can't go below the minimums without approval Yeah, then and then next time we'll write them up it's partially my fault because I let them sign them to a shitty six-month agreement because Paul was like, oh, it's really important like this just like a little therapy practice and he knows a lot of people out there So there's like some strategic benefit to it.

 I was like, yeah, that's fine We'll do you know a little bit get them on their feet Apparently they're happy. I went and looked at the back and forth in the emails and So it's not like they they try to sneak it past me necessarily They just took that I was willing to do it one time for six months,as I was willing to do it forever And it's not a good thing Okay so it's uh so these guys probably will still need to be talked to but you know all the I mean obviously all these couldn't and could be re-evaluated to to pay us more money but these ones it's it's more of a dire dire necessity um yeah so that these are kind of trouble cases down here um yeah so it's kind of like the The rollout, now the impact of putting 20 more clients on PR outreach is, you know, currently we have, where is it?

 We're kind of feeding clients into the PR team that have finished with Brandon's things. So then we have a handful of these clients in green that are kind of on to the PR thing. So we won't know when we hit their max until we hit it. And look at, you know, when we're getting diminishing returns and when we need to kind of max this stuff up. But that is something we need to be aware of And we need to pull resources from the link building team if that's not being effective.

 Then I think that's our step there.,Yeah.,Well, let's not shoot ourselves in the foot. Let's not just make this, hey, we had this meeting one time. So a big win from this is going to be getting people on 12-month agreements. I think that we should at least have a talk with these people because they were pitched two options. All of them that went with only guest posts were pitched PR for more money. So it's possible that through this process, we can say, is there some way that we can limit the amount of outreach?

 Or maybe do we want to implement the pay for performance? Hey, we're gonna do this outreach for you at at no cost, but you're only gonna pay us more money if Because once we tell them guest posts aren't a good anymore and we're going to do PR outreach for them They're gonna be like, okay Yes post no good. No more. They're gonna come to that conclusion and now We're going to say, hey, we have to do all this work.

 We have to build these relationships with reporters. It's really hard and takes a lot of time and effort and manpower. But we hired seven people and You know, for the same price that you're paying, we're going to do that outreach for you and we're going to add this pay for performance thing. So why don't you set a budget with us on what it And on the people that are like, hey, I can't pay another dollar.

 We'll just be like, okay, well, we're gonna do it for you to replace these guest posts. But we'll limit it at two or something like that. Let's get strategic about this because if it ends up that it's going to max out our team and we have to grow the team, let's get some money for that so that we're not paying to grow the team ourselves. And I think a lot of people will be on board. A lot of people won't, but let's get a little bit more strategic than just like, I agree with your list, Trevor.

 I think we've done the beginning of the work. I think that the conversation just has to go a little bit different. Than what you're, because if we're just like, hey, we're going to give you this for free, and we're going to do it no matter what, and we're doing this because we saved more money than we were spending on guest posts, yeah, that could work. But I think we can make it better. And the feedback I've gotten from Chris Harrison is that these people really do like this pay for performance thing.

 Because then we can set a budget and if we're like, okay, we're charging 300 bucks a link So long as it's within you know above a 30 Domain authority then they'll be like, okay cool. Do you want to show Trevor that deck I threw together a while back? Rank lab.,Yeah Is that? Yeah. While you're bringing it up, I see everyone has a slot open at 9 a.m. On Friday.,Is that OK to send out the training for pitchbox call with Alex? On Monday, Friday, the third Friday.,Yeah, that's fine with me. I'm actually going to include your whole team.,OK, just so that.,So these prizes per play, are probably a little high, but I think this one's fine. This one's maybe like 350, and this one's maybe like 450 or 500. And if they're like, okay, that's fine, but if I don't do this, Like, and then we can also give them the option. We'll just be like, well, look, like you're paying for guest posts right now. They cost us money. We can keep getting you the guest posts.,It's just, we don't feel good about it. So the idea is you can use this deck to help that conversation.,Yeah, I think we, I think, yeah, if Trevor, you and Kevin make this like a million times better, then it'd be good. But I think we need to talk about the issues, and then we need to figure out how we're approaching these calls, because we don't want the people to feel like they're getting sold. So the account managers are going to have to have a part in it.,Okay. Yeah. So I also have a couple of clients that are currently on PR outreach.,You don't like the current flat be structure You know Primary to lighthouse in Manila Okay, well that's fine we can we can make the deliverables and then we can just tell them what it is so we We'd have to,those are the first two that we need to hit up with this, but then we also need to have this kind of airtight before we do that. My only concern is that they're, you know, if they have, you know, a bank of money for links, then unless we fill the gap in some way, that their monthly rate is going to kind of fall down. And so I I put together kind of like a proposed scope of work for some of this stuff.

 And this is probably a larger conversation that we need to have now. But I was going to fill the gap in some way with just like more content. So like, you know, like,,I think that's a phenomenal idea for the people that aren't getting what they think they should. Like, you know, the person that were like, hey, we're going to do this for you for free, but you need a budget for pay for performance because it's going to, you know, we have to staff and blah, blah, blah. And they're like, well, no, I want to get at least as many links as I was getting Then we'll be like look we're getting rid of guest posting We're gonna have to do something different we can give you more content but this is gonna work better you hire us because we're the experts and And you're being a real freaking idiot right now, sir I Want that you to be the one that says that though, that'll be good and,we'll put that in the script So these guys, you know if they're currently paying all these people pay different amounts, right? Yeah 7,500 some 6,500 some you know, whatever it might be So probably have to break this down a little bit further, and then it's a good opportunity to get more consistent pricing across the board, where if we're just replacing, you know, four DA30 guest posts or something, a common number, then maybe we have that be, okay, for that price, we get you maximum two PR placements, and we don't put on the budget thing.

 We just do kind of like a low-level PR outreach thing. And then other people that go into the bank, they obviously get unlimited as long as their bank is able to adjust for it.,And those are the people that we prioritize as the big ones. OK. That makes sense. So. Yeah, these people that are getting just like four DA30 guest posts, I don't think are very good. They're never going to get anywhere.,Yeah, no, that's true. And the only tricky thing is we average out in a 12-month period, people that do PR outreach get on average four links.,Um, that's 12 months per month.,Okay.,Okay. Yeah.,Um, so like three grand, so they're paying like $800 a link. Yeah.,So we're going to reduce that to, you know, if it's $300 a link or whatever it might be, you know, we're, we're looking at like 1200 bucks, uh, a month, uh, which is, you know, could be less than they're paying now. So I just don't want to have...,The good thing about those people is that even though they don't love the way it is right now, we don't have to do anything about it right now. They're still paying us. They're super happy. I think Lighthouse and Monema are some of our more happy clients. Unless I'm wrong.,No, you know, they're they're finicky, but there may be more high maintenance, but I think they are satisfied with this generally. I just don't want to take a a big hit in our MRR.,Well, yeah, but I'm saying we can address that later if they're already getting if they're already getting. So let's win. Why don't we with these people we're trying to get on PR outreach? Let's try it and win. Let's try and fucking come out of this like wet. And it's okay if we took a hit on our MRR as long as the amount that we save in fees is more, which I get that there's a concern on the PR outreach specific side.

 So how is PR outreach going with Julia?,It's decent. We had to kind of of break free from some two of a situation, situations that were attached to Brandon's phone. I'd sorted that out, but they only have, you know, I showed this one, they only have so many clients that they're actively working with now.,So it's, you know, wondering though, if we're, we're getting anything yet.,I don't think we have No, we don't have any live placements yet, but it's been pretty slow. They've been up and running for a week or two, and it's been slow news time.,Yeah, because it's the end of the year. That's OK. But we feel like they're hitting every opportunity.,We'll have to go back and audit it more carefully. But from what I've seen, it seems pretty effective. It's also a new platform, so it's You know, there's a lot of caveats in there Okay, cool.,Well, I just want to get these things off the ground if in the next month we can get Alexandra's team like working better than the other the other piece is going to be much easier to approach and then You know we can kick the can of of switching the people that are already paying us thousands of dollars a month for PR down the road a little bit. We'll be able to kick that can down the road till March.

 And in March, we might want to reassess our pricing based on how many links we can actually get for these people on average. Because we'll have some data. And yeah, so I think all these that take get on PR outreach, I think that the plan should be to get them on PR outreach. Now, I do have another caveat. I think we have to continue buying links for the roofing company. We have to continue buying links for non-treatment centers just because I don't know if our PR outreach is going to work for these.

 And I doubt it will.,Yeah, it's the rollout that we would be getting Alex on board with ostensibly does not work in other areas now.,Which is a bummer, but at the end of the day, our clients are rehabs. There's so many more rehabs that if we all put our heads together and we're like, Hey, we only want to work with rehabs or mid market or enterprise companies. I think that maybe, maybe we'd have something. All right. Well, cool. So we've got that, that meeting on Friday and then Jordan, how do you want to work with Trevor to address phase one, which I would consider phase one, approaching all of these people that are on get on PR outreach.

,Yeah, you're talking about phase one of this not of our seven week sprint, right?,Phase one of this because yes, it's kind of crunch time because I asked Trevor not to order the guest posts for everybody because like, you know, all that money that we wanted to save. It's now time that we save it. So like those ones that are in the, the get on PR outreach, it's fine. It goes along with what we initially wanted to do. We'd said in January, we're going to want to be having these conversations.

 So, so it's all good.,Yeah.,It's really a two-step, it's a two-step thing. We need a deck and then we need to brief all the account managers on it. And then we just need to set up the calls, right? Am I off on that?,No, that's correct. But yeah, it's just a matter of whether they have the link bank or the max two placements. But yeah, I guess that depends on how much they're paying. So do we need different decks for each of those types of clients?,Or is it more of just a deal?,I think I think Trevor, does every SEO client know you? Every single one of them? Not me. Yeah.,OK.,So I think the conversation is going to be most natural with you and your account managers.,This is a place where we're going to need to have associate directors looking for these opportunities in the future. But that's fine. I think if it's too formal, we're going to screw it up. Like, I think we need the decks either way. And I don't think you run the call like a Presentation of a deck. I Think you guys get on the call and you say hey guys I just want to join this call because I've been conducting research across all of our clients and You know, we've we we have some some You know Results that are less than stellar with these these guest posts They were better And throughout last year, they declined in value.

 And we really don't want to be selling you guys these guest posts because they're not effective. And at that point, what we'll do is say, OK, so we've got some cool stuff. I know we pitched you on PR outreach. When you guys were coming on and you know you elected to go with something smaller We highly suggest adding PR outreach to your scope But either way, you know we're gonna want to be moving away from guest posting and then and then you can have like an open conversation get a good feel some of these people that are getting a lot like wave plastic surgery and They might be a touchy one, but the rest of them look approachable.

 I agree with you on the way we present it not being too sterile.,I think we could also make a deck that comes across that way. Like, hey, moving into 2025, we've done a ton of research over the last year and how the performance has gone for each client. Here's how we're shifting away from guest posts. We show the data, we talk about about the new team we hired? Do you think, or do you think it needs to be totally organic?,Like no deck presentation? I think we have the deck. I just don't know if we should lead with it.,Yeah, I could. That's my point.,Yeah, yeah.,We could envelop it in a quarterly slash year-end review where we just talk about general kind of stuff.,I like that. That'll be really easy.,Yeah, so yeah, schedule a year-end end review with every single one of these clients and segue into algorithm updates spam updates genius improved processes and then I can circle back after the meeting and say oh by the way I was talking about this PR outreach thing here's the details and then maybe even then have him follow up maybe just say like oh hey if you're sitting what Trevor's talking about this is what it looks like in in on paper brass taxes is what you have currently.

 We highly recommend this one. This is what that looks like for you financially.,OK. Guys, I think we just crushed it. OK. I think what we talked about just now is going to go really, really smooth, because then we could. Every single one knows Trevor. There's a couple that we're just going to continue buying guest posts for. Trevor, wave plastic surgery, continue buying guest posts. Roofing, continue buying guest posts. The rest of them, guest posts are going away.,All right.,So, yeah, there's no there's no you can continue on the same plan.,It's we're moving this way, right? Yeah. Yeah. That we're and after hearing from, you know, Trevor, that a guest post don't work, which we've been saying for what, over a year, Trevor, it just hasn't been a better option, really. Yeah, it's just like, hey, we're selling you something so that there's something there.,Yeah. I think we should also explain this to the team on Friday, Preston, like, We should explain why we're doing this and what we're doing so that they get a bigger picture, too, a little bit. So the link team on the pitch box called.,Okay, yeah, yeah, yeah. We'll bring it into the call. And yeah, we should include them more. And I think there's a way that over the next year, we can hire somebody that just does like some onboarding link flow for all of our clients, Trevor, if you find some good stuff in what we do, we can just like have somebody in Romania or some shit that, Uh that runs through this process Yeah, it's uh, that's one of the things I put on here um Like whatever this is Three to six month link building protocol So,bright locals one month. It's similar to what we do with dg roofing Right local one month startup ranking the next fiverr package Then you know, whatever cloudlink package and then and then uh Is this something our link building team could do?,What if we just had them start working on that kind of stuff too?,So they could do it, but we pay Bright Local. So they could do it manually.,And Bright Local is not expensive. Bright Local is so cheap for what they do.,I don't think we should get rid of that. Yeah. And it's a one-time cost. So we won the client. We're onboarding the client. And we have to pay for this once. Yeah.,So my next question, Trevor, is how can I help you? Do we need a call maybe Thursday to hammer out a deck with Kevin? What's the best modus operandi? Yeah.,I mean, the deck will be important. You shared it with me, the Rank Lab. So I'll take a look at that and see if there's any kind of changes we need to make there. And then we can use that.,We need to make a ton of changes. Yeah. It's rough, but it's nice.,Yeah, it's going to need a lot of changes to align with the strategy that we're talking about here. Just look at it as a conceptual thing. It's not very specific.,I had no context when I built that, so. OK, so we'll use that as the jump off point. Yeah. Could use assistance there. OK. And then, yeah, we'll just have to do some QC with the our link builders to make sure that they're getting the job done. And that's, it's not a jarring process because all these guys into PR outreach, just in the handful of clients that already do it, some just get jammed up. So we just need to make sure that we're able to execute just things like getting an email from them that we can access.

,The cool thing when we're We should talk about like an onboarding process and we should even map that out. And let them know that, hey, like it's just like building a sales pipeline. It's going to take 60 days, you know, before you start seeing like continual results for this. But, but, you know, we might get a couple of links in the meantime, but we're building that pipeline. I think that's an important thing to tell people.

,Hey, Trevor, what's your. So your Thursday looks pretty crazy. They're a good. Should we do it on Friday instead? Or like the next week?,I could do afternoon on Thursday. I should be free after 3 p.m.,But, uh, what about, um, yeah, or we could kick it to next week. Um, what I could do is this week, Thursday, Friday, I could work on the verbiage and getting it more dialed in. And then really next week we could put it into an actual deck with Kevin on a meeting. So 11 Monday.,Monday 11. Yeah, that works for me. Okay.,Cool.,All right. All right. All right. Sick. Um, should we give Alex a little bit of a warning slack to let her know what this Friday thing is about?,So she's not taken off guard as the account lead kind of Like, just let her know, like, hey, we're really needing to shift strategy over to like Preston's methodology. So we're going to do a full training call. Yeah, she's probably going to worry that that's what I mean.,Meeting is going to be to fire them off. Yeah, yeah, yeah.,And I want her to know, like, why we're doing this meeting. Oh, yeah.,Just just tell her, just be like, hey, Like, you know, we want to change up the way that we're doing this.,And and yeah. Do you mind sending it, Trevor?,I kind of want her to start. Why?,Why would you invite her whole team, though? Because I don't want any telephone game of like her having a relay to the rest of the team.,Well, but the big issue in her kind of ideal for setting up a department is really there's just one role and there's not actually a manager, right? She's like, I'm gonna do this thing and all these other people are gonna do this thing. And if they have questions, I'll answer them. Like in my system, one person does all the prospecting, whereas the manager, right? And the rest of the people are sending the emails.

,Yep.,I still think they should know how this works. I personally think, but if you disagree, like I can remove everyone from the call.,I think maybe they should.,I just.,If it's too much of an open format.,No, we're just going to tell them, like, It's not for the lower team to ask questions, it's for Alex. But they're shadowing. They're basically just seeing the whole process and the end, so they understand what we're doing. And they can get a context for who they're even emailing. It's basically a call for Alex to learn, and everyone else is shadowing, and everyone's on the same page. If you don't think it's a good idea, I'm happy to remove him.

,No, no, no. Let's include him. It's just I don't want it to seem like willy-nilly because I'm gonna ask her questions about how they're getting the contact information And if she's got a good solution that great that if she doesn't have a good solution We're gonna have to bring hunter IO into the mix And when a contact can't be found they're gonna have to go on the website they're gonna look in there there you You know, yeah contact us page.

 They're gonna they're gonna look around and try and find an email right What does that have to do with having the whole team on just I understand Well, just I don't it's fine it's totally fine but like I just,don't want it to seem too not finished. Okay, got it.,I mean, the way I look at it is we've got a team of four people that not only aren't doing much, but they're doing what they are doing wrong. And I think it's good to just get their butts on a call and we can start giving people more context for what we're trying to do here. And even if it's not totally useful information, at least they get a window into what we're doing, who you are, what our vision is.

,Yeah. Yeah, OK, I agree. OK.,Well, good work, ladies and gentlemen. Ladies.,Trevor looks like Fabio Hey Trevor Mm-hmm. I'm really really excited to see you right now. What's this calm? Well, I didn't want to tell you because the comedian got a little bit of me dude and I I know you're big on on Is it Dave Landau?,Is it Bruce Bruce?,It is. Chris D'Elia. It should be on my. Calendar here.,Let me let me tell you his name.,His name is.,Brian Callan.,Oh.,Yeah, I'm trying to think of what he got up to that was not great but some some lady accused him of Like raping her when they work together like forcing her to To give him a blowjob and he would give her like screen time or something Oh, yes. I mean, not that the accusation wasn't that he like forced himself upon her, just that. Yeah, but he's got a bunch of shows now, he's been accepted back into the mainstream.

 I like a nice redemption story.,Yeah.,So it should be good. And it's at 8 p.m.,on Sunday. Very good.,He's been around forever. Mad TV, dude.,Yeah.,Mad TV. That was great. I used to love the Mad Magazine as a kid. Yeah. You know this guy, Jordan?,It looks like this. Oh, yeah, he goes on Joe Rogan like all the time. Oh, yeah, he was on the podcast with the MMA fighter.,Yeah. Yeah. And the kid, he's been on a lot.,That's his his podcast is the fighter and the kid.,I feel like he's kind of boring on podcasts, but hopefully he's funny as a comedian.,I haven't seen any of his stand ups or anything, but I read a bunch of reviews and they were all either. Oh, fuck him. He's a rapist or he's great. Nice. So cool. And even if he's not good, the openers will be world class.,Yeah.,Speaking of which, we're still like, I think we need to speaking of Austin, if you are trying to actively Do we need to be rolling out an initiative to hire more in Austin and less here?,No, we, we've been working with our attorneys and stuff. It's not really all that big of a deal. Um, and we moved, we moved, we're in process of actually moving the headquarters to Nevada. Oh, okay, cool. Just cause Texas takes forever with like the paperwork and everything. And it's just kind of weird. Of annoying about it. And Nevada streamlined, we can do it. It took me took me like six and a half months to move my holding company that does nothing from California to Texas.

 Because just processing time. That's so weird. Super weird. My attorney was like, What the hell? It was it was strange. It's that It doesn't matter if we don't have any employees in Nevada or anything like they don't care.,California does kind of care, but we've got like a multiyear plan.,All we're trying to do is offset mine and Kyle's personal tax liability from California to another state. So California definitely cares. And it will help us the more employees that we get out of state It doesn't matter if they're in Texas, Nevada or anywhere else because there's no state income tax here So Nevada or Texas is never gonna care about it. Yeah, totally but but yeah, the more we can do to say that like Yeah Our business isn't a California business.

 So even getting clients out out of state helps Because what California? Essentially wants you to do is say, oh, you made 62% of this income in California. It's nonsense. And so you should be responsible for like this much of the tax.,It's crazy, dude. It's crazy. Brutal.,All right.,Oh, cool. That was a good call. Good job, guys.,Thanks, guys. And thanks for the prep, Trevor.,good about it or good it's not great but yeah you know change is tough and uh but I think we got a good plan together and uh it's good I need to touch base with all these people you know I have a select group of clients that monopolize my time so I you know I don't always get to touch base with everyone and I suck anyway and guest posts suck anyway No, good riddance to bad rubbish.,All right.,I'll see you soon. All right. See you guys. Hey, happy New Year. You guys better not be working tomorrow, Trevor.,Me?,I got a whole plan. I'm going to plant a passion fruit vine in my backyard. Good.,All right. I'm going to go to a New Year's party and get really drunk. I told Kim I'm going to the cannery.,I'm going to get shellacked. You know, it's time dude.,We've been sober too long, right? I'm gonna jump in the couch Talk to you soon

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok gotcha! Can you cancel the Nord account I setup for you if you're not using it?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: How are things going for you so far?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Thanks so much!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sounds good thanks Julia

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Perfect thank you! Really appreciate you putting that together. We are gtg

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome! Are you enjoying the role?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: awesome

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do we have an NSM tracker setup for SEO dept yet?

I see one for paid but not design or seo

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do we have an NSM tracker setup for SEO dept yet?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I see one for paid but not design or seo

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I guess we will do the best with whats available

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: But without data that will be harder

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: My week 1 with the dept. heads was to review 2024 and create a SWOT

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: nevermind, spoke to preston, thx

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So what is available? lmk if there's anything besides what I'm aware of here:

1. Client churn list with reasons
2. Overal dept. sales/rev numbers
3. CSATs?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: is he on slack here?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: CFO is you preston?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: How do I go to him with CFO questions

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: will chat with him

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Anything else?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think all I have is revenue numbers and churn data

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: That is week 1 for our sprint

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So what performance data from 2024 is available is my main question

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: want to huddle?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maybe we can nail that down on the call today

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: This looks good! How should we make the rest of the company aware. Send it out?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok gotcha cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Wanted to touch base about our list of items. Have you been able to make any progress on that? Can I help you out?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Morning Mitch

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I want to roll that out with the team on our meeting next week

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You should check out this new paid media-design form

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: That's great!

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: [3:00 PM] Jordan Dahlquist YU8$p@!%X&KO7Qg8 [3:00 PM] Jordan Dahlquist ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We have that training call on Wed so I want to be able to roll out new processes with claude, typeform, etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Dependencies etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is there anything that needs to improve with Asana before our wed call?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: couple of thoughts

• adding dollar thresholds - what numbers can they approve on their own, when do you need to involve someone higher
• Do any decisions need documentation or is verbal ok for everything
• Maybe merge "Changing SOW Template/Structure" with "Contract Amendments"
• Combine "Budgets" and "Subscriptions"

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Morning Shannon! I'm going to be training the paid media team on Wed next week regarding the new typeform process. Can you let me know if you want any further changes on it by tomorrow so I can have it ready to go for the team?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: we can get it all knocked out quick

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you have time for a quick call on this today?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool, let's look at it together later and we can figure it out

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I have an 11:30 but if you have time before then yes, or after my 1130 is good too

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: perf

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We can expand on it over time if we need

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think it's fine for now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Does each dept. head have a financial pro-forma, or do they have access to create one?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Also, for the 7 week sprint - I'm thinking I'd like to do a dept. head group call each week where they make their presentations to me and the other dept. heads together instead of siloed on separate calls. I believe this will motivate higher attention to detail and performance. You cool with that? Lmk if you prefer siloed approach.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm on it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah I've already got 1:1s going every week

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah totally

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: shoudl be

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I made it so you can just do login without google

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you try to login with email?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Does each dept. head have a financial pro-forma, or do they have access to create one?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: hmm yeah I see that now too

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think you should have an email invite now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ok I upgraded and added you as an admin

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: also, on week 5 the timeline has the dept heads working on a bonus incentive plan for their team. Do you want to keep that or work on that ourselves and roll it out between you and me?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah so keep it percent based etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: K sounds good

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: thdx

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I get you now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah I have that in there already

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We will have them setup goals and then you and I can build bonus off that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I added you to the workspae

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok try now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm assumign it's fine right?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Guess she's moving back for something

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Does she ever meet with clients in person?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Maria is asking if she can work from mexico, possibly permanently

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sure! I'll discuss with him, thanks for lettign me know

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'll let you know soon

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah I'm sure it won't matter then

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: or Mexican citizen

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Will she be a us citizen?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: But she's moving back to mexico?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So if she's a US citizen and going there temporarily for short periods then she is fine as an employee.

But if she is moving there or planning on being there, we would just need to move her to contractor vs. employee.

So she would not lose her job at all, but we would change the format for her employment.

If she's living in Mexico, she'll be better off as a contractor and would make more money anyway.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yes just on with preston, I'll ping you in a minute

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Also if she's going to live in Mexico her insurance would need to change or we'd possibly have to drop it.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Oh ok cool lmk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: sent you an invite

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: NRR tracking meeting
Meeting Participants:Jordan Dahlquist,Kevin Hall,Preston Powell,Seth Powell
Start Time: 2025-01-02T11:28:27-08:00
End Time: 2025-01-02T13:02:17-08:00
Transcript: It's happening, bro.,Just that you have the information on that on that seven-week sprint Jordan just joined a meeting that I'm supposed to be in so I'm on a phone call with Laurent. Can you hear me now? Yes, okay Cool well then yeah, just send me that stuff. We're good to go And I'll tell Jordan to send you some other stuff. When did we want to kick off? I'm sorry Okay cool. Well then. Okay cool. Okay. Okay, cool. Just send me the updated scope that addresses SEO and then whatever I gotta sign and we'll get going.

 All right, we're excited too, so thank you very much. All right, talk to you soon, bye. Cool. So I just, I came to terms with Laurent. He said he'd just add SEO. My thing was going to be like, oh, well, if you're not going to add it, I want a discount, but he's going to split the payment up. And I think the pricing's expensive, but not unfair. Yeah. Okay. So can you send him info on the seven week strategy sprint.

 Yeah, just so he understands it, because I thought maybe he should integrate at certain points of that he's going to schedule a kickoff for next week. And I asked him who should be on there. He said, maybe just you on that one. And then from there, we can bring everyone in.,And yeah, that's it. That sounds great. Cool. Amazing.,How's it going?,It's good.,Things are good. Hey, Seth. Hello. How's it going?,I don't know if I've actually met you yet, but hello.,Yeah.,We talked for a second at the party, I think. Yeah. Yeah. I was in office for a day and a half.,Nice. Yeah.,That is the bulk of most people's experience of meeting me in really.,He's he's super tall, strong.,Six, eight to 25. 3% body fat. 3% I must be hard.,Oh, yeah. Wow. Sorry, I'm sending this off to learn. Hey, can you please close the Thank you.,Alright guys, we're all here so Net revenue retention as a like web serves own NSM It's what we're talking about Trying to arrange the books so that that can be done but basically I will just kind of freestyle and sheets for a minute, and then you guys can kind of get an idea. So what is it? Net revenue retention is a measure of retention, obviously. I'll just share this with you guys. JD. And Jordan's got an outline that's got a little bit more than this.

 But let's just think about it this way. So we could have January, and so let's say So let's just say we need to 200,000 and so we just go off of the big template from directive that I built also or is is a separate thing you're doing. We can go off of that template, but I didn't think it was. I didn't think it was you. I sent it in the chat here if you want to open it up. I can open that one up too.

 Like the monthly tabs down below I think is like December for example Okay, yeah, that's like what we're shooting for I think right, okay Yeah, actually no this one is is Sorry, I didn't see that December so it's a little bit more usable than I thought. So yeah, basically to have your NRR, what you would need is you'd have to track cross sales this way. So let's say that SEO Brought somebody over to paid media.

 Let's just say Nova transformations because this is not going the way that I would have hoped it would go just because they don't have associate directors, but We were let know that they are on SEO switching to paid media and The potential monthly revenue there is going to be 6K. So category would be a cross-sell. Associate director, let's just say it's Trevor. Let's say the strategist was, what's that girl His name, Veronica.

 Let's put this as Kim. None of these guys are. All. Yes. Cool. So this one's a chem status forecasted. Cool. So I would have to get confirmed, but then you would fill this client churn. Uh. Every month and we have to add it all up. Does that make sense?,At the very bottom on the,Yeah, yeah, it makes sense.,One thing with the client win details for like cross selling and all that. Assuming I assume we're updating is what you're going at. And what, just cause in the past, like, I know for me from experience, like being clued in on all these little things is, you know, there might be like one rogue slack that goes through, but typically I don't know. So is this like, we're collabing with Jordan to know when like things are happening or like what it's the, how does it look?

,Isn't it your job? Once a month to meet with Jordan to update all of the data in HubSpot?,Yes, we were going to do that at the end of the month, but we're doing it next week.,Yeah, no. Next week. Typically, it's at the end of the month, so it doesn't conflict with Jordan's early month priority stuff.,I mean, what are Jordan's early month priorities other than billing on the first is a lot.,That's not it. I just, I gave her two suggestions at first, at early month or end of the month, and she said end of the month.,OK, but it needs to contain the complete month. So otherwise, you're going to miss some stuff that happens right at the end.,I also have a weekly department meetings. I mean, I could be updating this every week, potentially. I could just ask them real quick, like on the call, what have you gained? What have you churned? And I could just plug it in on that call if it's helpful.,But yeah, that would definitely help.,The monthly one is at this point just like a monthly show breakdown. Yeah. Final roundup of like, is all this legit?,You know, I think, I think department directors are gonna have to collaborate on both the client win details. And then, and then the client loss details, it has to be like when things end, because if someone's like, hey, I'm canceling, and you're like, okay, well, there's two months left on your contract. So your final bill will be this date, then that's, that's the date that it should you to.,Yeah.,And then this is not quite enough, just because, like, because this total NRR, it's almost as if you need a any, any department that has recurring revenue, specifically the SEO and paid media department. It should have their own because their total NRR. So the NRR formula.,How about right here where you help between line 10 and 16? There's like all this other stuff. Why don't we just do paid SEO and design?,Oh, because this is like a very busy sheet, like you see what I'm saying right here, though.,Right.,Ah.,And then yeah, that makes sense add enter are here for each depart for each group basically Yeah And then we have our total here, but then we have departmental in our I Guess we don't even need this blue one this blue seven and eight box because we already have it at 14 e So that's kind of pointless now All right, that makes it a lot easier.,Preston, do you happen to know what G1 and G2 are?,I just don't know what the, I basically duplicated what your cousin had, but like, I don't know what this is, what these little boxes are.,Oh, is it color coding? Project, revenue, variable, revenue, variance. I know what bookings are. Bookings are just sales that we got outside of this.,It might be like a legend.,Yeah. I think that must be what it was.,Yeah.,Okay, I gotcha. Green is real, blue is booked, in other words.,What it's trying to track, guys, is the revenue of the department without bringing in new sales from outside. Because what we're trying to do is if you lose a client, it's your responsibility and your team's responsibility to replace that revenue. It's not the sales team to replace that revenue okay so basically the contract revenue that they had last month if it's all there the next month then our zero zero.

 But there's other ways to grow. So, contract revenue, LM, minus churn, plus cross-sell, up-sell, plus revenue like ad spend. Right. And then, yeah, so how much do we retain? But net retention, because there's that they can add to it. You guys want to see this Yeah So I don't know if you guys can see it. And when I zoom in, it doesn't get any better. But Yeah, this is the old template. Yep. So. So, yeah.

 I basically carbon copied it, same exact thing, so. Yep, I even added drop downs and stuff so it should be better Or easier anyway, yeah, so we're just trying to get this number to zero right and our And So You know, here they're winning some. They're losing some. Here's the variance.,But it should be fed by all kinds of different things.,Yeah, so I mean, what I'd love to figure out in this call, because I am going to start meeting with department heads next week, and this is going to be a big metric for success for them. And I want to have it start working. I want to have this available in the next week or two. Yep. My question is, is how do we start getting all this data populated as soon as possible so I can start using it? And also, hopefully, some of this stuff we can even streamline and automate or something.

 I don't know. But either way, I just need to figure out how we can get all these numbers in here and keep it updated is the main goal.,that the MRR, I mean, this is actually pretty easy, because it doesn't even look at the existing revenue. It's either negative or it's positive, right? So, there's cross-sells, there's up-sells that, Bam. So the variance is negative here. So the variable revenue, though, is ad spend right now. And if we implement the link building pay per link type system, that will also be variable revenue.,Yeah.,Are you aware of that, Kevin?,I have basic knowledge of all that. I kind of know somewhat what's going on, but not much detail.,Yeah, basically, we're trying to move to a paper performance link building plan instead of just here's here's how many links you get. We're actually going to do performance based. I'll have an escrow account and they'll just pay based on a set tier pricing based on the link quality and all that kind of stuff.,So, OK.,Yep. Yep. So that makes sense.,So the very low revenue is ad spend or links once that's rolled out.,Yeah.,How do we forecast churn? Is that just based on talking with department heads and figuring that out? Do we know or is that real churn?,Is that forecasted churn, Mike? So, right. We have the different touch points. So if they're three quarters into a year long agreement and we approach them and say, Hey, like we're, you know, starting to work on your renewal. And they're like, Oh, I'm, I'm not thinking I'm going to renew. Uh, that would be forecasted churn or, Hey, like, you know, unless something changes these next three months, I'm not going to renew.

 Uh, that's how we would forecast churn.,So then how do we compile that data though?,How do we get that in here into a number? Well, the first year long contracts we ever sent aren't a year old yet. So it's a work in progress. Okay, cool. But we still hear things. So you would get that data in here because you basically need this to be the driving, like, the driving force for your, your department heads, and they need to get their bonuses based on what happens here.,So they should be very, very invested in this visibility on this or is this just Absolutely, absolutely.,We're gonna on that monthly all hands meeting. Even though it'll be weekly, the monthly one. Every time they new numbers, we're going to share it with the whole team. They'll have continuous visibility as department heads. Sweet.,Amazing.,And I could actually just tell them to fill out their own win and loss details whenever they get them. It's just like anytime you win, anytime you lose, go in here and update it, you know?,Absolutely. Except they're going to fuck it up. So it's important that Seth Verifies monitors.,Yeah Yeah, so let's do a once a month verification with Seth but besides that we're gonna tell directors like populate it and yeah, I think this will just become the other half of the meeting I have with Jordan for,like Reconciling hub spot with the MRR sheet and like the actual billing that's being sent out Because that's currently what the meeting is is just we have like a big MRR spreadsheet and then I just make sure that that and HubSpot are in agreement. But I can just tack this on as the other half of the meeting is, all right, cool, HubSpot is current, MRR sheet is current, and then make sure that everything on here agrees with both, and then that should be.

,Cool. Funny. So can we get, when can we get this one filled out by Seth, do you know?,I think my meeting with Jordan is Monday. Let me check. Okay, cool. Yeah, we can we can try and get that sorted this Monday. Yeah, I don't have it scheduled right now. But I'm just gonna see what time Monday will work.,Okay, cool. Amazing. Yeah, if we have this on Monday, and then we can start updating it for the January tab. I didn't create anything in the January February ongoing tabs yet because I wanted to make sure we actually like this setup and then I'll duplicate it so I Do like the the setup?,But we're gonna need Some interconnected Yeah, like formulas right so just like like this is very very easy so paid media The revenue when. Should equal. Like how do I get it to? Like If this is confirmed. This should automatically populate, right?,If what I couldn't see your screen.,If the status is confirmed. Oh yeah.,I can do that.,That's really easy.,It should be forecasted until the day. Well, actually, that's a separate line.,Does that make sense? Yeah. That's the revenue win. And then the MRR loss. Yeah. I got you. We'll have to figure that out. I can try to help with it.,Or unless Kevin or Seth is a spreadsheet whiz.,Yeah, so the explanation to the department heads is hey guys Like you guys are now responsible for Retaining the revenue Yep, and in order to retain the revenue this is what you have to do. And this is how we track it. And basically, yeah, if you lose a client, you're gonna have to replace it. Yeah, you know, our goal here, our goal here is $0. Yeah, we're hitting our goal so far this year, guys.,Oh, yeah.,I'm gonna hit the eight week sprint with this stock and show it to them on Monday. And then because my calls with them at three on Monday, so it's not totally populated, it's fine, but I'll just show them what it is and I'll explain that.,There's nothing there's nothing to populate it with.,Well, for December, I'm talking about December. Oh, yeah. OK. I would like to have December, if we don't mind. We have the data. We might as well just get it in there. Yeah.,Okay, this is probably a dumb question. But just a quick little aside, you said that you said the goal is to get the NRR to zero. But unless I'm misunderstanding it, like, wouldn't a positive number be better? Or am I entirely misunderstanding the representation of the number? Negative number bad positive number good zero also acceptable because it means we didn't explicitly lose.,That's what I'm saying. That one's set up, bro. Oh, okay, okay, okay. You guys see that there's no... The last month's revenue doesn't matter. Gotcha. Right? So if it's zero, we're at 100% NRR. Yeah. If it's a positive number, like, like, if it's a positive number, we're over 100%. Yeah, I'm expecting it to be a negative number and a big negative number. Our goal here is to get that negative that big negative number.

,Yeah, get the threshold back to zero.,Yep. Or positive. Yeah. And I want to ideally positive but realistic. We just want to retain 94% of the revenue from last month. So 94% NRR is actually the goal. So negative six. So if our MRR is 500 K And you're 1094 percent of it. Yeah, that'll be You know 470 K would be Well, that's actually retention I think we do want to get it to a hundred percent so we're okay losing 30,000 3,000 right pretty normal lose lose 6% of your revenue, but if we can make that up and cross sells and upsells Then the things that the sales team brings to the table or gravy.

 They actually mean our company grows Yeah, if we're losing 30k and replacing it with 30k and new sales every month then Then we stay the same Yeah, we're not actually once we start losing big clients and replacing them with small clients, then we're screwed. Yeah Then we're sure gotcha. So So the idea is to is to shift the burden Back on the team that lost the client. Yes rather than the the sales team because one that's that that's not fair.

 And two, we need better accountability than that, right? Like, oh, you lost 30 grand. That's somewhere else. Yeah. Where are you gonna make it up? Oh, that's bummer. You lost 30 grand. You a new guy. You know, 30 grand. It's not like that money is valuable or anything. Yeah, yeah.,Come on 30 grand. What are you poor?,30 grand shmurdy grand Exactly. So the whole point of this is to make it the responsibility of the service department to To take the money seriously and ideally even grow it and then and then once we get into Okay, we're gonna go quarters not have skies just because we're paying bonuses quarterly But But yeah, there you have it so like this guy positive 235 K amazing And these are being added to this this Half as booked revenue not monthly revenue if that makes sense Okay, so If You win a deal we need to know the MRR and the booked revenue in order to make this work because We want to pay people on booked revenue not MRR because MRR MRR is uh, yeah, it's is not in the bank the MRR is But if we get a signed contract where somebody agreed to pass two hundred and thirty five thousand dollars if they don't pay us We can just sue them.

 It's money in the bank essentially Cool Yeah, and then these guys that that were You know negative Then they're going to Probably not get a bonus and if you're losing, you know a lot of clients six of them Then maybe you're gonna be looking for a new job But it's cool it's cool because it runs runs like a sports team it's It's a leaderboard So that's what we're working towards just so you guys can understand it And you might need to use cloud and chat GPT to write the formulas and things and maybe there's Sheets that that we don't have that we're going to need but But it's essentially on you set to figure this out in a way.

,That's easily manageable Yeah, as automated as is reasonably achievable.,As unreasonably achievable. Well, there we go.,There needs to be inputs, but those inputs need to be really simple. The thing that's complicated is turning like, you know, with the NRC, it's it's really great or or NSM. You guys, this thing's dope because it's like, hey guys. Yeah. Very cool. Ooh, now what do we do? Are they back here? Oh, yep. They're back here. So, uh, it highlights the ones that, that need targets and the ones, the actual month that you should be changing.

 It's like, Hey guys, like, so this is Anything that you guys need to be putting input on are here, here and here.,Got you. So you're talking about all the like little quality of life things to make it as simple to use as possible rather than inherently the like,,Well, exactly. Like because the cool thing about this setup is if if they just do their one little thing, we get all of this. Yeah, everything is. So we. Have anything to visualize, because it's a new year. It's the second day of the year, yeah. Exactly. So yeah. I get what you're saying.,Cool.,I'm excited. So we'll probably have all that data populated in there before 3 o'clock on Monday.,That'd be awesome, or at least close, just so I can show them the visual.,That'd be awesome. Got you. Yeah, so And then you can go You know, this is all brand-new month-over-month missus Wow, yeah Oh, look we missed all these but they probably didn't update them And yeah, look, watch this. Did they update them? Yes, yes. Pretty sure they have been, I've talked to them. This hasn't been updated since the 17th. This one hasn't been updated since the 19th. I mean, they're shitty TMS clients that probably don't buy into the thing anyway.

 Clients that we should probably fire, but error client.,Yeah, I just set up the meeting with Jordan and you Kevin on Monday at 1pm my time. So it'll be like two California time.,All right, I'm gonna forward you this. And Kevin.,Please do I will take any sheets or documents or info.,It's just a screenshots from Garrett, but Cool, well then I think we're good. Yep, should be good to go.,Alright.,Anyone have anything for me?,Before we go No, I'll have the uh, I'm gonna have a updated like intro call deck On uh, either end of the day today or tomorrow So I'll show you that that's all that's gonna have all that data and stuff that I grabbed Seth and I worked on so We'll have that and then I'm gonna meet with kim and try and figure out how we make our intro calls more valuable by having like a hand-holding resource type of,thing. Okay. You want to stay on and chat a bit Preston?,Sure.,All right, we'll let y'all Thanks, guys. Appreciate it. See you. Oh, yeah. With her thing, I'll find out if she's going to be a U.S.,or Mexico. I don't know. I'll find out if she's moving to Mexico permanently. Like, I don't care if she works from there. That's totally fine with me. Yeah. It And she's gonna live in Mexico, I don't really want her to be a California employee Yeah We'll just I'll let her know I'm gonna find out it'd be better for her to she'll make more money totally I'll find out Our insurance we pay for for her won't be of any use to her in Mexico Yeah So just a little bit of that stuff to figure out, but I don't care if she's in Mexico.

,OK. Cool. And the other thing we don't have to figure it out right now, but even though. The account directors are going to work on their leading and lagging goals. During the eight week sprint, we could probably start using that time to also figure out what we want bonus structures to look like,,Yeah. Um, well, I think if they do a good job with this NRR sheet, we asked them to go back as far in time as they're able to last year, at least till June or so. So then we could at least like put together a half and then, and then we can say, Hey guys, like, okay. Over the second half of, of, you know, last year, Exactly. And then we can build it based on what that will look like for this year.,I got you. I like that.,Well, and it can give us an idea of what we are willing to pay and what the targets are because a number right now would be arbitrary. But if it's like, hey, you lost If it's like, let's say it's negative $1 million, then we might have $100,000 a quarter to pay out. Yeah. In total between every level but Obviously, they're not gonna hit that if that's the case. They're not gonna go from a million to zero.

 Mm-hmm. Maybe they will Mm-hmm, but yeah, but at least then when we're talking to them about it, we're like, hey Yes, we lost this much money Yeah, we're willing to pay this percent of that money Totally.,And that will be...,I like it. But, oh, that conversation should include associate directors and directors. It shouldn't include strategists, because, again, we don't want the strategists focused on money. Yeah, they're just focused on money. Exactly. And so they're still going to get bonuses, but they should, I think, be flat rates, but they should make up a portion of the overall. Yeah, that makes sense.,Yeah. Cool.,All right.,Sounds good. And then for me, do I need to set up rippling or something for now that I'm an employee? I haven't signed anything or done anything.,But you're not an employee. We have to figure that out before the end of January.,Oh, I thought we were starting January first. I thought that's what we're doing.,You started full time. It's the same thing. Oh, got it. Okay. You got paid as a contractor, right?,Before Yeah, I thought when you said starting January, I thought you meant I'm down.,I'm down to start making the switch. But we haven't. That's what I was asking about.,I thought you wanted to start as an employee January 1.,Oh, did you not get paid?,I don't know.,It hasn't been the fifth yet, so I don't know. Oh, yeah. So what we're expecting is an invoice. That'll get you halfway through. If we can figure out what your bonus structure is between now and then, because we're agreed, I think, on the salary. Yeah, totally. I'm fine. So when we were meeting in office, we were going back and forth. And you remember the $60? And the squigglies yeah I was like okay well we got to figure out some of these numbers because so I think going back in the half will also you know contribute to because you're you're essentially the top of this and our bonus totally yeah so if we figure out how much is there I don't care you can tell the team that that they get three 93% of the overall and you get 97% of it.

,I don't give a fuck but we'll figure out what the total amount I Just I got confused and I thought you were wanting me to be an employee as of like yesterday. Oh I'm totally cool with that. I just We didn't get to the point where we could come up with I thought that's what you were saying And I thought we were gonna figure the bonus structure out in a couple weeks or something something. I didn't know.

 But now I understand you want me to just be a contractor until we lock it in, which is fine with me.,I don't care. Yeah. So it sounds like on the fifth, you'll get paid for the first half of the month. So if we can figure it out by the 15th, then great. If we can't figure it out by the 15th, we'll pay you one more time and we'll have to figure it out by the 31st.,Yeah, that's totally fine. I'm super flexible. I didn't I wasn't like make it weird. Thought that's what you had said.,So I was like, oh, do I need to be doing it? Maybe it was, but we still didn't figure out that. And if you're comfortable starting as an employee without signing for that, I think we're already past the first, so you're probably better off getting paid on the fifth through, and that's through the 15th and just joining the second pay period anyway. Which I'm totally totally cool with. I just my thought.

 It might not have been what I said. I don't remember exactly what I said, but in my mind it was like, OK, we got to figure out this bonus thing. Yeah, no, I'm totally down with that. That works.,I don't even care if I'm a contractor all of January. I just thought that that's what you said. And I wanted to be like, oh, do I need to be signing something? Do I need to set up rippling? Like I didn't know.,I invited you to a Tomorrow is optional it is Not that big of a deal it's meeting with the billing company and our BD team just trying to figure out you know, if we can if we can Work it together. Yeah And I don't want it to be a big focus of yours just because the cross selling and upselling hasn't been figured out at web serve. So once we get good at that, then we can worry about getting good at selling them out of web serve to other things that we do.

 But but I want you to just get an idea of what we're trying to accomplish. Because the billing company makes crazy profit margin. Yeah. And the clients pay more money. Right? We get paid a commission of like, 5 to 8 percent of their revenue. Yeah, so if if they do 2 million a month, you know, and we're getting 8% of that It's like a hundred and sixty K. Yeah, yeah That is insane, dude. Yeah, but most of them don't do 2 million a month.

 They do like 200,000 a month and but it's still oh, yeah Yeah, yeah, that's really you guys have hit a cool little thing there Yeah, happy to jump on that one, that'll be great.,Yeah Regarding the sales side of things is if the directors want to upsell a client or cross sell a client Do you Have the directors kind of manage that whole process on their own or do you send them over to a sales guy? And then the sales guy manages that process.,What do you prefer? What I would prefer to happen is it be super casual on monthly leadership syncs that they've already identified, okay, there's a potential opportunity for this client and have enough to just open a conversation Hey, like, you know your PPC is doing okay. I think it could be doing a lot better if you had performance design It's not very expensive like And what it is, it's like conversion rate optimization if we up your conversion rate by 2% Just with your last three months numbers that would have been four more admits it would have cost you six grand and Those four admits like right now you're spending 40k to get those admins.

 Like, do you want to have a talk about it? And they're like, yeah, I want to have a talk about it. And they're like, okay, cool. I'm going to put you in touch with Cam and just bam.,That's all they got to do. Okay, cool. And so Kim does that stuff.,I was thinking it was like Chris or Paul, but Kim or Chris or Paul, we don't have a we don't have a process.,We need to build that.,Got it. Okay. Yeah. But that's that would feel the most natural to to me.,So it'll go to Kim, she'll have the discussion, get an SOW, get it signed, and then she would then loop them in with Shannon, who will then take over the account.,Cool, I like it. Whatever happened with winning by design, we kind of ducked them, and they just fell off the map, I guess.,We decided that Laurent was more important right now, and then we wanted to keep him.,agree but uh but they were like getting a little pushy about the end of the year because and oh right fairness on their end is like that's what I had initially told them and then I dropped off a little bit on them but uh they gave me some spiel about how if like I didn't come to terms they've got like all these engagements that were starting and if I didn't start at the beginning of january then I wouldn't be able to start until maybe maybe after February.

 And I was like,,Yeah, but normally it's a pretty big bluff.,Yeah. And I just haven't heard from them since I did that. So I'm guessing. I don't think it's. Maybe it wasn't a bluff.,I don't think it is a big bluff because usually like they'll just be like, Oh yeah, we found some room to fit you in if you change your mind. Yeah. Oh, you know we thought we couldn't fit in but now actually a slot opened up, but that makes it that makes it a bluff Right. Yeah.,No, I used to do it with vids all the time. I It actually worked a lot. Yeah, it does. Yeah, it's urgency. It's uh, I don't I don't love it but but Yeah SEO deck I feel like stink Laura said it was pretty good, but it's a little bit old school, doesn't touch on any of the AI stuff, doesn't touch on any of the video stuff that Google is sending a lot of traffic to these days and brought that up.,That's good. Yeah, I was feeling like we need to bring in some kind of like innovation and how we're pushing new technology. And then also, I honestly think that hitting more on their pain points Like a slide that's customizable for their paint their custom pain points that they brought up during the discovery would be good like more than just data and screenshots, but like actual like Pain point bullet points where we bring solutions directly to what they brought up, you know Yep also, I think a couple of the slides are just like too much like I know you didn't ask for my opinion, but I'm just giving it I think some of the slides aren't very impactful like they're cool, but maybe they could even be compressed down like into one slide Like let me bring it up So there's who we are There's more than just marketers.

 Predictable patients, five core principles, your team. I think your team might come a little bit early in it.,Yeah, I feel like it's a little early.,I also think that predictable patients and the five core principles should be one slide. Way too much copy and stuff going on.,I think that's like one slide. Yeah, but the second slide's really good. And the first one's just introducing it. So I think it's like an important part of what we do. I do think it could be compressed into one slide. But I think everything it says in both the slides would probably need to be in The the two because it's like what we're trying to drive with the methodology and and Laurent will make it better but is is Specialization we're different than all this bullshit that you've been dealing with and here's why mm-hmm Yeah, and and we're the exact thing that you're looking for we're not just another marketing agency so That's the point of that one.

 And maybe we're not knocking it out of the park yet. But that's why it's got two slides. I get that.,I just have noticed when there's a lot of paragraphs and things, it's like people aren't able to read it. It's OK if you're going to send it to them in an email. But on a presentation, I feel like it's not impactful.,So I walk Kim through presenting it and she'll breeze through it. Hey guys, this is our methodology. It'll be included. Uh, I'm going to email this deck to you after the call, but uh, you know, it's like a model because then your presentation is less impactful.,Like if you do a presentation where what you're seeing on the screen is like big words and big headers and numbers, and it's like, you're connecting directly with what she's saying. It's really like, impactful whereas if it's like All these random paragraphs and muddled and I don't even have time to read what I'm seeing But then she's saying something and I'm like trying to follow what she's saying It's like,it becomes kind of just like not useful and not impactful in my opinion. Yeah. No, I I don't disagree So real quick so there was a There was a to a I know you guys are working with us. But I put together this deck for you guys. It's a lot of templated slides. We'll go through it real quick. But the important thing for this call is just kind of figuring out what's going to be best for you guys. You guys already know us.

 So let's skip through here. But we do have a methodology that's very specific to behavioral health care. And there's some principles here. Maybe you should read it. But cool, how our paid media works is you work with a specialist and an associate director, that's your account team. They're going to be, you know, working on strategy, they're going to be working on you week to week optimizations and ongoing growth.

 Here's kind of our progress here. So we're gonna have this intro call. We'll bring your account team into this strategy call. We'll come up with a scope of work. But I know you guys were asking kind of some questions about budget and all of that. Typically, we perform a thorough analysis of your Google Ad accounts. You guys don't have them.,So it's probably not going to be applicable.,You said this was a cross sell from SEO or something? Yep. Got it. So, okay. So here's kind of just what we focus on. We focus on leads, VOBs, approved VOBs, and ultimately admissions. We don't care about clicks or any of the vanity stuff. Here's what it looks like working with us. It's a 12-month agreement, and we spend the whole first month kind of preparing. And then, yeah, strategy stuff, blah, blah, blah.

 We do goal setting so that you know, you can see continued growth over that that year and You know you had talked about what's a good suggested budget? Typically when people have one location we suggest about $30,000 and spend That could change quite a bit. You know, if you want to do something small local in network stuff, you know, yeah, basically We suggest starting that at like 15 K. Sometimes people have 50 beds and we suggest they start a lot higher I told Kim to initially start her her You know when people are asking questions like that throw out a number That's like the number of beds that they have like every six beds should be about 30 K and spend Not to fill all six because they probably have other other efforts going but you know just as a ballpark number that whittle it down from there.

 So I have some gem, bang. Start with that. And it's all templated slides. That part's not supposed to knock their socks off, really. Hey, can I take a leak really fast? I'll be right back.,No. I have a bladder the size of a key lime, and I drink water all day. Why don't you just pee on the floor?,I should. I don't know.,works.,So my question is, why, if it's already a client and we already know like a ton of stuff about them, why wouldn't we do like a custom proposal where we're like, Hey, we know you, we've put a ton of energy into a proposal. Here's what we know. Here's what we know about you. Here's what we know from similar clients. We've collected all this data here. Like here's why you need to run ads and bam, like solve all their problems in one proposal instead of just like, throwing out kind of a reintroduction with a little bit of info about our ad services.

,I'm curious.,Just so that Kim has something to say, so that she feels comfortable, like, because she's like, oh, should I have Sam or Mitch on this? And I'm like, nobody. Yeah.,So let's just forget about our current process. Let's picture like a perfect world. Just has unlimited people and resources, right? So in a perfect world, I would say we need a deck that is set up to be customized very easily for cross-sells. It's a cross-sell pitch deck. And it's literally like, hey, here's how this new service ties into the service you already have and how it's gonna 10X everything.

 Because you're coming from multiple angles, like you've got your SEO, you've got your paid, Here's how they tie together. Here's how it's going to increase your results. You already have a strong foundation with us. You don't have to re-onboard. You don't have to do anything. We already know everything about you. All you do is plug in the service. We're going to actually give you a discounted rate because you're already a client and blah, blah, you know, so-called discount.

 And then make it like really impactful, you know, like, so it's literally.,Yeah, no, that makes sense. Sense to me. Yeah, the reason we don't do that is the same reason we have no process whatsoever for tracking cross sales upsells and don't really get them.,So basically, the person that would help gather this info could just be anyone with some extra time in the paid media department. It doesn't even matter, right? It would be the account manager of that client. Sorry, this is a cross sell. So it'd be a account manager of associate director. It'd be an associate director.,Okay.,Yeah. So what's keeping us from doing that?,Just basically setting up a process for it to happen. Um, well, that's, that's a lot, right? Like, uh, I'm not, I'm not sure. I'm not sure that like, So in this case account access isn't relevant right because they don't have a Google Ads account Like they're starting from scratch With Google Ads and And they identified a cross sale opportunity. Mm-hmm And they are going to need a little bit of help.

 And all we have is the sales system that we have. And they got a little bit confused on what to do. And so all I could tell Kim was, to a Well. Not that we have to ask for 36, I guess we're going to ask for at least 18.,I'm not saying what you did here was wrong.,I was just saying, like, how do we optimize this to be a lot better? Yeah, yeah. So. I think one, our our proposals. And in all this need to make aware of all of the services that we offer. Just because like, I think they should, I agree.,I think they should be aware of all our services, but I also think we need to make, as the authority, we need to make suggestions based on what we know about them, you know, as the agency. So it's like, Hey, here's ours. Like, I feel like a cross sell pitch. It should be like, hey, here's our services. We know we mentioned this one service, paid media. Here's why we think it's the perfect fit for you and why it's your next step.

 And then show them a couple of example clients that are similar to them. So we can say.,Who owns the process? So I think that what you're saying makes sense. Kim would just handle the contract of it. I think that one associate director would reach out to the department head of the other one and book directly with them so that that person that they know and trust is involved. And so they're like, yeah, okay, cool. Like you're interested in that. Let me, let me do this. But I'm gonna schedule with you and Mitch.

 And yeah. Yeah, exactly. But as of right now, the reason I didn't want her to include Mitch was because Mitch is busy with a million things that he shouldn't be busy with. Mitch should be worrying about NRR. And that should be like music to his ears. But it won't be. Because he'll be like, oh, we don't we don't have enough staff members to handle this and blah, blah, blah. And I don't disagree with him, but but I think all the all of those things are his fault for not being on top of it because he's he's so involved in.

,Yeah. So we're fixing that. Yeah.,Yeah.,That's going to be fixed soon. You know, stuff like we're I have basically resolved the issue of people asking a million questions a day. So that's pretty much solved. And then I'm working on hiring an account analyst out of Mexico so that they should be hired in the next few weeks. And that's going to free up a ton of people's time. And then we're also hiring a paid media manager or whatever associate.

 And so that's going to hopefully take a couple clients off his plate.,Yeah, no, it's okay. I want I want Mitch touching our blue chip accounts. So like the pinnacle account, like, I eventually want to get it away from Mitch. But, but it's okay if they're with him forever. But if they are with him forever, he can only have like two of those accounts. And so if he's only going to touch two accounts, they better be our two I guess my point is, is not to like say that what we're doing right now is horrible.

,I'm just saying like, let's look forward over the next quarter. We're going to be getting Mitch freed up. We can build a cross-selling deck that's better. That makes more sense for an existing client. And then, yeah, they could work together. So Kim, would you like to add anything to that? Associate director to build out these proposals, you know, and they should be pretty easy.,I think it's more about just getting the messaging, right? Yeah. Yeah. So cool. Let's, uh, let's add that to maybe, uh, you, Kevin and Lauren. Yeah. Figure that out during this, uh, process.,Yep. I'm adding it to my list of things.,All right, cool. Yeah, awesome, man.,Sounds good. Awesome.,I am going to take my son to the dirt bike track after this, so I'll be available by phone for the next like 2 hours, but I won't be in front of the computer.,Yeah, no worries.,All good. Yeah, is there any way I can support you.,Anything? No, I am. I'm doing good. I'm happy.,Right now. I just I want to keep an eye on what we're spending in all these places.,That brings up a really good question that I had. You can stop presenting if you want. Not even 90%.,There we go. Nice.,All right, so I feel like we need some kind of a, uh, some way to track visibility or finances in a way where I can see what's available for hiring, firing, whatever.,Like in other words, I mean, technically we want our payroll under 30% of our top line revenue and it's above it right now. So that number would be negative. Yeah. So where do I even see that though?,How do I know where to find that.,How do you find payroll?,Well, how would I see what our payroll percentage is?,Like, you know what I mean? It's on any P&L.,Like, you could just I have a P&L. But you got QuickBooks. Okay, you're talking QuickBooks.,Yeah, so we're not very good at this. But the targets 30%. You know for and we're we're gonna be way above that with with you plus plus Laurent here until we grow a little bit but we're okay you know going into 35 and we've even been above 40% a lot of the time but if you just go into a Reports. And then it profit and loss. I think what would help too is if I could start being a part of some of the financial review meetings if you have that.

,Meet and like go over everything.,Yeah, yeah, you should. We just don't really have them, so that's probably something we should incorporate in. Let's just go last year everything changed Months run a report Cool, so we have two payrolls, right? So we have this payroll total Okay, and then And then after cogs we have another payroll somewhere Here 803 So what what payroll it who's getting paid before cogs? Who's getting paid after COGS.

 Yeah, so the COGS are... Is that like vendors or contractors only? No, it's, you know, Kevin has been like marketing for us. He's not COGS. It's anybody that provides services to clients And then anybody that doesn't provide services to clients I would be after cogs you're after We're overhead Jordan would be Overhead.,Yep. Yep. Okay.,I got you now so yeah that that way we can figure out what our what our I Really? It would help me if we did like a monthly Financial overview where we're talking This kind of stuff because then I then I have better visibility on like where this this number here is really really important This gross profit. Yeah As well as The bottom line is is nonsensical Right, uh, because you have your other company the billing?

 No, the billing company doesn't run through those QuickBooks, but we arbitrarily pay, for what would seem arbitrarily to this, we pay holding companies a bunch of money. Our bottom line number, we try to keep it somewhat close Yeah, I gotcha. You know, $629,000 is what it says for the year. But once they finish December, the 265 is going to turn into a negative number. So it'll say we've made like $300,000 this year.

 Yeah. But we didn't. Yeah. $300,000 is like what have to pay California income taxes on if that makes sense.,Yeah.,Because all of our money goes to you'll see it. It's like net other services, outside services. So this all would have been profit.,So that's what's going to a holding company.,Or just different stuff.,Yeah.,Okay.,All right.,And actually like consultants here, Laurent will go on this line. So that will be outside services. But the big ones are these, look. So PowellCo and McHenryCo. So that all would have gone directly to the bottom line. This would have gone to the bottom line. And this would have gone to the bottom line.,What are your thoughts on hiring a director of finances or something like that to really own all this stuff?,We're doing consultancy or advisory with our bookkeepers right now, and it's getting a lot better, and they own it right now. We couldn't afford a finance director. I think it's something that we need, but we're going to have to kick that can down the road.,I have spreadsheets on how every agency I've ever run, I've run it off of a spreadsheet. And it's how Bastion Global even runs their stuff. We can really start to try to implement that. Because what it helps us do, like, I don't know, are you guys setting quarterly revenue goals or stuff like that? No, but we should. Yeah, like all that stuff that can't happen out of QuickBooks. That needs to happen in like a tracking sheet, just like we're tracking NSMs, just like we're tracking all this stuff.

,Yep. So, yeah. Yeah. So let me show you. I could even like, because I have some examples, too. But yeah, show me what you got. But I don't really want to see it right now. Yeah, that's fine. Sorry. Not because, not because, uh... Maybe So he uses a bunch of stuff running a spreadsheet Like this. I can't see anything Okay, now noob is North America.,Why does he say North America?,Because he has an international unit and goals there.,Oh, that's cool. Directive does. Wow.,Yeah.,Well, all right. They're good.,Yeah, yeah, no, that's awesome. Yeah, this is way more simplified than the one Bastion did. I didn't impose it all onto here. But I like it. Yeah, like this is the kind of stuff we need. We need all this. Agreed.,Absolutely agreed.,So I actually am friends with the CFO of Bastion, who was formerly CFO of Bastion, and she consults. I get her to help me for like It's really cheap to like settle this kind of stuff up Like she could probably set up our entire Tracking sheets and everything for like under five grand. You know what I mean? Let's let's talk with her. Yeah, I Haven't spoken to her in a year, but I know she'd be down to help me probably if she has time that is But she's east she's an absolute beast like free She's a freak in the sheets.

,She's a freak in the sheets, dude. Good. She's like a bird dog.,Like she just gets in and just hammers it out and like gets what she needs and like in and out, you know?,Yep. Okay. Well, I'm interested in that for sure.,I think that's missing a little bit for me. Like I would, I feel like I can help you so much if I have that visibility and I know like, okay, what's where's it?,We're lacking in all kinds of visibility systems.,Yeah, it's okay though, we're gonna fix it.,Like, I am just so impressed with where... Wait, wait, wait, I gotta answer this. One second. Okay. No, you're good to go. That's not awesome. Uh, do you still want to go? Okay. What time are you thinking? Five? Okay. All right. Sounds good. Yeah, no, for sure. Okay. Just keep me posted. I'm gonna start getting ready. Okay. All right. Sounds good. Just know, I think traffic on the way to your house every time.

 So it's possible that I may need more of it. All right. You should. You should. All right. I'll talk to you soon. All right, bye. Sorry. No, all good. That bought me more time. Nice. Cool. I know. We could get more into it if you want. No, I mean, I'm just kind of like, there's just so much stuff that we can work on.,And I'm really excited about it. So I want to just make sure I'm not working on things you don't want me to be working on. I guess that's what I'm a little bit afraid of,my fingers in too many pies, like, and no, no, you can touch everything. Okay, we're gonna pay a lot of money and better, better get all the value. But totally. But yeah, there's nothing off limits. I the whole idea of that. I don't want to micromanage you. I am very interested in this initial strategy sprint, just so that we can and get on the same page of what every department's doing this year and what we're doing this year.

 And then we can say, OK, we did it or we didn't. But other than that, no, I don't want to tell you what to do. Well, I feel like, honestly, I feel like you and I need a strategy sprint.,While we're doing this with the directors, I feel like you and I need to road map out, OK, over the next Let's plan 2025 of what we want to get done. We want like financial visibility. We want Employee visibility. We want bonus structures. We want to reduce NRR and I feel like we need to then implement a strategy for this whole year of how you and I Will implement, you know, okay Yeah, and then you and I have a roadmap so I'm not just like running rampant even if it means I'm doing most of it.

,I'm just saying at least then we're on the same page. Okay Yeah, so growth goals how we even set goals would be pretty important Yeah, and then everything around bookings so Their bookings goals are crazy 1.5 million a month in bookings I guess that's not that crazy.,What was that? Sorry. No, I'm just looking.,Yeah, so we need to be able to set growth goals, retention goals. Revenue retention, obviously we're setting goals there. And I do like this. What are you looking at? Here, I'm going to make a copy of this and then share it to you. Okay, cool. Just so that you have it and then you can me the bastion ones. Because yeah, this is like for the executive team. Here's all the detail. I think it's good. I think it's really good.

 But no, I'm I'm starting to feel like there's a path to getting all this stuff. There isn't even just like, getting this sort of visibility, like it's a daunting task. Just like getting the NSMs in place was a daunting task. And so we're kind of working from the bottom up rather than from like the top down with this stuff because trying to solve for retention. I'm not even really all that worried about growth.

 We could crack down on the sales team and like, Get a lot more serious with this stuff, which we'll have to but there's just other pressing problems, you know Yeah, um, and so that's that's kind of the reason why um Yeah, uh, I haven't even cared that much.,Yeah, totally well just lean on me man, like I I know a lot of this stuff is daunting, but like I'm gonna push it through we're gonna make this shit happen and I think it's gonna be We're going to look back and think, actually, it was easier than we thought.,Yeah, so I do want to be tracking gross margins, for sure, because it's pretty important. And then I want to track EBITDA margins, but we're just going to have to do some add backs in a different way, which me and Kyle do on a one-off month basis. But we don't do it every month in any sort of format. Yeah. So we'll be like, OK, our our profit margin is like 20 percent.,Yeah. Dude, if we get Tracy involved, she'll like, She'll hammer all this stuff out for us. It'll be like crazy. I'm trying to see if I can find. Oh, yeah.,Oh.,I don't know if I can show you this. You can show me anything your heart desires. You just, you gotta want it.,Well, I want to show it to you, but then you might see Bastion's numbers. Okay, so I'll just show you this is some old numbers from Bastion. It's pretty old. So whatever. Not a big deal. I don't care.,I'm not gonna I'm not gonna share it with anybody or screenshot it or anything.,So yeah, this one was duplicated out of the original so it's like the formatting got kind of jacked up and stuff but this was from like year two or something of when I was in Bastion. But you can absolutely Yeah. Well, here's a dashboard similar to what you were showing me. So there's projected, and then there's forecast, and then there's gap. And every month had a forecast. So we had to forecast our June, forecast July, forecast August.

 And then there was booked, whatever's signed. And then what was our gap, whether it's positive or negative, from our forecast. And then for each department, so there's digital services, There's production, there's social media, there's design. And then there's a tracker for every single client of budget, actual, variance for every month. And then there was a budget here. So you'd have FY budget, and it includes everything, you know, how much room there for raises, bonuses, subscriptions, everything.

 And then you'd have numbers at the end. We could see what our overarching percentages were. There's a P&L. But my point is, is having the dashboard where we don't have to run filters and run things all the time. It's all right there. And it's just up there. You know what I mean? And so I don't have to go figure out and take 15 minutes like, oh, can we hire someone? I know, I can just look at my spreadsheet.

 I already know we've got X amount available for hiring if we need to or whatever. But yeah, Stacy would set all that up for us. It would take her probably like a month, but she would, maybe less actually, because your QuickBooks is pretty organized, which is good.,It's getting a lot more organized by the week. And I can invite you to those calls Okay.,Which calls?,The advisory with the bookkeepers that are structuring it more. Yeah, that'd be great.,At least so I know what's going on. Cool. Maybe I should call Tracy and see what she's doing.,Yeah, give her a call. All right. Oh, you're calling her now.,I'm calling her now, but you can leave if you want. Should I leave? I don't care. I brought her in when I was CEO of Outlier Agency, and that agency had zero financial tracking. She came in, got it all cleaned up over like a month. Got visibility set up everything it was freaking awesome Cool.,Well, then I'm gonna let you go, but I'm gonna call Trevor. He needs me. All right. See ya.,All right

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: kk i'll join

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Tryign to remember how I had it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Did you move anything around in the typeform?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey there~

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Looks like the logic on it broke

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So any department can use the same form and it sends them into the right dependencies

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Keep in mind I am trying to make it so the form applies to all departments

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It has a time machine setting I could do

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Should I reverse all the changes you made?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: got a sec?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Especially client calls, zero exception

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you let your team know they should have an invite to read and to start allowing it into all calls?

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan & Mitch
Meeting Participants:Jordan Dahlquist,Mitch Marowitz
Start Time: 2025-01-02T21:17:44+00:00
End Time: 2025-01-02T22:20:55+00:00
Transcript: I heard you went out to Palm Desert or something.,Yeah, I went out to Joshua Tree. It was technically Landers, but then we made it over to Joshua Tree in the morning. So I got up early, saw the sunrise. Yeah, it was a good deal. Just me and my buddy.,Right on. Sounds epic, man. Yeah, it was cool.,I'd never been out there.,Yeah, I love that area. I want to take my truck out there and go do some exploring. You have a nice off-road truck? I do, yeah. Sweet. Yeah, I have an F250 Platinum, but it has the Carli Pintop 5.5-inch lift with 38-inch wheels and just every modification you can get.,The total toy suite.,Yeah.,Did you geek out? About that with Kyle?,We both talked briefly that we're into that kind of stuff, but we didn't like go into it too much. I heard he's he showed me a picture of his Baja truck, so that's pretty cool. Yeah, he loves that thing. Yeah, sounds fun. Well, come on. Yeah, so OK, on this call, we're just going to go over whatever. My main goal is by next Wednesday for that training call to just have as much stuff lined up so that we can train the team on the new processes.

 And if we don't get to everything, it's okay, but at least get them going down the road, like better type forms. They can start using Cloud. We'll train everyone again on Cloud for anyone that missed it. We'll talk about creating ads. Ad copy with it, landing page copy. You've been working on that, which is great.,Yeah, the landing page copy is done. I would like to have different variations, but that's solid for now. And then, yeah, next idea is the ads. Amazing. Yeah.,And for the ads, I think it's going to be pretty easy. But you said you tried one and it wasn't working very good. Or was that the landing page one?,That was more so the landing page one. Honestly, the the ads should be easier. I think so. Because there's a lot less to it. You just have like headlines and descriptions. And it doesn't need to get very creative. You just need to get creative with like a few things. Um, totally didn't make the landing page one. I just copied and pasted content so that like, everyone didn't need to make a private project.

 It's so annoying that you You have to use Google Docs and connect it. It has to be a private project. Anyway, what am I trying to say here? Yeah, I'll come up with something. I was hoping to even, but this one's probably gonna have to be a private project. I was hoping to, we have like a skeleton that you can just import Google ads editor like the offline editor if you could just edit this spreadsheet and make it so that the person can just Upload it and it's all done would be amazing.

 Um, say that one more time Uh, so we have a skeleton for the national campaign and you just like it's a csv and you just upload it to the offline editor Uh, and there's the campaign Yeah So you can,actually have clouds Spit out a CSV doc for sure.,Um, yeah, if it could understand it well enough You think it would be able to? Yeah, the exports come out a little bit funky, which is why I'm a little concerned Like it doesn't always print out everything, but I think it should be good enough to be like, hey, here's your head start Okay.,Yeah. Well, let's look at it together get it put together and it's not quite working perfect, let me know and maybe I can help problem solve it with you.,For sure. The thing I'd need your problem solving efforts with is exporting any channels because I gave that.,Oh yeah. So you need that because we're still working on the question answering thing, right? Yes. Did you try making it public and then exporting? Yeah. Did you try contacting Slack and what they said? I would do that next, because they'll probably have an answer very easy. That's fair. Yeah. Probably faster than I could figure it out, because if you can't figure it out, I'm probably not going to be able to.

,It was weird. It didn't even find the channel.,So, yeah, I think Slack supports probably good next. Yeah. I would just shoot him a message and just be like, yo, here's what I'm trying to do. Can't do it. Help. Yeah. And then. OK, cool. Okay. And then the next thing we should hit on, I guess, is the Asana stuff. I built out that custom form for design requests, so that's going to hopefully help with PPC to design and SEO to design. But I think the deal is, is we, when you fill out that type form, it automatically creates a task for the design department and tags.

 And everything. It does it all. So like nobody even needs to go into a sauna. You know what I mean? All I really need to do is just go to that type form somehow. So I don't know if that happens in a sauna or if you want it to happen somewhere else. But like I don't need to create or do anything in a sauna other than if Shannon responds in a sauna and ask a question or something, you know?,Yeah, I think that's thing to be in Asana. Here, let me share my screen. And then that Asana task just says, hey, complete this type form.,Where do I have this? Anyways, yeah, so I was editing this. And then I wanted to have the project roles and all this stuff. But anyways, that way, the task is assigned to them. Because I still want everyone to work, unless you have a different vision. But everyone work out of a sauna so they know what to do. And that way, they know to do the type horn.,Yeah. I guess my question is, is like, does, do I need to turn off the Zapier that's creating a task after they fill it out? Cause right now what happens is they fill out the form and it's going to take everything they entered in the form and it's going to send it in to a task in Asana. And it actually Slack messages Shannon to notify her that there's a new project also.,Yeah.,Perfect. Or do you want to keep that?,No, I want to keep that. So there's this request landing page task, which would just be altered to Complete the form and then that will create 10-4.,Yes.,Okay, cool. Is there a way to Okay, never mind, yeah that works cool Yeah, all you need to do then is just clean up the Asana task. So it's actually and then you're pretty much good to go.,Cool. Let me see this. Send it to me. Well, you did send me here. Let me go.,I saw you sent me an invitation to my personal email.,There it is.,Don't worry, they're going to send you all that stuff anyway.,I know, it's so annoying.,I'm constantly having Unsubscribe from shit.,Yeah Do you have superhuman for your emails? No, I've heard it though, bro life-changing. Yeah You can basically just vim through all your emails like, you know Like just hotkeys for everything. It's really cool. Nice. I'm a big hotkey guy For sure.,Well, then you would love it.,You would also love them cows Is that similar? Yeah, VimCal is a calendar.,Right, well, I mean like similar idea like AI.,Yeah, it's all simplified. You can basically create and add calendar invites like with just hotkeys. It's pretty cool. It works crazy good. Best calendar. That I've ever had. I will look into that. Yeah, it's pretty.,Jesus.,I'm an inbox zero guy, too, though, so I'm a little bit like anal. Yeah, you don't like any notifications.,Yeah, I just don't like any emails in my inbox at all.,Oh, yeah, yeah, yeah. I get way too many. Yeah. Jeez, man. Sorry, I wish we didn't go through all this.,I just want to see the type form that you got.,Yeah. I hate when they make you fill out all this stuff when you join, it's like so annoying. I usually just pick a random one. Oh, I need to add you to the workspace.,All right.,Yeah, I guess so.,Let me go. Let me go add you.,Unless that other invite That oh, yeah, this just says join organization.,Yeah, I need to add you had to do the same thing for Shannon. OK. There you go. Any?,Okay, so yeah, if you go to logic in the top there, this shows the full roadmap. Whoa, did something get moved? Uh-oh. That's not good. I think Shannon may have broken something. Or someone did. Let me look here.,too much.,I didn't see you move anything.,So it goes.,Should I just try going through it? No, it's broken right now.,One second.,Let me ask Shannon if she moves.,I can go back in time. That's cool. I know this isn't what we're going to meet about. Let me try and fix it really fast. I think I can.,So this is all things design.,that looks like that is you can kind of zoom in and pan around and stuff on the type form if you want to see. But basically, in the upper left where it says who.it means, like, who are you? You're going to enter your name. Then it's going to go to the next one, which has you select what kind of project it is. So new project, landing page, ad set. If you hit cancel and go over to create on the upper left Well when you project like that Yeah, so this is what the next step will say so it's like what's your name?

 What kind of project is it? Is it a new project or a revision? What she changed everything everything oh no wow this is like really messed up right now um well hopefully she gets it how she wants um I think I see where so did this panel is completely different is this like,the main thing that she changed because it looks like she wants this to work current system or something.,Or I don't know.,Yeah, she's confused, and she messed up the entire form, unfortunately. Okay. She's responding to me now.,Well, that's a bummer.,Unfortunately, it has versions. Yes. Version control and backups are hugely important.,We have backups for one website, Okay, I'm gonna time machine the whole thing back to how I had it because she did not know and it's okay Let me see here Please let it be the right one I fixed it now. Back to where it was. OK, so now you could just go through it if you want. You're free to do that. But I made it so it works now. So if you want to go to Logic, I could show you the flow now. So it goes name, what kind of project, and under project, is it a new project or is it a revision?

 So in other words, whatever it is, I don't care if it's an ad, if it's a landing page, are you revising something that already exists or are you creating something totally new, right? So if it's a revision, it goes directly up to that top right section where it says enter the Asana project ID, and that way you can actually just continue the revision based on what the original project was. Was. You get what I mean?

 Yeah.,Does that make sense?,Yeah, does it? I don't hear you for some reason. It's weird.,I thought that might have been the case.,Can you hear me now? I wonder if my audio settings got messed up. That's weird, I don't hear you. I think it's mine. Let me try rejoining Can you hear me better now, yeah, it's showing your audio, but I'm not hearing anything That is really weird What the heck This is crazy Mike test Mike test And my speakers aren't working. What? This has never happened to me. It's like just not playing any audio.

,Can I play music? OK, music is working.,Mic test, mic test.,Yeah, because I was having a hard time understanding the setup of the projects. But let me show you how I've done it and then maybe you'll like it.,Yeah, I looked into it at one point and then I didn't dislike it. I just, we never moved over. But like I said, I think they didn't even exist when we first started using it. Yeah, possible. Um, you let me stranger.,Oh, yeah, go ahead.,Also, since you have yourself muted on the Google Meets, I don't know if your read AI is going to pick it up. What I just did was I muted the Google Meets tab so that your little note taker could. Oh, thanks.,Yeah. All right, so can you see my screen I can yep All right. So basically the way I broke it out in the last company This is click up, which I love click up by the way, but the song is song is good, too but um You have everything in in spaces which is like a portfolio Yeah Basically, and so there's operations which is like founder tasks meeting my you know success stuff for the company blah blah There was talent which is hiring.

 So like different categories of people that we had to hire and then under That group we've got different categories. So like active animators Inactive discarded terminated whatever So we're tracking everything in here area and then we had a space called clients and when you open up clients you'll see each client has their own board here and so for example GoDaddy you can open it up and we had a very specific thing that we did for these clients for this company it was like plug and it's very cookie cutter It's either makes it easy Yeah, the project is even is either need to start it's with the client or it's approved or it's closed.

 Yeah, and so A project basically looks like this Inside the project there's communication lines going on with the animator with the script writer There's the over overarching project script, there's attachments, there's dates, assignees, all that kind of stuff. But all that's within a client board, you know, and then you can quickly and easily get and look through all the different clients. So I do think having some kind of a portfolio like that could be good portfolio system.

 But I don't know, I could I don't quite understand, Osama, maybe that is kind of how it's set up.,I was trying to figure it out before this call. Yeah, I see a lot of similarities. Do you want me to run through it? I don't know the portfolios part, but it looks like that they have a similar structure, what you were just showing me. And then the projects technically were the same level equivalent on ClickUps. But yeah, yeah, let me see. So this is my task board. I just like having calendars like my default and I can like move things around so I can see all sorts of stuff.

 It gets crazy, obviously, and I can't get around to everything. But here's like the clients. I don't have a great example of a portfolio, but I was playing around with it for rehab path. And I know it tracks like progress and things. But anyways, here is the current PPC design. I was trying to do the same thing for tech team. I wanted Seth to be able to do technical implementations. But that's sort of a side note.

 Um, here's the project for, um, design as it is right now. So here's the invigorate landing page. You can see this task. This task is connected to two different projects. It's connected to, um, this one here and then also to the client. Um, here's the description on it. There is, uh, like communication within. Task itself. I don't know if there I guess there is communication at the project level, but we typically do all the project level communication within Slack with the channels, client channels.

 Yeah, there's different views, you can have a list. And there's different organizations for it. Like you'll see new landing page, new ads, that's equivalent to these boards. And then there's timeline. I never really use timeline, but Pretty similar to ClickUp.,Yeah. Almost the same thing.,Exactly.,Actually. Yeah. Yeah.,I saw a lot of similarities.,Yeah.,OK, cool. Yeah. You might consider leveraging the messages thing more often with on each task because then you don't have to go back and forth between Slack. And then the reason I liked it too is because then you have a paper trail on the task, on the project. And I don't know, there's like less room for error.,I see for sure what you're talking about. I have a sauna. I think at some point I messaged you like the notifications and kind of how I was, how I have mine set up and it should probably be standard for everyone. But yeah, so those certain things come in. If Shannon, you know, assigns me a task, it's right there in Slack.,Well, also you should have an inbox on Asana, right?,I do. I don't really, I mean, I see the inbox here, but since all the inbox stuff goes to Slack and I'm best with Slack, cause everyone's just, you know, communicating there. I like the Asana notifications too.,Yeah, I agree.,Communication on like tasks done within Asana is great. Cause yeah, like you said, you have a trail of what's happening for the activity.,Yeah, for sure. Okay, cool. So the question is where do you want So usually we get a client I just have this one mega template for all of them.,It would be great to have different templates, but anyways I'll hit use template. I'll name it and Then it'll pop open and populate something like this And these are the assignees and then the due dates So you can auto assign. So like as soon as it's created, you can have it like, okay, now like today's this thing, or it can be like multiple days out, whatever. So those should be situated. So you're going to create a task.

,And in the task, it's going to have the type form, and then we're going to fill out the type form. But then the type form is going and creating a task somewhere else too.,So that If the type form fills out the information on the test, I don't know what the zap looks like, I was thinking, you know, this was just a task assigned to them. And then they fill all the things out in the type form. New task and assigns that task to Shannon or whoever.,Yeah, that's, that works. Oh, I guess what I meant is like, now there's a whole nother task over in the design department. And I meant like, is that okay for you for your problems?,It's different, which is okay. Um, if it can go here, and then that that's why I was like, Oh, she tried. I was saying this stuff when you couldn't hear me. So Um, okay.,But yeah, if it goes here and works within the current system, that's awesome. It goes to workspace web serve, and then it goes to. Great task. Does it just go nowhere? Let me see.,Let me screen share and you can see them. Yep. Hang on. It's like the audio started working.,Google at all. You

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: need to pick your brain

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: cool, can I show you something in conference room?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool! Thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We can chat about it more, hard to slack the full context

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: The 8 week sprint will help me determine which route is the best.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Also, I'm thinking it's possible that the design dept. will need to disolve, and just place them into the SEO/PPC dept. instead.

I think the design dept. either needs to grow or it needs to disolve and the members just integrate into the two main departments. And then hire more offshore devs and designers to support for cheap.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Was chatting with Trevor, had a great meeting.

To support his middle management I think we should move Jenn into Strategist role over the AM's, and hire an AM to replace her current role.

Is that something we have budget to execute on?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: awesome

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hmm yeah I would ask Jordan Pohl about that and if she doesn't know then go to Rippling support.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Question - one of the PR contractors asked Jordan for 13th of Jan off - and Jordan told her it would be unpaid leave. I thought we were giving them unlimited PTO? Or am I wrong on that and it's holidays only?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I even get confused lol

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So you basically want a zap to send the call summary to the specific client channel?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah people call me JD to keep it from being confusing

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah seeing if i can get it to go into client channeels now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So it gets a bit messy

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: The main issue is that the read is only pulling from my own personal meetings, not the whole workspace

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So we would essentailly need a zap for each person that is synced up to each account's login

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm sure it's possible if I keep working at it and getting creative, but I'm not seeing an easy way to directly have it post to a specific channel

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I would just need each persons read login to set it up

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Which we could do

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We would just create a zap for each person

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok so yeah. was researching some more

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or why?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So design dept. just is too busy?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Are we using vendors outside of our design team to build landing pages? I saw something on asana about hiring on fiverr for a LP design

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: at all

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: They don't do anythign for seo

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: :face_with_monocle:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you think they actually output enough?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What are they so busy on?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: trevor told me yesterday

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: not in a long time

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: except web maintenence which they ahven't done in 6 months

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And we can take action from there

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think the 8 week sprint is going to hep me suss out a lot

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah that would make sense

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Pitchbox Training Call
Meeting Participants:Aleksandra Kazhleva-Popovska,Ana Arsovska,Jordan Dahlquist,Marija Vidacic,Milica J,Preston Powell,Trevor Gage
Start Time: 2025-01-03T08:59:40-08:00
End Time: 2025-01-03T10:00:17-08:00
Transcript: Hey, what's up, everybody?,What's happening? Nothing much. Getting used to the idea that we need to work again in the new year.,How about you guys? Hey Yeah doing good Our New Year's is kind of already over.,I guess I worked yesterday. I'm already back in the group It's better for you guys because you have Christmas and then you have New Year's and for us it's like yeah Yeah, that's so crazy. I never knew that before It's really funny Santa takes like a break comes back into action.,Yeah, we actually have presents for New Year's. So it's Yeah, it's everything. A bit different Christmas.,Yeah, that's cool. Can you guys?,Okay, cool. Sorry, it was my headphones were on. But anyways, how's everyone doing? Happy New Year. Happy New Year to everyone.,Well, nice.,So we just wanted to have this call because we want to train you guys on just this way of like resource page link building. And I found some great resources along the way and I can show you guys real quick, you know what we've been doing and how it's different from Kind of like the paid outreach negotiation that you might be used to And and I promise you it will work But but we got it. We got to try it this way not totally opposed to the paid stuff but But I'm going to share this with you guys because it's pretty interesting.

 But basically, we work with all of our clients to build content. And it's good, long-form, linkable content. And then this outlines the process. I know you guys do something similar. But I'll show you how it's different real quick so Content analysis basically looking at our our client sites and finding okay I think these three pieces of content are going to be the most likely to get links Because they're informational.

 There's a lot of writing about say depression or you know, whatever There's a some good websites that are talking about And then finding prospects, setting up communication, basically crafting your pitches. I don't know about all of this, but what I will show you is, so blogger outreach, pretty straightforward, but that's not what we wanna do. Obviously, this is pretty straightforward. Probably more what you're used to.

 So outreach response, and then negotiating a price. So then there's like resource page building. And so what people do with resource page building, they find, you know, they'll use these queries, and I'll show you more on this in a second. But they'll will say in the title or the URL, there's resources, the same thing, just different variants of these search queries that they'd put into Google. And then they'd find a bunch of pages that talk about similar things and have links or resources to similar type of stuff, and then they craft a pitch.

 But I've got like a couple kind of cheat codes here. So I was actually this morning, I didn't start it till this morning, but I started to try and, and put something together. And I'll send this to everybody after the call, but I'm not done with it. So. So I'm just gonna go through this really quick and show you guys kind of how this is different, then we can have more an open conversation and but really what we want we've got you know maybe 30 clients doing this I don't know the exact number Trevor would be better but basically what we want is one super targeted campaign per month per client and so we're not going to send out like mass emails per say our goal with prospecting is going to be to identify targets that are highly likely to link to us for free and so when working with like one of our clients you're going to want to identify the content right so I'm going to show you guys just real quick let's just pretend that we're trying to find links here we have these information informational content pieces.

 So some of these are really good. Opioid overdose prevention, that's big and important right now. And it might actually go really good on somebody's, it might be good to link to because here in the United States, and I think all over the place, There's a fentanyl crisis, and people are dying. So there's a lot of public support. And people are trying to obviously avoid the tragic overdose deaths. So there's a lot of talk about this.

 So you look at the content. OK, this is a nice piece of content. It's got long form content. It looks like it's pretty well written. There's different ways to, you know, or, you know, it's explaining what to do if somebody's overdosing. It's got a medical reviewer, adds credibility to it, clinical reviewer, it cites its sources. Okay, this piece of content looks pretty good. So, what I would do with this, and I'm going to show you guys a cheat code because we've got two options to create a prospect list.

 So, Ahrefs, we can find people that already link to similar types of content. Or Scrapebox, which I'm going to get set up for you, Aleksandra. We don't have it right now, I can show you how it works in just a second. Um, so first thing I'm going to do is, um, I'm going to go to this website addiction center, um, which, um, I've worked with these guys in the past. They have a team of like seven or eight people all day long, just, uh, building, um, building links all day long to pages like this.

 And so each one of these has had an outreach campaign done to it. The reason that this is going to work really well is because everybody that links to them, we already know that they're linking to similar content and that it's going to be relevant. So what I'm I'm going to do two things actually. I'm going to go to Ahrefs. Oops, I didn't mean to click that. I'm going to go through their content and find pages Give me one second.

 So I'm going to go like this. Let's go to Google. I'm going to go site addictioncenter.com. And I'm going to go, what's the content we're doing? Guide to overdose prevention. So let me type in opioid overdose. And then I can see all of the pages on their website. This is probably the most similar one, how to prevent opioid overdose. And so I'm going to take that exact URL that that page is at. I'm going to pop that one into Ahrefs and just see if they got any links to it.

 Okay, they haven't gotten very many links to that specific page. There is one.,We just don't see Ahrefs.,We only see Addiction Center. Oh, okay.,Sorry about that. So that exact page has one referring domain. I'm going to look at it. We can add that to our prospect list for sure. Addiction, the dark night of the soul. Yeah, this does not look like a good prospect. But so let's, let's go back to where we were. Oh, sorry. Let me just share my whole window. So cool. Addiction Yeah, it only had that one referring domain. It didn't look very good.

 But let's see if maybe that site got hacked or something. Learn the sign, save lives. There it is right there, just a link. But this site seems out of date. I don't know if anybody It looks like it's broken. So I'm going to go back to my Google search. Oops. And I'll just And I'll do opioids.,I'll even do overdose.,This might be a better one, but we'll just have to see. So copy that one. I'm going to pop it in Ahrefs. OK, that one has 519 backlinks. And This one is a treatment center looks potentially legit cool this is citing sources This might not be the highest chance to get a link But it's definitely worth it because we already know that they're they're linking to American addiction centers, which is a group of treatment centers an addiction center, which is a directory.

 They're talking about overdose. So definitely worth reaching out to them. But I would just go through this list because we already know that these people linked. And so we're not opposed to paying for links. They just need to be relevant. I don't think it should be part of the initial pitch, because people, if they want money, they're going to respond and say they want money anyway. And then if it's highly relevant, we're open to paying some money for links.

 But the goal is to get them at no cost. And then I will start to show you guys. I don't want to get too deep into it, just because for now, Like in the long term some kind of combination of both using a traps in this way Plus using a tool like scrape box, which again? Aleksandra will do something separately to get that going For now, I think if we can make prospect lists using a traps, it'll be better But the goal here in prospecting is we just need 80 to 200 outreach targets that are like high quality, highly relevant to the piece of content.

 So rather than doing 10 campaigns for the client in a month or a bunch of campaigns, we're just trying to do one really high quality campaign. And then we should be crafting a pitch that's personalized every time. So, real quick, right now, what do you guys use to identify contact information? Emails.,Thank you for combining all this.,So, we've currently tested several approaches. One was the competitor approach. So basically, we took our client, put it in Ahrefs, and then we took out the competitors that they have, and then we took out referring domains linking to the competitor. So something similar to what you showed is just that we didn't target a specific page, we went for the entire domain. But maybe the approach with the page would make more sense, as you mentioned.

 And then the other idea that we had was actually we were going with a relevant keyword and then searching in title, whoever has that particular keyword, and then make a list of prospects with that. And then the third approach we tried was actually the resource. Pitchbox has the ability for you to make a campaign within Pitchbox, which is called the resource page. So you basically type in a keyword that you're targeting, a resource that you're targeting, and Pitchbox gives you websites that have resource on that keyword.

 And it gives us the prospects. So those are the two types of campaigns we've tried so far in Pitchbox.,OK, and then does Pitchbox identify the emails that you're targeting right now? Yeah, yeah, yeah.,It has the ability. So basically, whenever you put the domains, it just finds the contact information from within. Now, what I've noticed is that if we make the campaign in Ahrefs and then upload a spreadsheet in Pitchbox, it doesn't find contact information for all of them. But if you do everything within Pitchbox, then the chances are it will find more contact information for the prospect. Probably, I don't know, something on their end.

,But they have a good amount of emails being found. So when we used Pitchbox in the past, we used this, hunter.io. And let me just see if this is a good way to go about it. So these are yearly. So not too bad. 600,000 contacts a year for 4,000 a year. That's a little expensive to commit to if it's not going to work, but we could try monthly, like on the growth plan, and then we'll we'll upgrade if need be.

 But I do think that Pitchbox has a direct integration. Because that can help you find... Yep. What's up? Do we actually need this?,Because we have like a huge list of websites that we're going to get. So we can might as well use those that we get in Pitchbox unless we want a specific ones to be able to find the contact information for it.,Really specific ones and then we can use an additional tool Yeah, if we don't need it, I don't want to pay for it so I'm I'm totally with you but I know for a fact that These guys what they do is they go into Scrape box they type in a Google query a modified query and part of like the art of Prospecting with scrape box. It's just like messing with these until you get it just right so I put some more up here But the resource page link building is It works really really well, and then as a bonus these edu links can be really good and sometimes Sometimes it can work pretty well so I would We can do that separately But I want to just start with stealing the most similar content where you think you can make a good a good list straight from Addiction Center.

 So let's just go back before this. No, we were here, but let's just go to overview, and then how many referring domains? So 78 referring domains. Some of these probably aren't going to be relevant, but But you can make a target based on these. But what you're going to have to do in the pitch is you're going to have to say, like, you're going to have to, everything can be templated except obviously, like, the name.

 And then here's a link to my article. That'll be the same one every time. But you're also probably going to want like hey I found your your resource page at this URL and you're gonna want to change that a little bit for you know whichever one you know you find linking so like actually spending a little bit of time I think you're gonna spend more time prospecting than anything else to get this right but But let's just, like, expand.

 How do I do this? OK, here it is. So they link to this with the word overdose. That looks like it might be a paid link, but maybe it's not. This is more of a blog and not a resource page. Let's look at this. One. Yeah, more of a blog here, too. But yeah, I would link out or I would reach out to everybody in this list. But again, you know, I think if we can make 80 to 100 outreach targets that are already linking to similar content, I think that we're going to have a lot of success.

 And then let me try real quick a modified query like I would do for this one. So let's just go opioid overdose entitled links. No, that doesn't look right. Let's go in title go helpful Cool so yeah, these are really really good because Because they already have links about overdose a lot of them are like high authority, like local pages that have to do with like government or university stuff. Some of them aren't going to link to us, but yeah, we can turn this list into a list very easily.

 Using this. So, Aleksandra, if you would like, we can start with just the Ahrefs link building. But yeah, specifically we're focusing on resource pages and finding links that way. The copying addiction center will be really, really easy because you'll be able to find like hundreds of different resources related to anything that our clients write about on their website. But if we run into a block, I will, I can, I can, I can get this set up for you and show you how to use it.

 But yeah, it just makes a list. And then, yeah, do you want to show me maybe a couple campaigns that webserve.scrapebox, I believe, a couple resource page campaigns that we did. I don't know how to get here. Yeah, sure. In Pitchbox, right?,Yeah.,Okay.,Do you want me to take over the sharing? Sure. Okay, just a second. Let me just move it because it's in a different screen. Okay, so I'm not quite sure how the girls basically named the campaigns because we were doing a different approach. So I'll just walk you through. So I think that what Pitchbox was trying to do is basically incorporate all of these approaches, different approaches, and making sure we do it within Pitchbox.

 So if we go with the resource page, they actually have the approach from here. So I'm not quite sure if Scriptbox would be necessary, but we can try it. I've never used it. So when you click on this one, you type campaign name, whatever, blah, blah, test. And then here, you can add your keywords that are related to the resource you're trying to to find. So let's say addiction center.,But that's probably not good. Let's like, let's do this as if we're like really doing it. So let's take that page. And I'll drop it in the chat for you. And let's just do healthy life recovery guide to overdose prevention. Okay. Sorry, I'm losing it. So I popped it in there. And then what you're probably going to want to put in keywords are going to be overdose prevention, opioid overdose. Yep. Something specific, it says.

,So we would need a category here. So let's say opioid overdose, maybe, without the prevention.,Yep, that's that's good.,Maybe even just like overdose.,Overdose prevention is good. I don't think I typed it well though. You have opioid overdose twice and it eliminated the prevention so.,Oh, you're good. Okay, not good. Overdose prevention, opioid overdose. Okay, so let's say these three, right? And then it gives you the option to set everything that you want in terms of DR and TR in Ahrefs, backlinks and stuff like that, number of referring domains, whatever you want to do.,I put the DR all the way to 100 just because, Because we want those links if we can get them.,I know it's going to be hard, but... Almost impossible, but let's try. So we can set basically everything to this.,And then traffic, yeah. Keywords in top 10, zero to 500,000 plus, okay. Yeah, at least 100 traffic's probably good. Yeah, this looks good.,We can just set everything, whatever. I don't know This is, to be quite honest, referring class C. Never used it, so I'm not quite sure what that is. But we can set it to maximum.,And then we go next. What is it saying? Oh, it's starting.,Just type in healthy life.,OK, whatever it is. Let's just make sure it goes. OK. And then what it does is basically it's acquiring the target, and at the same it's finding contacts. Okay. Then it takes, of course, some time to do that. Now what we've added as a step last time that we were doing this is basically trying a bit more manual approach into manually opening each page website that was part of the campaign and marking it as good or bad in terms of do we want to do the outreach to this one or not.

 So that would be probably that part that you were talking about for and a bit more narrow approach and stuff like that. And then what's good about Pitchbox, I'll just skip to this one while this one is doing whatever it's doing. It has the ability to pick up some things automatically, like the person you're addressing to. So if there is a name, you just put the code, it picks up the code. You can put URL and it picks up the URL automatically, the domain automatically.

 And then what Kevin, the guy was showing us, It even has an option once you get to the phase of personalization to use AI. And AI would basically scan whatever there is on the prospects page, and then it creates a pitch for the link. So that can be something that we can use in this more personalized approach. So even though it would be a bit more manual, it will still have this AI help there, whatever.

 So if we were to make the template here and just add hi, And then if there is no name, let's say it's going to be team Here I'll pop a template in there Okay I don't like this one because,it says shared on slack. You could say hey, I was doing a research but but This was just a copy paste one from somebody that did do research resource page building. But yeah, so hi, prospect first name. Yep. And then you could say I was doing research on opioid overdose and found your resource here, this URL. You know, I created a resource that I think would be a valuable addition to your readers.

 And, you know, would you be open to giving a link? And we can even use chat GPT to help us write like a few variants of pitches. Will it send like two or three different ones to see like what works because what I'd like to get is like a library of pitches that we've like tested and we're like, okay, we know that these ones work the best. Um, and so like, at least then we'll have better starting points.

 Okay.,We can do that.,But then to get that, uh, as a valuable result, the results we might need to test, like, I don't know, we testing this, you have so many Who are you reaching out to? What is that website? And then who is the client we are reaching out to? Because we have, let's say, two clients that have very little stats. So whoever will be adding a resource, if they're looking at that, they might be like, oh, well, I'm not open to adding a link to a website that has DR below 30, let's say, and traffic below 500 and stuff like that.

 So we can try and test, but I'm not quite sure how conclusive the results will be in terms of making sure, OK, this works and this doesn't.,But if we if we have like our strongest clients and start getting some results for them Even the weaker ones we know maybe they're gonna perform worse But at least we know that hey this templates worked well in the past And maybe they won't get the same result because they're they're not to the same point that other client was if we at least had you know a few pitches that we We we liked I think that would would be helpful and then Yeah, but I would absolutely try a traps With the Addiction Center because we already know that those people linked to them Using the same kind of outreach setup because like I know of people that work there.

 And, and I know how they, they do it, they, they don't even use pitchbox, they make a list through, like, spreadsheets, and the the manager, right. So like, Aleksandra, it, in this case, would be responsible for prospecting, finding all the prospects. And then like, everybody else would be responsible for or crafting the pitches. And then they do bonuses, which I want to roll out for you guys. We just have to start getting a little bit of success.

 They do bonuses based on, OK, if you're able to win a link to this page above this domain authority or from a .gov or .org, then you get an extra $100 or whatever. Certain links are worth a bunch. Bonus. And I would love to roll that out. Just want to start seeing like a little bit of success. So basically, I guess what we're getting at is we only want to go the research, the the sorry, the resource page route right now.

 We want to prove that out. So I think what you should do, Aleksandra is with every campaign, build one with pitchbox only. And then Build a side-by-side campaign with Ahrefs, with copying Addiction Center. Run them side-by-side for the exact same page target. And look on the client's website. You find the one that you think is going to be most successful based upon whatever you want. You can say, OK, the similar page on Addiction Center has tons and tons of links.

 I think this one's going to be successful because they were successful. And, you know, let's get, you know, just we again, we only need one really good campaign per month per client. And then as this evolves, like we have a whole SEO team writing content. If you guys find like, hey, Trevor, like this, this campaign absolutely killed it about opioid overdose. And We want to You know, we've been struggling with this client over here.

 Why don't you guys make a really good linkable piece of content for this client? And Then we'll build the content for you Make it like like an easy win For everybody and then another thing that we've had success with in the past I don't know if you've seen any of our like they're basically just type forms that spit out a score, but there'll be tests for like, like, am I an alcoholic, for example, or like, it's a depression test, am I depressed, those have been really good, because they're interactive.

 And you can say in your pitch, like, hey, like, I made this interactive test, and I think your users will really like it. And and people like that. So rather than like going off of hey, we want to link because Because we just want to link we say hey we created something really valuable and we think it's actually gonna add value to what you're offering rather than hey like We have this page and we really need links to it and like if you'll do it, I guess we'll give you some money It's just a different different kind of Approach and specifically in these like mental health and addiction people are more willing to do it because like because they actually care right and so we need to come from the Perspective of like hey, we really care about this issue and we commend you for making these resources available You know, we think we can't like we created this piece of content that That will help help your readers with whatever the topic is, overdose, depression, getting sober, whatever.

 OK. We actually have a similar approach so far.,So this is like an example template random that we've used. Quick question, do you accept link insertions? I've got a detailed and helpful resource on drug treatment that might be a great fit for your content. It could provide your audience, blah, blah, blah. But we can personalize it even more here. The thing that I wanted to ask you are you open to us adding a link to the resource in the email? The reason I'm asking is because that would basically mean that we're exposing the client immediately in the first email.

,Absolutely. Okay. Not only am I open to it, I think you guys have to do it. I think you have to include their page that you're asking a link from and our page. Because again, we're coming out like right at the beginning. Spending, not about money, about like, we spent time, effort and energy creating this great piece of content. And we think you'll like it. And so yeah, we can expose the client. And we can say, Hey, you can even tell them about the client, we can give you like little blurbs about like, how healthy life recovery has helped 1000s of addicts recover from their addictions.

 And like, yeah, we want it to be like really like a heartfelt, like, Hey, we actually care. And it's clear that you guys do too.,So yeah. Okay. And then, yeah.,Uh, in one of my templates, I can't remember which one, uh, I said, I think there was a line I'm really trying to raise awareness to this issue, like the drug issue I was talking about in the email so,I could use that again I guess absolutely and I think I think what uh me jordan and trevor should do is uh just give like some examples uh and maybe work with like claude or chat gpt and create something for you guys that uh you guys can pop in the to uh the resource and like it can can craft good pitches because, yeah, absolutely, we're trying to raise awareness on these issues. We're trying to just add value to what they're doing, or at least that's the approach that we want to convey.

,Maybe we can also try this one, the AI assistant within Pitchbox. Perfect.,That could potentially be really good, and if it's not good enough, then we'll make a custom GPT to do it. Okay.,I have more questions though, like in terms of the quality of websites you want to get a link from, because what we've been having recently, Ana made one link successfully on a website, and then Maria has one lined up, and another we are struggling to decide whether we want to link or not, because the reason for that is because most of the websites that are saying yes to us are pretty low quality, low stats websites.

 Maybe not necessarily low quality, but it's like 15 TR or 200.,So most important to us, I think above even like the quality, like how we would determine a yes versus a no should be based on the relevance. Does this page talk about what our page is talking about? It could be a brand new website. Site that has no traffic, but they're talking about the same thing that we are. We just want to be relevant for what our page is talking about. So that's number one. Obviously, we want high DA.

 We want a lot of stuff. But we want it clearly not to be spam. So we don't want a website about how to wash your dog linking to our page about opioid overdose. Uh, if, if like the sites somewhat relevant, like it's talking about like, say maybe not opioid overdose, but it's generally talking about addiction. Um, that's okay. But we don't want it to be like, uh, a blog about, about something totally unrelated.

 Uh, like, like what to buy your mom for mother's day.,So you want, relevance on an article level that's obvious, but you also insist on having a website relevance or is it okay if it's just like an actual relation between the two articles?,It's okay. I think if it's like a general website that talks about a lot of things, but they have this article that's relevant, I think that's fine. But yeah. We were looking at some of the links that did want money, and we're like, we wouldn't pay for this because it's just too far off. But if it's relevant and they ask for money, we should consider paying for those links.,OK.,Because we've got some that are in the medical niche. Now, they're not high-quality websites. And I know for a fact that they sell links to a lot of people because I've worked with them in the past and we got them through the outreach. So maybe we can consider those as well.,Those are in the medical niche and they have content that's relevant to us, but they're asking for money and they sell links to almost anyone in the niche. Yeah, I think what we should do is do our best to not pay for the the links and Like because what we're what we're working on And and you guys should should see this we're gonna start adding your guys's services to our offering and then Have our clients establish a budget now.

 We're gonna make them pay for any link that they get us but But obviously, if they start to pay us for the links, then we have money to get bonuses and do all of that kind of stuff. But I think you're going to find this is going to work really, really well. I'm going to take over just a little bit again, just because I want to show you a couple more things. Trevor, what's up? Example of a website that needs needs links right now Do more Yep, so these guys Resources here.

 We are so depression self-test BAM like this one. I guarantee you guys can get links for free I know because we've already done it before and gotten them links for free just using the resource page approach. Now, we did use Pitchbox to find those prospects. And so, if we find that we're struggling to get them, that with the built-in resource page template in Pitchbox, then Aleksandra maybe like next month or even like later into this month will start doing it.

 But yeah, just go to the resource page of any of our clients and look at the resources that they have. These are all tests. If you have questions like, hey, Trevor, where's the rest of the content that might work well? And all of these are actually good, too. There's a general depression page. It's going to be harder to get to this than one of those resources, but you'll still have some success in our experience in doing this.

 And you can even bring up in your pitch like, hey, we have this page about our depression programs. We've built some really cool info Graphics on the page. It's clinically reviewed by our Our clinical social worker Valerie. Here's a little bit about her blah blah And And Yeah, there's like so much if you start like making your pitch by looking at what it is that we're talking about out on the page, that you have so much more ammunition to make a more compelling pitch.

 Because you're saying, hey, not only do I want links, but I created this really great thing. And it gives people this test so that they can see whether or not they have general anxiety disorder. And I think you'll really like the content and thought it would be a great resource for your users. I noticed you guys have this page when I was doing research and that you linked to similar resources. I think ours would be a really good fit for your readers, whatever.

 And I think you're going to have tons and tons of success with that. Along the way, again, they ask for money. Let's just save all of those in the spreadsheets that you guys use. But I want you guys to spend all of your effort doing it this way. Pick a piece of content. And then make two side-by-side campaigns. The one that's built out of Pitchbox, the one that's built out of Ahrefs. Aleksandra, if you find that you're doing really good prospecting or somebody's doing really good prospecting, we're totally open to structuring things in a different way where one person spends all their time prospecting and then everybody else crafts the pitches.

 We're open to whatever's going to work the the best, but we know for a fact that this works because we did it in the past and it worked, and I know Addiction Center still does it to today. They're, again, not using Pitchbox. They're crafting every email separately, sending one at a time. They make a list of a couple hundred prospects by using Scrapebox, and then they go through the list, and they're like, okay, these 200 are our targets.

 And then they go one by one by one and they have tons and tons of success. So I think personalization is key. I think, you know, if we do this well and we find out, okay, maybe each person can only do three campaigns a month, whatever, all of that's fine. We just know that if we go this route, it'll work. So I know you guys are trying trying 10 different things. I just wanted to pare it back and have you guys just focus on one thing that we know works.

 And yeah, we're super happy with you guys. We thought, OK, if we call this call, you guys are going to be worried or something. So nothing to worry about. We're happy with where we're at, just trying to kind of direct things in one direction. That's really all I have. But I want to be a better resource for you guys to offer more help. I'm so freaking busy. I got a million things going on all the time.

 But this is really, really important to me, really important to Jordan and Trevor. So if you guys feel like you guys need a little bit of help on anything, I think you guys are probably better at this than I am, but I do have some experience doing exactly this in exactly this industry in the past that might be helpful. So I'm willing to drop what I'm doing and try and help you guys. But yeah, if anyone has any questions or wants to comment or anything, I'm all ears.

,I just want to confirm a few things with you. So basically we go with the resource page campaign, but you're fine even if we get a link from a blog, right? But our focus is music. Absolutely. Okay. And then in terms of the link quality, we only want to make sure it's relevant, so we don't care about anything else that's related to the website that's linking to us.,So traffic origin, traffic value, DR, TR, whatever, we don't care about that. Yeah, because our clients have no freaking clue other than domain authority. They understand that high domain authority means good. Low domain authority means not as good. But if we can show them a list of relevant links, they're going to be really happy either way. They don't really get it. And then we think if we're working on relevant content, that Google is going to reward us, because it's clearly not spam.

,OK.,And then when you said running two parallel campaigns through Pitchbox and Ahrefs. Are you referring to them being exactly the same? Because, I mean, what would be the point then?,I'm saying that I think you're going to have a lot of success with getting the links that addiction centers already gotten. So the point of running two parallel campaigns with a list of prospects that you got that already be linked to something similar from addiction center. I already know that they did outreach like we're talking about to get those links. Um, so I think like mostly it's just going to be like for the next month or so, let's see where we're having more success.

 Um, so build the one just like we did live, uh, on, on, uh, pitch box and then side by side. So thank like, okay, so it's January. So for this client in January, they get one campaign. I'm just saying make two separate campaigns that all target the exact same page. And you can use the same email and everything. The only thing that's different is that one you're prospecting inside a pitch box, the other one you're prospecting by getting a list in Ahrefs and let's run them side by side.

 If both work, then great. We'll just continue doing that. If one works way better than the other, then that's fine too. We'll nix one and go with the other. But yeah, what I'm asking you to do is just make two campaigns that are exactly the same, except for how the prospects are found.,Okay. And then the other question is, we have five clients with five targets. So we disregard the targets that we've been given and basically just focus on whatever we want, or should we focus on the targets that Trevor gave us to build links on?,Drop Trevor's targets. You guys identify what you think is going to perform best. And just by doing that, I think you're going to, like, yeah, pick the websites that Trevor gave you, but find specific pieces of content on their websites. And just know that next month we're going to have to do another one. So, so, uh, yeah, we're going page by page now. Um, no restrictions on revealing the client's identity.

 That doesn't matter to us. Um, cause cause basically what we want the person that we're outreach doing the outreach to, we want them to open that website. We want them to look at the content and be like, yes, this is a good fit for what I'm doing. Um, because if we don't do that, it will not work. I promise you that. Because, like, when we were doing this before, sometimes we'd get feedback, like, oh, yeah, this resource is great, or, yeah, we like it, but we don't do this kind of resource, you know, so they need to look at the,page. Determine if it's a fit. If the girls have any additional questions, they can step in, but thank you for the presentation. I think it's very useful to understand what you guys need, actually.,Ana. So I have one question. Is it okay to say that I wrote this resource, although I'm not the author of the resource, and I created this test, like you said earlier?,Absolutely. Yeah, yeah. You can say we created this, or my company or me personally, I don't care. Like, cause we did create it. WebSurf created that and we're all WebSurf. So, so yeah, say you can, you can cite anything that, that you want. And, and it's not even really like a lie. Cause we did create it. Okay. Thanks.,Awesome.,Oh, It helps the process. I can compile a list of what I think are good resource pages created on client websites that I think will be successful. So I can put together a sheet with some possible targets just so you don't go on a wild goose chase trying to find these things.,Whatever works for you guys. Whatever you prefer.,Trevor Gage make the list but but don't use that list to restrict you guys if you guys think you're gonna have success with something that's not on the list like give it a try because what we're gonna find is like some of these things are gonna be working really well and other topics just aren't as good because not as many people write about them whatever and You know eventually you're gonna have run nine nine things for this client and, you know, sometimes it works well, sometimes it doesn't, but you're gonna start to get an idea of like, hey, I know for sure that if we do a campaign around this topic, it's gonna work well.

 So like this client that's struggling, hey Trevor, can you guys make a piece that's similar to this other piece on this other website that already did well, and then we can collaborate and be like more effective. Um, and then as we get really good at this, um, I do kind of want. Somebody on the team to be like our test prospector. Um, so Aleksandra, that could be you, but like, I want to like, they're really, really hard, but like those.gov and.edu links, like, like we can come up with some tricks up our sleeve to try and win a couple of those and, uh, and create Bonus structures and all of that we just got to get to a baseline of like everybody agrees on what we're doing because based on what I've seen like Like I had Just a little bit of a different idea of how we would do it for this industry based on my experience And so I think I think we're on the right track Oh Jordan left, but I've got a meeting in two minutes, but I Some other things, just real quick, like HR type stuff.

 So you guys all have Jordan's direct information? Like jordanpol, jordan.webserve.io? Yeah? Oh, you're muted, Aleksandra. I just found out it's a different person an hour ago, so we'll make sure to reach out to her. Yeah, yeah, yeah, yeah. So, cool. Handles everything payment related. Regarding holidays, did you guys kind of get on the same page there? Just because we do things a little bit different, and we were willing to just give you guys a certain number.

 And you guys can pick which ones those are for, but we just want a list of which ones you guys select. And then, yeah, we should be really easy to work with. We're a really really happy to have you guys here and hope you guys are are kind of enjoying it I felt like since like we got started and holidays and Christmas time that we've been kind of absentee but we really really want to be involved and work together as like a team so sorry if it's felt like you guys are just kind of on your own and good luck out there thanks we appreciate that And yeah, we understand so oh good.

 Okay. Thanks so much guys.,Have a great day and Let's get let's get some links

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I get the list of clients who require monthly site maintenence?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: hi! Can I get the list of clients who require monthly site maintenence?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Acutally I'll ask Shannon, sry

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Seems like a lot of them are really behind? or am I misreading?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I see where you track website projects?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: looks like probably old from 2023

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is the "ongoing website projects" tab up to date or is that old?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: They are contractors though

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: For U.S. Classification Purposes:
1. The IRS and Department of Labor use several key factors to determine if someone is truly a contractor:
• Behavioral Control: The company shouldn't control:
    ◦ When and where they work
    ◦ What tools or equipment they use
    ◦ How they perform their work
• Financial Control:
    ◦ Contractors should have their own business expenses
    ◦ They can work for multiple clients
    ◦ They should invoice for work rather than receive regular wages
• Relationship Type:
    ◦ Work should be project-based rather than indefinite
    ◦ Contractors shouldn't receive employee benefits
    ◦ The relationship should be documented in a clear contract

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yes please! let's cancel whatever we don't need

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I spoke with Tracy about our finance visibility tracking and she said she's actually booked out until May this year but she recommended seeing if our CPA or our accountant could help with developing some of those visibility sheets. If they don't I actually have a guy that I think can help us

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I definitely think this is something we should take seriously going into 2025 cuz it's going to help us track and grow our revenues much better

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's setup a chat with them whenever you want

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Amazing

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm driving now if you want to talk on the phone

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yes happy to chat

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Heading into Costco in a few min

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's chat at 130 when I get home if that works for you

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok thanks for letting me know.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Jessi was up all freakin' night with the baby and had to get an hour of sleep this morning

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Happy Monday

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey Preston!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Bit of a late start this morning

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: How was your weekend?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's slay this week

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Get rid of digi

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm getting the ranklab deck hammered out at 11:30 with kevin and trevor

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Then we can start approaching some clients about the move to performance links

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey all! Forwarding a message from <@U083E324RCL|Julia Gumeniuk> here about needing a Prowly account. <@U025QMUHGTD|Preston Powell> can you share your thoughts on this?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Do any of these times (PST) work for you? If it's easier, you can click on a slot below to book: January 6 (Monday): • January 7 (Tuesday): • January 8 (Wednesday): • • January 9 (Thursday): • ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Are you ok if we not share that I'm expensive with the team? I just don't want to create any weird expectations with them. Just don't feel good about it personally. Hope that's ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah or that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We should dupe it into our own workspace

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You are awesome

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: No all good man, not a huge deal just wanted to mention it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: nbd

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I've just seen people get jealous in the past and create culture issues or they try to leverage it to get more pay etc.

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: PPC dept. is spending nearly $2,500/mo on fiverr to create landing pages and video ads.

I'd rather get away from fiverr and hire someone cheap to do LP's.

I can hire LP design/dev and also a video ad editor for cheaper than $2,500/mo to work for us full time. So we would get a lot more output for the same or less cost.

Can I do this?

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan & Mitch // Department Checklist Optimization
Meeting Participants:Jordan Dahlquist,Mitch Marowitz
Start Time: 2025-01-06T09:58:52-08:00
End Time: 2025-01-06T10:31:35-08:00
Transcript: Bye.,you you Thanks.,the the I was just saying something about it cuz you know, we're supposed to move away from me geek and I don't know why my my note takers not Trying to join my read note takers not trying to join,this meeting.,Oh, I Don't know did you check I was just looking at the settings it looks like Join all calendar events Sometimes it like if this call was created on a different email, it won't join.,Could this be on a different email? Mitch at web serve should be fine. Yeah, you can always do you see a little read.ai circle in the bottom right of your call?,No, because I don't have the extension probably I Don't have the extension either.,I don't know why You can invite Or just go to read and hit invite in the bottom left there add to a live meeting and Then paste the call URL then it'll join Yeah, I'm gonna want to fix that,but um it's weird because uh I thought that there didn't need to be a note taker to join. Only reason is I joined a meeting on Friday. And it got a summary and I don't remember the note taker trying to join. Yeah, you know, do you think it but but it's still joined the meeting. I guess maybe I did I just didn't notice, but perhaps there's an issue of me having both?,Like meet, geek, and read, you mean?,Yeah, I think that wouldn't make sense, but I mean.,You can have both.,It doesn't make a difference. I've had two at the same time before, and it never impacted it.,Yeah.,I don't know why it's not joining for you, though. Weird.,Maybe got to give it permissions again or something. Google calendars active connected.,I don't know.,Weird. Yeah. I'll try and figure it out. We can get started.,Cool. I'm trying to send this thing.,to.,you Okay.,All right, I'll do this after the call.,Let me respond here.,Uh, where are you?,Okay.,You can ignore all that. It's fine. All right. So let, yeah, let's look at our doc of our little Bullet point checklist that we had going here Here you go All right, so basically We have this call coming up on Wednesday with your team to go over all the new tools and processes to try to fix some of these just low-hanging issues. And a lot of this, I could have waited until the eight-week sprint that we're starting.

 But to me, this is just quick fixes that we can implement and just get it by the way. So I think it'll actually help you more with the eight-week sprint so that then you have more time and you're not still answering dumb questions all the time and stuff like that. So let's look through our list that we had. Process, role definition, quality control. So the issues we had overall was people not to the process, workload management, documentation problems, setup quality, communication flow.

 So communication flow, I think we've mostly fixed. But I wrote it out here, too. So we'll use Cloud as the first line of defense. And then if it's not in Cloud, then they go to you. And so we'll basically just explain that to the team. And then as far as setup quality, nuanced things, little things slipping through the cracks, that comes down to the process documentation stuff, which is going to take develop, I assume.

 So this could go into our knowledge base that I'm starting with Laurent on. And I have an hour call with him today that I'm going to be starting all this stuff. So hopefully, that will help us get a framework in place over the next month or two, where we could actually start to fix some of that process documentation. He's going to create a huge Notion space. And there's going to be dropdowns and segments and sections Yeah.

 And then as far as documentation problems, that's going to get fixed with that. So setup quality and documentation problems is going to take work from our end, but Laurent's going to help us build a framework for us to fill in, basically. So we're going to wait on that. As far as workload management, we're still trying to hire that obviously. And we are actually trying to tighten the belts on web serve in January and February because we hired me, we hired Chris, and then took on a ton of new stuff.

 We hired this whole digital PR and link building team in Serbia. And so we can't hire a ton right now, but I did manage to get permission Preston yesterday to hire that paid analyst the paid analyst role offshore So we can still keep going with that Which I'm already hiring for unworkable I've already got a job post out and I think we have let me check how many candidates we got Yeah, I have a hundred and six applicants already for that role.

 So Did you?,I have an idea in mind as far as additional recurring revenue on when we could hire. I know we're already looking for the director and that person. I believe we still want to take on like a few clients just to get the idea of the lay of the land and then hire the account manager. But I'm just curious what he has mentioned with you.,Yeah, I think as far as hiring that account manager, I don't think Preston wants to right now because of the cash flow, but it sounds like it's kind of mission critical and it's already been dog-eared for your team. So hopefully we can keep going with that and we're just going to keep going with it. And then a paid media analyst support role. They're only going to cost like 1500 bucks a month or something.

 So we're good on that as well. So between those two things, really think that we can free up workload on your team and hopefully improve quality, improve setup, even without documentation because they're spending more time on it, more focus on it, et cetera, hopefully. And then as far as process adherence, again, it's just there's so many different processes in different places. But we do need to crack down on this as time goes on and get more serious about it with the team.

 One of the initial processes that we're rolling out is the new type form design. And that is going to honestly help a ton, I think. It's not necessarily going to fix the fact that the design department is really slow right now and can't really do much, which is a bummer. But hopefully over the coming month or two, we can start to work some of that out. At least getting this process in place is at least going to get a lot of things fixed in terms of basic communication issues that we shouldn't be having.

 So as far as what we're going to go over with the team, we're going to go over the Clawed project.,the cloud project for the Why am I blanking the landing page already? And I did update. So it's good to go for the landing page.,Yeah, it's good to go.,And yeah, Keaton wasn't on the call, but everyone else was. And then. OK, cool. So you already had a Yeah, the videos, um, the knowledge database is updated to the point where, um, I actually deleted, um, or put a note within the document that there's another video that covered a similar thing and it was older. So we'll see how that works out. But I put all the links to the videos. Um, all the newer videos that I've made are in there.

 The older ones regarding the team meetings or not, but yeah, that's where we stand. Okay, sick. Maybe we could, oh, nevermind, it's fine.,Basically, we need to make sure the team understands that when they submit that type form, they've already done all the previous steps. So the Asana hopefully has it all bold pointed out, right? We're able to add all that into the new task template For doing the, no, it was not. I think you already had somewhat of a bullet point checklist, but it was like, Yes, I know what you're talking about.,That basically this. Oh, I'm not sharing my screen anymore. But yeah, we have that one. I didn't make a new one regarding the use of the zap or the type form, I mean, but, uh, okay. Yeah.,I just think, um, when we instruct the team on Wednesday, we need to tell them like, Hey, when you are building out your campaign, whenever you're going to submit to design, This is the link to the type form, so it's really clear. The old process is going away. This new process is coming in.,Here's exactly how you do it.,That would be the goal.,All right. And then.,Meeting agenda for client calls. This was something you said you want to implement, right, because the client calls are kind of just aimless, is that right?,Some people are definitely like Keaton does a great job with it. I think everyone does a fairly good job. I think we just had a concern about Fabi, really. Yeah. Having it more laid out, I guess, might probably help her. Yeah. I think that's good for everyone to do, even Keaton.,Even though he already has a pretty good framework, I think it's good to have a doc that you send the client before the call that they can review. So they're briefed on what the call is gonna be about. And then, yeah, I think that's a good way to do it. So if you send me just a few bullet points on what you want in that agenda, I can build out that doc for you and have it kind of like templatized for the team.

,Cool. I wrote one once upon a time and it's in the daily, Let me find, it's in the template. So, like it's in, when they're doing the weekly optimizations, that's when their mind's most on the account. So it is mentioned here to develop an agenda for the next meeting. And it has some notes. And then sort of the process of what they should be doing on the optimization. Perfect. Yeah. Send me that agenda details.

,So you can just Slack that to me. Uh, yeah, sure. And then I'll create a new template doc, and then you can plug that in there and just get rid of that and just say, Hey, fill out this agenda and send it to the client at least 30 minutes prior to every a client call, you know?,Yeah. Cool. Perfect. We'll get that done today or next day or two.,Yeah, there's also the meeting task.,I believe I just copied and pasted the same stuff. But anyways, yeah.,I also need the same thing for the associate But there's needs to be a little bit different. Do you already have anything for that? Or do you want me to just start from scratch?,If you want to start from scratch, that'd be great.,I don't have that equipment. And then is there anything off the top of your head that you for sure want to have in there?,In that agenda for the associate director calls? Nothing, I don't think you'd be able to pick up. So if you want to get started, we'll just review it, I suppose. All right, cool.,And then we have our one on one tomorrow. So we don't need to do much more on this call. I can probably let you go now. But yeah, as long as we can just get all this kind of buttoned up a little bit, maybe throw it in a nice document by Wednesday, which and help with, we should be good to go. And then we'll get the team updated on all this stuff, all in one big call.,Sounds good. We'll be sure to get that task built for the Typeform. Yeah. Sweet. That sounds good.,And check through the Typeform, too. And if you feel like there's anything missing, because I just built that. I just pulled those questions out of my head. Like there may be other things you need the design department to know or something, you know?,Definitely, especially with the flow that we have or we're trying to build with the Fiverr people. But yeah, I'll definitely take.,Yeah, that's a good question. Yeah. So the Fiverr people are doing ad designs or what are they doing?,All of it. Landing pages, ad designs, especially video, because our design team's particularly weak with video. But here's some processes that Sam mentioned that we're trying to follow. So I mean, this is just a start. It didn't exactly work out. Out like this for me with the ones I did. But there was a task that Shannon made and it's somewhere. So here's my question.,What are we spending per month on Fiverr work?,Great question. It's about like, I don't know, like 150 ish or so like a landing page. And then it's been building obviously there's not like a especially last because design team, um, they both, you know, two out of two people were taking vacation time. Um, but it's, it's been growing. Okay.,So like, can you go into fiber and show me like what the monthly total might be estimated? Cause the reason I'm asking is because we could potentially just hire some offshore guys for the same amount that could work for us full time. You know, if it's a, If it's the same amount or cheaper, then it would be better to just get someone working for us. Yeah, perhaps we're billing payments. And then do like December.

,Maybe just.,Total, but the PDF.,and throw it in Claude and say, what's the total?,Or GPT, whatever.,Should just be able to do that.,Yeah, that works too.,I can already see this is close to a full-time salary for a designer.,Oh, man. I forget, slash sum.,No, literally just select all of them, and it'll show on the bottom right.,Just select all of them? Yeah.,This is a weird doc, but yeah, I think probably what I need. Sum 2,142. Wow. We can hire a full-time dev and a full-time video editor to work for us at that rate.,Did you know that?,Probably so yeah, um, we got video editing and then so this is between video editing and yeah That's what I'm saying we could hire um We could hire one video editor and one web landing page designer for cheaper than what we're paying right now to fiverr So, what do you think about hiring?,someone.,Yeah, um, I also have a video editors, like, what were you paying for the videos there?,Let me see.,This one was 40 bucks. And then this one was like 60.,Can I see what they look like,,What the videos look like, One is? Oh, yeah, these were earlier in the Can you send me that spreadsheet also or the doc?,When you get a minute.,Oh, you keep your DMs really like at zero.,Yeah, I tried to. Nice. Here we go. Great, thanks. Might as well just send you the link. Can I get the, is the login for Fiverr in Blastconf?,Can I just go in myself too?,I think you need to log in through Google, but let's, get a password for it.,That'd be good. Then I can go back and just kind of see like some examples of what we're doing and that'll help me hire better.,Yeah. Settings.,Cool. Oh, shit.,I think we have two Fiverr accounts for some reason. I thought I did the wrong one.,Shoot. So here's the videos.,Let me share tab so you can hear it.,This is going out on meta or where do you put this kind of stuff?,This one I believe was meta.,Yep.,Got it. Yeah, we can make really, really dope ads like that. Like if we had the ability to make more videos like that, would you leverage it?,Absolutely. Yeah, I've been really wanting more video content for like a couple Cool, I got the idea. All right, cool.,Let me work on that. That's a cool find.,It'd be sick if I could find someone that does video and web landing. Let's talk about the landing page stuff. Like what are they doing?,Just creating a Figma landing page?,No, they're creating a Elementor. So they're actually developing it then? Yeah.,And then who's designing the layout? Who's doing UX? Us, basically. I mean, the UX, that's kind of the Fiverr person. So like, the The project for the landing page, it's very templated. It doesn't really allow too much outside of what it is, which is both a good thing and a bad thing. It kind of keeps all the similar, but I think it could also be a negative because it could potentially reduce the creativity of our landing page.

 And that was one thing we tried to improve sometime last year, fairly early on, where design team would create two different Figma files, and then we'd choose the best of the Figma files, and then they would build the landing page. I can't remember the last time we've done that. It's been months, so at some point it just back to what we had because they're busy and it was, you know, we had three designers and we got rid of one.

 What does it cost to create those on average?,Like the whole thing, designing it and dubbing it.,It's the same price. You know, we've just given them one task. No, I didn't hear the price how much oh, they're like 150 ish for lightning page. Um, This one was three because we tried it But yeah, can I see? Oh, yeah. Sorry. I'm not sure Um Yeah, this one we So yeah, it was like 150, 160.,Can I see what it looks like,,Is that possible? Yeah.,Trying to figure out how complex these are.,Yeah.,Is there a reason we don't just do the exact same template every time and just change out the colors and fonts?,Because we don't want it to be like, we're in the same industry bidding on the same keywords. We don't want it to be exactly the same. I mean, it's similar enough to already have a concern itself. Here's one, gosh. Just any example is fine too.,It doesn't have to be like, not one from Fiverr.,It looks like they moved it. Okay, let me see. Grada was one that I liked, which is actually a little bit outside VOB. Sort of, she asked for this one. There we go. So they look nice, but they're pretty basic.,Yeah.,Looks nice. Yeah.,I got you. Cool.,So we need a landing page design and dev, and then some video support.,OK. I'm on it.,Yeah, the video support would provide additional capabilities that we haven't really been able to do. And then, yeah, the landing page, dev, whatever. Yeah, it's additional support. So, okay, cool.,Let me work on this, man. And I'll get back to you.,Cool beans.,Anything else you want to go over?,Um, don't think so. I'll just try and get that task done. And then continue building out the knowledge database like it happened. So, okay, sick.,All right. Sounds good, Mitch. Have a good day, man.,Appreciate it. See ya.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Preston signed off

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: will keep you posted

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm going to hire a ft lp dev and video editor

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: every detail you can send will help

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I will need to know all that so I can make a strong hire

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you gpt a quick description of the role ?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sam struggles to follow thru i've noticed :face_with_monocle:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Usually have to send to a large list to get responses since a lot go to spam or they wont' do it etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I noticed you sent out one challenge, did you mean to only send to one person? Or to all?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just sent a google call invite

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: about ranklab deck design copy direction

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U025QMUHGTD|Preston Powell> when you are done with your call can you join this one with trevor and kevin and I? We have questions

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's reschedule

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: we just left

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It's a big move so I wnat to iron out the details together

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: nevermind, let's reschedule that so we can discuss with you

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's get meetgeek canceled also since we don't need anymore

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I sent an invite for wed

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I didn't thinkwe would need you but turns out we do

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I know

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan, Trevor, Kevin
Meeting Participants:Jordan Dahlquist,Kevin Hall,Preston Powell,Trevor Gage
Start Time: 2025-01-06T11:32:57-08:00
End Time: 2025-01-06T11:44:07-08:00
Transcript: Let me bring it up. The main things are, let's see here. OK, so yeah, like basically a lot of the messaging just isn't accurate. This is all just kind of like filler stuff. So what we need to figure out is how we want to relay better messaging about this new program. So the benefits, uh, why the old systems outmoded that could be like the first slide, the challenge slide number two. And then from there, moving into the third slide, slide three, we could do the solution, which is this new system we're implementing slide four could be.

 Maybe like slightly more detail on how we actually do the new system. I'm just spitballing here. Do you have any thoughts?,I'm more concerned with just getting the pricing. Yeah, pricing down properly. So I think the final slide seven we could get rid of Six, I just want to make sure that this is OK with Preston.,I think he did want to bring the pricing down, but I don't know, like, to what.,I don't really have any information on it. Yeah, I adjusted them, but I don't know if it's exactly what he had in mind. Okay. In terms of the messaging and stuff, I can knock that out.,And then just need Kevin to help us make it look okay. Yeah. Yep.,And I also wasn't super sure if everyone's switching over to the banking model of linking, or if people who were doing guest posts and no PR outreach, if we want to get them on this banking model or just have it be on the blanket kind of service model.,Well, is there a reason we wouldn't move them over?,I was concerned that the that what if they can't deliver? Yeah, so if we the average link we get is worth 300 bucks the average amount we get is for our four per month so that's 1,200 bucks in the past people have paid 3k for PR outreach so that would kind of diminish that but we can switch over but we would just have to pad out their scope of work which we could also include in this. Just to kind of segue that.

 But if somebody's used to getting whatever it is for DA40 guest posts, and they're only paying $6,500, if we take that down to, I guess we wouldn't take it down is what Preston would say. But they still pay 6k and then they have like you know a bank of 2,000 when they pay per piece with guest posts I just don't want to see our 6k clients turn into like a 4k or something if,we can't yeah those just cause red flags for Preston and yeah I think am I totally off here but in the beginning he was saying we keep the plan but then they add a budget for links. In other words, there's no links or guest posts or anything included in their current plan and then they are going to add on the performance-based escrow account.,That might be a harder sell then.,Yeah, well is that what he's Was I off on that like maybe I misheard I don't know I wonder if we can get him in here Let's see what he's doing Doesn't look like he's on a call or like, you know, I Know this is what Kevin's on He's on with Kevin. So maybe when Kevin gets here we could get Preston to Okay.,I'll send him the link to this call.,Yeah, I feel like we're trying to do something that Preston has the keys to right now. Yeah.,Okay, so I'm just reviewing my notes from our calls. One of them was, excuse me, focus on high quality campaign per month per client instead of multiple smaller campaigns.,So this is for the link outreach team?,Yeah.,So that's for link outreach. Target 80 to 200 highly relevant outreach targets per campaign. So that wouldn't be related to this. Yeah. Okay. I'm trying to find my PR. Move to pay for performance model for links set tier price based on link quality. Clients will have an escrow budget suggested price ranges DA 30 plus links 300 a month. So this is separate though. This We're talking about VR here.,I'm working here. So I've only got until noon here. I do want to reschedule this one. Yeah, I think we're going to have to. All right, apologies. Hey. What up? I got endless meetings back to back today.,I think we need to reschedule this one, because neither Trevor or I have very much time left. And we're actually realizing we need more input from Preston on this. That's fine. Yeah, I got a meeting at 12 too, so. Yeah, I think we're going to just let you go, and we'll reconvene.,Sounds good. All right, thanks, guys. Thank you.,Thanks.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: no

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: idk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: meetgeek?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: or I need to send invites?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Are they struggling to get setup?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You can add me if youw ant

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So I didn't see it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm not in that channel

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: oh strange

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: kk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: to keep track

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok gotcha you may want to move them to the challenge sent tab then

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: a lot of workable emails go to spam so sometimes sending a personal email helps

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah if you only send to a few they may not get it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: or message question here

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: On call til 1ish but if it ends sooner i'll ping you

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: today is just a kickoff and then we can work on the tasks this week

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: you mean like if the renewal amount is higher than previous year?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: No need to do anything

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Are we counting renewals as upsells for the NRR

If renewed at a higher rate

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: let me get back to you in a few after this call

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: so if 5k renews at 7k we count 2k

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ok almost done with call and will review

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is this using formulas at all or jus tnumbers plugged in?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So the numbers aren't lining up because QB isn't showing correctly?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: No it should be a dollar amount

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What NRR Is:
• A measure of how well departments retain and grow their existing client revenue
• Does NOT include new sales from outside - only measures what happens with existing clients
• Goal is 94% NRR (meaning maintaining 94% of last month's revenue)
How It's Calculated: Starting Revenue (Last Month)
• Client Churn (Lost Revenue)
• Cross-sells (Revenue from selling additional services to existing clients)
• Upsells (Revenue from increasing existing service costs)
• Variable Revenue (Ad spend or future performance-based link payments) = NRR
For example:
• If your revenue was $500K last month
• You lose $30K in client churn
• But gain $20K in cross-sells
• Your NRR would be -$10K
Key Points:
• The goal is to get NRR to zero or positive
• Department heads are responsible for replacing lost revenue through cross-sells/upsells
• This shifts responsibility from sales team to service teams
• Each department (SEO, Paid Media, etc.) has their own NRR target
• Will be tracked monthly and used for quarterly bonuses
• Seth will verify all numbers monthly to ensure accuracy
• Department heads should update wins/losses in the tracker as they happen

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Here's a claude outline I prompted maybe helps?

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan Dahlquist <> Laurent
Meeting Participants:Jordan Dahlquist,Laurent Matson,Preston Powell
Start Time: 2025-01-06T12:01:01-08:00
End Time: 2025-01-06T13:01:33-08:00
Transcript: Snow's cool. I like visiting the snow. Yeah, I know.,It's fun to ski. Otherwise, it's just kind of like, what am I doing with my life? It's scraping ice off the car for no reason.,Yeah, totally. I love snow sports.,I just don't like living in snow sports. Yeah. Base of the mountain or bust, right?,Yeah, totally, man.,Well, how's your day going so far?,It's been really busy, just back to backs all morning. And fortunately, my next one isn't until three. So I got a little bit of time now.,But yeah, totally.,But yeah, let's dive in, man.,All right.,Yep. Cool.,Got a few things to go through here and help us Let's figure out what the initiative will look like here. Let me bring it up.,And do you go by Jordan or JD? Normally Jordan, but at web serve JD because there's another Jordan that pre presumed me.,So I'm now JD. I'm good either way. It doesn't matter to me. Okay.,All right.,So you have a couple of things to walk through today and just get us on the same page with the initiative. Done some prep, have a few things to share, and I think it'll all come together. So yeah, I wanted to start off with just like a kind of like a focus point here, because I think a good goal here would be to kind of seamlessly bring together like the strategy sprint that you shared with me, and then the work that we're doing together.

 And there is like a lot of overlap between them, which is nice. I will say, and I kind of mentioned this in the email, like I've done a lot of these Types of um sprints with directors as well like where they have things to do in their department and I'm like In that like role to help them through it like I manage the directors at one point at directive and like Garrett loves these types of Exercises so we did this a couple times.

 Yeah, and they can be hard like it's a lot of There's a lot.,I know it's I know it's gonna be really hard and I know I said I basically set a high bar just hoping we can and get something valuable. And I don't expect to get everything that's in this document out of it. You know, that's kind of my, so.,Yeah, and I guess my point being, you know, with me in the fold now, I think we, you're giving them a lot of support, right? Like we'll be able to do a lot of builds. I think this is, it is best when it's more about like kind of extracting points of view for them and like collaborating with them versus like they're on the hook to like develop things. I think we'll kind of be on that path, which is good.

 Totally. Yeah. This, I'm trying to think what else I was going to say there. The other part of this is like, there's a world where we already kind of know what we need to do and that's why you brought me on. So like a lot of this is, and it's harder when we already know those things where let's say we're at like 50% where we want to And it's like, hey guys, what do you think we should do? And everything's just so open-ended.

 There's also a version of this where it's like, look, we kind of know what we need to do to get to 90%. And I think you and I will work to get there, do like the product work and what we do in sales and how we look ahead to process. And for them, it's going to be kind of like, all right, how do we end up optimizing that final 10% if that makes sense? It's kind of where we want to get to versus being like so open-ended.

 So one thought I did have, on this sprint is if we could just change one of the modules in terms of the timing, that would be core opportunities. Cause I think we have a really good flow from like, let's like, this is basically discovery week, right? They're kind of doing their own discovery. I'm doing discovery. And then it'd be good to get into the service offering review. And I think that's going to do a couple things.

 One, that's going to, let me get in there, get the right data that then I can keep developing after they've moved into another week. So we kind of have that like handoff there. Also, I think core opportunities makes a lot of sense coming after at least these next two, because they're going to have a lot more like data and questions figured out. I like that.,Let's do it. All right, cool.,And then it kind of bookends a little bit where like the first ones like review and analysis, which is a little bit assumptive, like, all right, what do we think's going on? Like, what are our goals?,And then we can get into the work and be like, all right. My thought on doing, um, go up one. What was that called?,Oh yeah.,My thought on core opportunities was basically figure out what the issue, what the opportunities are and then craft our services around those opportunities. But you're, you're suggesting it's better to do it the opposite way because of what, just so I understand.,Well, we're kind of doing that a little bit up here already in a SWOT, figuring out like what's happening. If we can do that there, that would be good too, like kind of calling out the opportunities. So there might just be a version of it where it's like kind of kickoff, like what do we think our SWOT is right now? And then we go through some of the work of like, let's look at the service offering, sales strategy that incorporates our ICP and things like that.

 And then kind of arrive back at core opportunities, be like, all right, based off all that, what do we think our biggest strategic opportunities are? A 2020, 25 vision statement. And then that kind of goes into like some maybe KPI development or whatever. So it doesn't really, or it can go before here. I don't know. Yeah, no, that sounds good.,I, I definitely expect this thing to shift a bit as we go to, I have a feeling some of these weeks are probably going to end up being way more work than any thought in the extra week. And like, yeah, this whole thing can definitely flex however we need.,Cool. Yeah. And yeah, so let's go through it. So this is our work in progress document. You'll have access to this. We'll review it together. We can kind of keep building on this, but it's a good start for us. And yeah, we covered initiative there. Feel good about that. Meeting cadence. When do you want to meet on this, Jordan, on a weekly basis? And if Mondays are particularly busy for you, I'm happy to move it to Tuesdays.

 I will say we'll talk about when we want to meet with directors, maybe, and if we want to do that over the next couple weeks. I don't know if you and I want to meet maybe on Tuesday, and then we have a director meeting later in the week. So we can talk about that.,Yeah. Well, I meet with the whole team to go over eight weeks sprint review every week at 3 p.m. On Monday. OK, so it may be good to touch base with you before that time just to make sure. I am set up for that call. OK, or we meet on like Thursdays or Fridays, and then I'm prepared for the Monday call, which could be better, too. It's up to you. Right. Yeah, that could be better. Like right now, my Thursday is completely wide open.

,So I figured I'd jump in with you guys. Nice. I had some open time that was booked earlier. So I don't know what's eating went away.,But welcome in. We're hitting the ground running here. I'm going over.,Yeah, I would say. Like anytime Thursday or Friday mornings after 9 a.m. Are typical. Except for this Friday doesn't work, but normally it would.,Okay. Yep.,Yeah, that could work well. Yeah, we can come back to that as we kind of see everything crystallize here. So yeah, what I was explaining Preston here is we're looking through and I think there's a pretty clear like intersection here between the work we're doing In the eight week strategy sprint, which is great Um, I think as part of it like i've done a lot of this with directors. So I think we'll definitely be able to support them through this and probably As an output of this it's we want actual like tangible Outcomes and systems developed and I think that's that'll kind of add this to the to the approach Um, whereas other times with initiatives like this, sometimes you just end up with a lot of word docs And like people have like worked on stuff and you're like, all right what now?

 Like what happens. But I think we can actually like kind of pave the road as we go through and kind of set them up. Yeah, I love it. I feel like it's perfect timing, pulling everything up. Perfect. So Discover.,Hey, sorry to interrupt my first call with them today at three. So this is great timing. And if there's anything you want me to share or update or include about the doc, I can discuss that with them today to kick off call.,Perfect.,Yeah, so week one, the sprint is really that discovery element. So for the team, they're doing the review and SWOT analysis. That makes sense to me. They're going through that. I know you have the template with it. So they're looking at some of these things. I think that's great. I like the idea, as we just talked about, as it's a little bit like, let's start with a hypothesis. What do we think right now is our strengths, weaknesses, opportunities, threats, let's put that down.

 And then let's like, let's do the work and work through our process end to end, going through product, sales, and service, one by one, actually figure out what those are before we arrive at like, cementing our core opportunities for 2025.,At the end, right, so you're saying do make week one more of a shoot from the hip, and in the week two and three, we're actually going through in more depth, is what you're saying?,A little bit. And it's kind of baked in here a little bit already. Like, obviously, there's a little bit more, you know, we're actually getting like, get the forecast in there. So I think it obviously should be based in data to the degree that it can early on. So that's fine. This totally makes sense to me. Now, On my side, on the discovery side, what we had talked about is people, product, process, clients.

 So just getting as much data or assets as we can around there to help influence that discovery process. So people, let's talk about that in a second, like where and if, how I meet with people and what that looks like, For product, process, and clients, what I mean by that is if we jump over to the assets, that we're going to have here. We'll start storing everything in here just so we're aggregating everything in one area where we can look at it.

 So at the starting point this week, it would be great to get things filled out in the current column, which is things that we may have now or may not have, which is fine. Like for instance, we just saw that SEO proposal that can be dropped in here as a link. Do we have an SEO C-O-S-O-W, anything like that. If you want to add things in each of these categories, like product and R&D, sales, marketing, ongoing, feel free.

 But we're just kind of, we're beginning to color in the canvas of web serve here with the assets that we have on hand. Yeah. So yeah. And that's in any problem system. Yeah, that's great.,I can start working on getting this filled out this week.,Cool.,And then as we go, we're going to have this other kind of like, we'll see to what degree we have the bandwidth for Jordan. Um, but we, we can also be kind of looking ahead here to things that we know we're going to want to develop, like the processes and stuff. So as we do that, we might be like, look, we don't have an onboarding sheet. I'll be like, sweet. Here's what one can look like, We can get a head start on that and start developing that to get that in there.

 And like, we can start kind of thinking, um, with the end in mind and start working on some of those things.,That sounds great.,Love it. So yeah, so we'll discover a week. I think a good outcome of this week would be to get this peppered in as much as possible with what we have. Now on clients, I'm also going to like be doing my own kind of questions that I would like addressed per stage here. And again, I've aligned it with the sprint stage. But the big one for me is as ICP and personas in this first week. And I know we have that, it looks like it's a little bit integrated in the other phases, but I think this is one of those moments where it's like less a question for directors, like, hey, who do you think your ICP is?

 Or like, hey, what, you know, I think these are things that, you know, we can just develop on our own or identify who the best person to help us develop it is. It's usually a mix of like sales and marketing in those teams. For instance, I just want to show you like what I mean by that. So I have a, and again, here's like, this is a web serve IPC sheet.,So I can come in here, come into our app. Can you send that ICP we have?,I think you had one set up for the LinkedIn ads and stuff, right?,I think.,I mean, kind of, we have an ICP. They're not really personas, they're more like job functions and titles. And then there's an analysis. It all might be interesting to see. And I can just send that, but it's from directive. Let's see, when they send us here.,Yeah, while you're getting all the directive assets, I feel like I should put a wishlist in to you.,documents.,I was like, Oh, I have this thing. And I went to look for it. I'm like, I don't have that right now.,That's locked in a G drive somewhere. Yeah, for sure. Well, maybe I can maybe I can help send you that wish list.,So yeah, what that can look like top level, you know, firmer graphics would be great. So I think about an ICP firmographics, buyer personas is like the traits of an actual buyer within that. So it's nice to get that outlined, of course. Now, the way I typically do this, and this might be a question for the marketing team, but if you go to the CRM, you get the customer list export, right? You probably do this for performance marketing for your clients to a certain degree.

 It's good to end up with something like this, where you enrich it to the degree that you can, but you get a sense of like, all right, job title, the deal value per company, company website, of course, and then additional firmographics like verticals and industry. These are examples right now, or these are actual exports.,That would be great.,But it's an example sheet. Yeah.,So I've got this for you if you if you want to look at it. Okay. I just shared it with you. But It's just these slides. I think that he's referring to so Clients within these different revenue ranges that we got actual data from our CRM Their estimated marketing budget wasn't that good of an indicator because we're dealing with a lot of small businesses Number of employees was a little bit better and then Location most of our clients are in, California but that's changing and shouldn't be used as an indicator because we're trying to not have that be the case.

 Number of locations was really good. And then our contact, this will give you some insights into job titles or job functions and then seniority levels. And I shared that with you guys. So you guys have but that's, I think what you meant. Yeah, that is what I meant, yeah.,That's perfect.,That's part of the way, yeah.,Yeah, no, that looked like a lot of it. Now, at a top level there, like from a vertical perspective, what do we have there for like, I know we have treatment centers, is it only treatment centers or are there other subsets?,There's, so we've had some success medical device. But yeah, we want to build our offering for behavioral health care treatment that are funded by commercial insurance, because that's kind of where our sweet spot is. My, my partner, Kyle, he's got a medical billing company, and we're able to get some data for him, or from him. We were thinking about like the work that directed did for us to build that deck that I just showed you incorporating that into our paid media approach in a different way because we're able to pour through clients billing data and then I'd like to make something similar like just like hey here's your best paying clients you've ever had and here's how we're going to incorporate that into our marketing strategy and two it would figure gives us a, you know, we've been building software that tries to tell people what they're going to get paid before they accept the client.

 And it's, it's technical, but, but it's very similar, right? Like we'd export a big list, and then we'd, we'd make sense of the data that came out through pivots and different things. And then that deliverable, you know, already we talk about an insurance policy deep dive, but it's just kind of like, it's kind of bullshit. Like it shouldn't be, because we have the capability to do it and we just don't have a deliverable.

 And it would just add a lot of value because when Directive did this for us, we're like, oh my gosh, this is so great. The wheels started spinning. It's like, Hey, we could do this. And we actually use, we use primer for our clients to make these audiences, uh, on, on meta so that we can go after people that work for companies with insurance policies that reimburse, uh, like 40% or more of the bill charge.

 Cause it's, it's like kind of wild dealing with insurance and it's very It sucks. But if we could pull that data really quick, then we can say, Hey, like, here's where your clients have come from And we can incorporate that because we're really good at one thing, which is like these out of network rehabs, they charge a lot of money, finding their patient is really hard, they're willing to pay 20 grand to get a good patient in because it'll for some 100K or more.

 But it's like fighting a needle in a haystack. But then once we get out of California and we're in the Midwest and they're doing these small campaigns that are very local, we run into, hey, our fly people out from the East Coast scenario isn't really working because X, Y, and Z. But if we had collected more insight in the beginning on what has worked for them in the past, it would have informed our marketing strategy.

 Yeah. So anyways, sorry. That's a lot of context for.,That's good. Yeah. So like a persona ICP development type service piece, which it can be, I mean, it's massively valuable. Usually sits by itself as like in the strategy department. It's a, you know, it's a, it's either a pretty big add on or enhances the overall value of like the strategy phase.,Right. So that's great. And then, you know, another added benefit is we get insights into their, their billing data, which makes our, our software product stronger because that's what powers the whole thing. And then we have a revenue cycle management company, basically a billing company. And if we look in there and it's all messed up, we can potentially identify, hey, this person needs to be approached because our marketing isn't going to work that well because they're not collecting what they should be anyways.

 And now I can pitch them on billing. And, uh, I'll get a, you know, 6% commission on every dollar they make next year. Right.,Yeah.,And at the proprietary data part of that is so valuable, right? Like that you couldn't like have the benchmarks in the industry kind of like have, have like be able to open the black box for them a little bit and like have that because you're actually connected to all your clients data and you're aggregating it and anonymizing it and offering it to them.,I said black box because This is our product offering that's going live black book There we go. Yep, and Just just very specific to the industry and We have like our first beta users on it right now and tons of interest so could turn it into something big Yeah.,Well, absolutely. Good. Nice. What is that? Vertical or horizontal integration? Some kind of integration is going on.,I think it's vertical integration.,That's good. That was one of the first things I did at Directive, actually, was create the benchmarks library they have, which is once we connected it all via funnel.io and everything, we just had all that data. So understanding performance data in tech and SaaS has always been a little bit confusing. Now that it's all like, I mean, it's mostly in spreadsheets still. I think it needs to be converted to a platform like that, but, um, hugely valuable for, for setting an SMS and in forecasting performance.

,Um, okay. Well, two, two pieces here. So I don't want to send you on a, on like a two aspirational of a hunt. Cause like, this would be like really nice to get into our product. Um, but I think maybe that's. More part of an ongoing, because I don't, I don't know if we're capable of doing all of that in house. And as of today, until we get like a data analyst full time on our team, and we can't probably afford that today.

 Yeah, so I don't want to send you on a wild goose chase and all these great things to our services that we can't deliver on but I also want to kind of be aware of that being something that I want to add because I think it would really really differentiate us like a hundred percent if we were like okay we're in our initial project phase and we're like let's get access to your billing data so that we can see what your best clients look like, they'd be like, oh my God, no one's ever asked me this before.

 And like, they'd really feel like it was different.,Yeah. Yep. A hundred percent. Yeah. Yeah. I recently developed like an AI type approach for that. That's still takes me way too long, but it's like really powerful. Like in terms of persona development and being able to create like an enriched list like this all the way through and just using a lot of different data sources to, um, and basically like fully loading, like a custom GPT or a custom gem.

 If you're using Gemini with like all these data sources and then you can extrapolate so much stuff from that, like our jobs we've done or content jobs we've done or add copy or write Mike. So once you have that fully loaded, like imagine if we had that for web serve, right? Like your persona per client's fully loaded in a custom gem. And now you can tap it whenever you need to within the project to create all kinds of cool assets or creative or anything.

 So there are cool things we can do there. Anyway, so coming back to this, yeah, we'll get what we have there from a current perspective into the sheet. That'd be great. And then looking ahead to next week, a lot of discovery this week for both myself and the team. Next week, if we move that ahead, Jordan, when we're looking at service review. Similarly, I have questions on that too, in terms of like the way that I would work with a director on this to help understand and kind of extract their point of view and their positioning and give it a construct.

 And so I've taken that and already developed like what that outline would look like for that productization piece. So for paid media, we would start with like, all right, what are our main categories? What's the summary for each one? And we're just getting all of that kind of down to understand like where we currently operate and the way we think about our unique groupings. And then to Preston's point, there might be a couple like aspirational ones that we can highlight.

 Be like, we don't do this now, but maybe we want this on the roadmap in the next like to six months. And we can put that in the spreadsheet too. And so the way I'd recommend going through this is like, I could give you a brief for the team, or I mean, we're kind of talking about it right now. And you have these docs, and I can kind of cover that with you before your meeting later today. So the team kind of has that they're already doing their homework this week, for week one, and then for week two, it'd be great to meet with them.

 And then if they've thought about this a little but already, and then we can go through it together. I'd say that'd be probably a more productive approach than letting them kind of do it on their own, if that works. So I'd be happy to meet, especially it's just two directors, right?,Director of pay, director of SEO.,There is a third, but yeah, the third doesn't have a lot going on right now. Okay. Yeah. Yeah. We have a, basically we have this web design team that, um, doesn't really make us any money. Uh, And it's just kind of sitting there and we want to obviously change that but it's just two people and they just crank out websites and yeah, and hopefully they make Enough money not not to be a loss. We're just kind of breaking even there This year we want to add kind of a performance design aspect is what directive calls it, but we're gonna call it something different but just a CRO kind of Add-on to our paid media services and that's how we think we can get good recurring revenue because right now they're just project revenue and We kind of have to have it because we deal with some smaller companies that that need a website that are just starting up and If we can't build them the website, they're gonna give the other company that can their SEO and paid media.

 Yeah, so they're important for us. But then, currently, the goal has been just to break even or make a little bit of money and not much time, effort or energy has been put into them yet. So yeah, I guess just be aware that Jordan's working to roll out kind of a CRO type service on the side over the coming months.,Yeah. Well, I'm well versed in that. So if you want me to include like, uh, creative time CRO in the aid media offering, I can do that initially. So you get a sense of what that looks like, because that's how I've always pitched creative successfully is by aligning it with a performance and with CRO. Um, it's, it's yeah. I have so many slides on that. I can't even tell you. So I think we'll, we'll be good there.

,So let's, let's. Let's do that, but yeah, let's just kind of touch on it so that Jordan has a little bit of help and Expertise from you. I mean, we've got we've got some expertise there already Just just haven't Gone through anything, but I think you'll be super helpful.,But yeah, it doesn't need to be a big focus Yeah, I mean it was like a director a hard time selling it to you know, it's like an extra 5k a month and they're like What do I need for this? And then you just tie it into CRO. And you're like, look, you're at 1% conversion rate right now. Maybe you can take it from click-through rate all the way to conversion rate on the landing page. You're like, what if we just got this to 2% over the next three to six months?

 You plug that into a mini financial calculator model. And you're like, look, based off your conversions and your AOV, whatever it may be for health care, you just quadrupled your pipeline. So you're asking me why we should do 25K over the next And I'm telling you, you're going to make 100K if we do this, right? So CRO and design effectively becomes free in that instance. So that was like the case we made and how we, that became a core upsell for us or cross-sell rather.

 And I think we could easily do the same here. So anyway, so yeah, we have, yeah, so what would be great is to kind of give them a little bit of a brief and then meet with them next week, Jordan, to go over this together. What we go over basically for the service side would be, is this our paid media line up? Is this everything we do? We want to get everything in there captured and organized the right way, the way we think about it.

 Are these the right categories? Does everything make sense? Eventually, what we're going to end up doing, if we come over here, is we're going to want to align our assets are deliverables with each one. Not everyone will have one because some will be more like, some will be more of a client deliverable, like a deck or a spreadsheet, whatever. Some will be more of like that in-platform piece we spoke about, in which case eventually we're going to want like a training link to it, right?

 Whether that's a Word doc or a video, whatever. And then finally we'll want to do something that I kind of do all the time now, which is, is there like an AI slash automation layer to this task. So something key for us, it's like, all right, is there is no one, everyone is on a different curve when it comes to AI. And usually, there's someone either I'm calling out to someone calling.,Yeah, how do we break this out a little bit more? Because there's a lot of other stuff underneath each category. Like, so if a paid media campaign. I see you have paid me to strategy. I'm trying to see your screen. Sorry, but it's like really small in the corner. For some reason, it's not giving me my full view. Okay, so you have announced the strategy execution. I got it now. I love this.,Okay, cool.,Yeah, I mean, if the starting place like ours might be a little bit different, but it's usually probably captures most of our main, you know, buckets. But we can we can we can make it we want to make it actual. So we'll go through that. Similarly with SEO, we'll go through those two and just make sure that it's everything that we do. Ultimately, like this informs a slide, right? Imagine the slide where it's like, this is what you get.

 Like when you think SEO, this is how we think about it, right? You kind of get that sense of like overwhelm, like, holy crap, they do a lot of stuff. You can break it up like that. Another key question would be like, our tech stack. People tend to under promote their tech stack. So we have a few different platforms here. We'll bring those together in a slide that's really attractive and talk about how we leverage that for their goals.

 So we've got all that mapped in there. Then we'll go into positioning, have a bit of a framework for that. And this is just to stoke the main building blocks of what makes a good message or a good position. We should do this per department. So we have a little bit of that in there already in that proposal, but We can start a little bit fresh be like look what's happening? Like what's happening in healthcare right now when it comes to like, Discoverability for SEO right like are they discoverable or they not like how's the algorithm?

 Whatever it may be. Yeah, what's the big opportunity?,What's the this is overarching or this is just for pain?,This is just paid, that's a great question. So on that, the paid one's kind of like a mini. I do want for web serve at large, and I wanted to get your thoughts on this. I feel like it's worth just mapping this out here, because I don't know where we're at with this right now. Who would be the best person? It might be you too, but to help kind of like map that narrative.,It's a good question, but I think Preston would definitely need to be involved in that because he knows.,Can you repeat, sorry, I'm going back and forth with three people on Slack and I was just kind of an observer here. So I wasn't following the last five minutes or so.,No worries. Yeah. So we have a positioning framework here. It's basically a strategic narrative that just is kind of a tried and true narrative where we like state the market change. This is how the world is shifting. Like maybe in healthcare and healthcare marketing, you know, and it's happening with or without web serve, right? This is just what's happening.,And as a result, this is the opportunity. Yeah, I know those conversations that operators are having and absolutely can, you know, their reality is insurance companies are paying less and less money for their services year over year. And it's getting harder and harder to operate due to that.,Yep.,So I think it would be good to have that locked in here. It's not usually a lot of information in here, but we want enough. I don't know if I have an example for maybe, I did one of these with index. Let's see, maybe messaging. I don't think I have one them. I do have an example of that one. I think getting this mapped out at like an agency level would be useful for us in because we're going to be doing this for the department in more of a smaller way with this understanding like this is how we arrive at the methodology like all right for for paid media at web serve what's the old way of doing paid media what's the new way you know let's come up with five principles there.

 Let's understand like what we measure, you know, our proof points, things like that. If they're developing this, but they can do it with our agency umbrella messaging to help kind of steer them in the right direction, I think that would be useful.,Okay. I can definitely help with that. Yeah. Are we trying to do it right now?,No I mean, um Yeah, we'll probably work on this with them. I'm guessing the middle of next week Um, yeah, so we could have any of this For that, that'd be great You probably know it off the top of your head Yeah, I I know at least like a base that,you can build off of in my head.,Yep. Cool. Is it freezing cold?,Man, it was dumping today.,It was snowing all morning. Yeah, it was pretty. I hadn't seen in a while. I was like, that's nice.,I forgot exactly where you are.,Chicago?,I'm in Connecticut. Connecticut. Oh yeah, nice. Beautiful Connecticut.,Cold Etiquette.,Cold Etiquette.,Yeah, we're just kind of between New York and Boston here and everyone kind of skips over us. But, you know, it's nice. It's, I'll try to get some pond hockey in this week, which I haven't done since I was like, so that'll be awesome. Fun.,We're freezing here right now. Yeah we're gonna get we're gonna get snow this week which is weird.,Oh wow. Cool.,Snow all around. You see there is some news they said this cold front. Oh yeah. They said somewhere in all 48 like states there will be snow.,Wow, that's cool.,All 48.,That's crazy.,It's up to Hawaii.,Well, I'm sure Alaska, but they're just continuous, whatever they call it. I don't know vocabulary very well. I'm kind of a degenerate. It's not contagious. There's a G in the word. It's kind of like continuous.,So I'm meeting with the team at three today in a couple hours. And what I'd like to do is give them solid directions that they can start on this week. So my question is, is there anything you would like me to specifically have them focus on in this first week sprint to kind of get them get the ball rolling.,Yeah, I think this makes sense. So you can stick to the script here in terms of like that first week, I tried to provide a little bit of color there just to like, help give them the context that we're starting off with those assumptions, just getting a sense of like the strengths, weaknesses, the SWOT of the department. Now, to the degree that they can provide you with any of these assets, that would be great too.

 They might have, this is all about kind of bringing us all on the same page. So they might have some of this stuff floating around that we don't have access to. So I think on this being like, look, let's drop current links in here. This one, I won't, I won't confuse them and move that. Anything they can drop in here or in what new things would be great. They can do that. Be good. Second thing would be be just swapping this around before that meeting.

 So dumping it down to wherever you want to. And then priming them for when we'll meet, and I guess that would be next in our agenda here, would be setting up time to meet with them. So if that works for you, like the next Monday, I can meet with them next week when we find time with those two departments. And we can have that productization meeting with them. And I'll just try to like, do you want it?

,What kind of meeting do you want just with each of the heads on separate calls? I think.,Yeah. Yeah. And, um, I'll, I'll give you a briefing this week for them. I'll just kind of bundle it together in like an email, but it's basically just going to be, um, look, here's the services sheet that we have for web serve. Now we're just going to try to get consolidate everything in here. As a starting point, let's review our independent areas that we do in our department. So we can review that.

 Any assets you have aligned with it over here would be good. And then that'll be part one, will be subservices. Basically, part two is positioning. And they should come with an idea about this for their department. And again, this is giving structure to these sprints. That could be maybe too vague in here right now, right? It's just like, hey, analyze your service and, you know, what's happening. I feel like we're going to help do the building for them.

 So it's more about like extracting like that data from them. And then when they move on into the next week, I'm going to continue on in a timeline focus here for a second. I'll continue on to be developing it kind of in the background, in a touching base with them, bringing them collaborating, right? So they feel like it's their proposal too, right? It's their department capabilities deck ultimately, but I'm helping them build it.

 So. I love it. Yeah, we'll do that. And yeah, that'll be the focus for that. And then you'll move into the following week, which will be the sales stages. And there it would be good to meet with the head of sales. And I think, and again, that's where like the directors are going to have some, viewpoint, but like so much of this will already be achieved by the fact that we're going to be developing the service up front.

 So we're already going to be talking about upsells and cross-sells and things like that. And then with the sales leader, we can figure out our winning by design stages and just kind of get those locked in, make those good. And then for the directors, they only have to do a piece of this, which is like, all right, let's think about your involvement in sales a little bit.,I think this is going to be really good bringing in and our sales leaders, which are Chris and Paul, but they're both kind of like main individual contributors. And I don't have a head of sales. So I've got like, we've got BD and like inside sales. And I've got the guy that heads up the inside sales and the guy that heads up the BD, but I don't really have the most organized sales department. But I think getting this buy-in, not only will it be needed for this process, but I think it will help them to buy into it a lot more anyways.

 So that's just kind of a warning that you're not dealing with like, it's always kind of like this.,It's always, it's always a mix, you know, but it's fine. Hey, sales of sales. If you're good at sales, that's, that's all. Yeah. Yeah.,They're, they're good at sales. They're, uh, perfect. They're not good at hearing the processes. They're not good at, uh, yeah.,Uh, I would have actually put them on the entire eight week sprint, but then And I understood that about the sales department and I was like, I don't think we would accomplish much with them in an eight week sprint,right now. But maybe down the road. Paul and Chris are good for about 20K new monthly recurring revenue per month, each. And so that's why they make the big bucks. It's not because of their beautiful minds. Not that they're dumb or anything, but their competence is in building relationships, being cool guys that can convince other people to sign these contracts. They're not great at everything else.

 Yeah, that's fine.,And I think we'll get a sense. Yeah, they might not be able to answer some of the process-based questions but they'll have a sense of some of the other elements of it that are important. Now, is there like a CRM master at the agency?,Is there like someone in the marketing maybe across that or what is that? Kevin and Seth handle that and they are sharp.,Okay, cool. Because we will end up having some dedicated questions for the sales phase as well. Like, you know, like what's the optimal amount of calls? Like what's our like sales velocity or what should it be? Like, well, based on the stages, do we want an intro deck and a proposal deck? Is that the right combination? Right? Questions like that.,And actually like, I mean, Chris is going to be pretty good for a lot of that stuff. Paul, the BD side, he's just at a conference after conference, building relationships with people. Sometimes he's been building a relationship for two years before this person becomes a deal. And they kind of skip the lead phase entirely. And once our CRM sees them on the BD side, they're already pretty qualified.

 Chris, on the other hand, he's kind of like a machine. He sends out probably about a hundred emails a day to targeted prospects that are customized. They'll have some screenshots of their SEMrush. He follows up very, very like in a disciplined way and touch points and he pulls stuff out of it pretty consistently. So Chris will be very helpful and he will need intro decks. Paul's the business development leads, which are, you know, most of our sales still come from some sort of a referral or Somebody saying something good about us and and connecting us those ones tend to Kind of want to rush through the sales process And they already kind of trust us.

 So there's not all that building. Oh, we're so great. They're like, oh my buddy Kyle said you guys are doing great work for him and like yeah, we're struggling in our admissions and we heard you can help, like, let's do what Kyle did.,Right.,And at that point, like, decks are helpful, but you could probably send half of those people a scope of work and an agreement and just just get straight to negotiations.,Yeah, that's cool. It's a small world, probably, right?,Very, very small world. They all refer to each other. This sounds horrible, but it's kind of true. If you remember trading Pokemon cards, it's like, oh, I got an Etna. I can't take the Etna, but this guy over here could take Etna, and maybe he'll give me a Charizard or a Sigma for it. And yeah, so everybody knows everybody, and the word spreads.,Yeah, it kind of speaks to the importance of that client satisfaction piece, right? Like you kind of have the golden goose. Now the trick is just not to kill it, right? And just feel like, look, everyone's happy.,Everyone's referring or do it like that's that that becomes even more important. And then operationalizing a referral program that maybe our associate directors can pitch to all of our clients like so that like maybe every two months, not on quarterly business reviews, but just like a casual, Hey guys, you still get a thousand bucks if you refer us somebody that could probably increase our referrals like twofold.

 Yeah. Yeah.,We can link that up with like an NPS or something like that too. So anytime there's any like a signifier of like client satisfaction or good client Like, it's not automatic, like, hey, love that 10 out of 10 review. Would love to know if you want to like participate in our program. That doesn't, right, you hit them up at the right time. So yeah, we can link things like that up. So, all right. Yeah, Jordan, does that make sense for your call later?

,Okay. I'm really excited this is going to tie together because I was hoping it wasn't like going to be two different things, making things complex for everyone.,I think it's more like now we have tangible outcomes and systems built as we go through it, rather than just having a lot of- I totally agree.,Yeah.,It's super true. This stuff can just end up being a bunch of talk and meetings and docs, and then it doesn't land in anything.,It's like March, and then it's like, well, what's happening in Q2? What actually happened, yeah. Yeah, I'm excited.,Cool.,Well, yeah, I'm looking ahead to kind of these first three weeks. That's why I've kind of focused on that to start and I think we'll have other things will come together more as we go through that piece, but at least we're kind of on pace for like, uh, service and sales,development there. Um, yeah.,I switched those, um, weeks. Okay, cool.,So we'll be on track just to confirm you wanted it. Um, SWOT, wait, let me get back to my doc. So you want SWOT, then service offering, then sales, then core opportunities, right?,Yeah, that looks great. Okay, cool.,I think that's actually a really good flow, right? Because now we're, yeah, we're kind of bookending this work here with SWOT and actual opportunities, and then they can go right into like the operational side of it and do KPIs for their team.,Yeah.,Hey, I've got questions for you. Yes, because you seem to be like a frickin wizard. What's what's your background? How did you do this?,That's a good question. So I started doing work like mostly marketing based work like in college. And that allowed me to just travel a bit and be remote early on. Like kind of before remote was a thing. And I wanted to work with Ogilvy, which was kind of like, you know, it's like the mad men, like, right agency that you want to work with. And so I moved to Australia, where they had like a big kind of growing team, they did all Asia Pacific, and I got a job there.

 And that's when I kind of realized that no one knew what they're doing. And I was like, I was in, we didn't really have good service developed at that time. And I was, I was good at marketing, but you have to market something at the sell something to us also on all the pitches and everything. Right. Um, so I started developing things. It was like, Oh, IBM, like here's like a conversation map. And then they loved it.

 I was like, Oh shit, I can sell this to SAP and Microsoft now. And like, I started running around. So I ended up building like their B2B products basically. Um, and I was just kind of do, I was like, is this right? Like no one told me to do it or not do it. I just did it. Cause it was helping me close a lot more deals. And then the global head of Ogilvy came and I presented it to him I was like, this is what we're doing here in Australia kind of was like the guinea pig for Ogilvy worldwide because like we had the same profiles America like we reached like Affluent people right you speak English, but in a much smaller way So if anybody screws up or any brand screws up it almost doesn't matter, right?

 Yeah It's a sandbox. Yeah, and he saw it and he's like, this is great. We don't have this This is now our global b2b product offering and he just kind of took it and rolled it out worldwide. And that just gave me confidence. I was like, all right, like I can do this. Right. And so I kind of went from being like a T-shaped marketer to wanting to be T-shaped across the entire, um, any, anything dealing with like B2B services or, or knowledge transfer.

 So that's, that's how I kind of got back into consulting in this way. Um, and it's been great. Yeah, this is the fun stuff.,Did you ever work with Bastion Agency or Megaphone in Australia?,I don't think I've worked with those two, no.,Those are two agencies I've been a part of over there.,That need help.,Oh yeah, they probably could use some help. But they're pretty big already, like Bastion's the largest privately held agency in Australia. Oh, right on.,So I was just curious if you ever I don't think it sounds familiar, but I don't think so.,Yeah.,Yeah. They actually do need help really bad.,So it's a lot of times it's the bigger ones. When you're a little bit smaller, you get the systems right early on. And then you can just, you have such a good foundation. You can scale and like always tweak it, but that's my whole thing, right? Let's it's not going to be like person dependent. It'll be system built. Yeah. When we get really big, man, I get in there.,Like it's, it's like, it's put together with like glue and like chewing gum, you Yeah, I mean they had some systems but the only thing they're really good at systematizing was the the finances and then outside of that it's like the money Free ballin, you know, I mean services whatever pricing like everyone just figures it out. Yep Yeah, you know Yeah, totally. So Ed what happens is like each little satellite location or US operations And we would just create our own and be like, okay, we're just going to develop our own and crush it.

,It's great for like a level talent, like, right. Like the kind of the stars of the team, like proactive people, they'll kind of fill that space, but for everyone else. And a lot of times the people you're hiring that you be a button pusher, they need that structure to succeed, you know? Yeah. So that's what we're trying to do. Are. They need structure for sure. Yep, 100 percent. So hopefully you're all set for this week then.

 We'll just kind of gather everything. If you can set up, I'll do a quick summary email too just so we have these points in email, but if we can set up meetings for next week with the two directors that would be sweet and we can probably even look ahead to the sales meeting too if we want to get that on the books.,to set up meeting with and directors. And then for sales, what's the best way to link you up with them? Do you want me to, should we get you in our Slack connect or something?,Or do you do that? Or do you use email? Yeah, up to you.,I mean, do you do Slack connect?,Like where you can, yeah.,Yep. Slack works well.,Cause then I could just intro them to you and you guys can line it up however you want. Okay. But whatever is easy. Do you want to be in the meeting too?,Um, sure. Yeah, I'll join.,Okay. Uh, especially if we book it now, I mean, that's a month out, so I can probably be pretty flexible.,Oh, they're not ready for, Oh, it would be not this week, not next week, but the following week or third week. Yeah. All right, well, we're off and running. We're going to build the most functional, streamlined, sexy health care marketing agency on the planet. Let's do it.,One quick thing, and I think that should be laid out as our goal, is I don't know how to pay you. Did you email me? I don't know. Maybe I just haven't seen it. That should be a goal.,No, I didn't. I appreciate you following me or following up on me with that. That was really nice. I don't always get that.,Usually it's the other way around. Yeah. Well, I want to take care of it. We're actually like a little bit tight on funds right now, which, which, which changed pretty quick, but we, we had onboarded, you know, a lot of, a lot of costs trying to try to grow this thing. And, and the, the tides turned pretty quick from, from a surplus to a deficit. It. And it's all working itself out. But, but yeah, I just want to, I want to pay everything.

 And just keep keep moving ahead. Or well, not everything I want to pay half right now.,I was waiting for my bank details to resolve here because I was updating something for the new year. But I'll check on that and I'll send you the invoice. Okay, cool.,Cool.,Cool. And then I'll just ACH it or something.,Yeah. Okay, cool.,Yeah, that works for me. All right. Take your time. I don't have to pay you today. But I just I didn't want to I didn't want to miss it. And then you'd be mad at me.,Appreciate it. It's all good. Right on.,Do you have a quick question about a different Matter I don't today's a rough one for me.,No worries.,It's all good. All right I might be able to connect with you at some point today between 45 and 330 Pacific.,I'm good. Oh cool. All right

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Today actually on my meeting with them

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Going to show the dept. heads this sheet this week

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Looks like we took a big hit in revenue in Dec. -$44k

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you guys now work on going back to June 2024?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I have a video editor ready to start. Do you have projects?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If you get time today or tomorrow could you try to do this for our workspace?

follow this instructions for the google auth
1. Enable the Google Docs API
Go to the Google Cloud Console:
Create a new project or select an existing one.
Enable the Google Docs API:
Navigate to API & Services > Library, search for "Google Docs API," and enable it.
Set Up Credentials:
Create a service account (recommended for server-side applications) and download the JSON key file.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: actually appears I might be able to myself

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok can you look into that and see if we can get her busy? If not I'll ask her to do per project

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Meet Meeting
Meeting Participants:Jordan Dahlquist,Jordan Pohl,Preston Powell
Start Time: 2025-01-06T13:31:01-08:00
End Time: 2025-01-06T13:58:12-08:00
Transcript: Credit because our team had dropped the ball and it was like hey like like We're gonna give you the month for free If you guys stay with us, I mean they're in contract anyway, so they couldn't have canceled but gotcha But it was the right thing to do in that case And let me see if they're doing any better But yeah, this is this is about what I would want it to just say Are we able to go,further back in time?,What time are you looking at or what?,Oh Like just do another sheet for every I mean, um, no November, October, we want to get back to like June so that we can make your targets and stuff.,Yeah, no, I think that's great. Let's do it. I didn't get there yet.,I was just seeing if they could even do one sheet. So let's I'll ask Kevin to work on that. Cool. But Kevin built this with Seth.,Yeah.,OK, well, they're.,Their variable revenue.,Is not in there. I think some of it they he was just saying he doesn't know what that is or how to do it. It's the ads, but but Yeah, just comment on it and tag him. Uh.,I don't know exactly how to comment on SILs. Oh, here it is. This should be all the ad space. I already did it.,I already commented.,Just so you know. OK. You don't need to do it. Cool. And then bookings. Yeah, returning point of contact, referral, okay. So some of these might need to go away, but because.,Yeah, well also, if we get a better performance sheet set up, like what I was wanting to do with Tracy, We would actually already do all this stuff, too, on top of everything else. So eventually, we may not even need this sheet if we get that set up right. That's a side conversation, obviously. And then what's variance? Oh, variance from December versus...,Yeah, November. November, okay. Yeah, positive, negative, whatever. It wouldn't be NRR necessarily, but positive would at least go to that one month's So what's December project revenue to beat versus December variable revenue to beat? And then project revenue, variable revenue. A funky setup. So that would be like projections, right?,December.,Yeah. Versus received. Yeah.,So this is our sales team needs to start a, um, so what we're doing right now is like a Frankenstein version of what we really need, which is a huge tracker.,Like what I showed you that track.,Cause then we would have the sales department filling out What's your projected closes? What are you planning on closing? We'd have, what are we planning on losing?,And we would have all that there.,I mean, this is good for now. We'll just leave the top empty, I guess, until we have that.,And no wins in December, no new clients? Those are cross-over. They don't get any credit for new clients Right, like if they get a new client they're there and our Doesn't change My girls team brings in a new deal, right?,So this is client wins, but so you're saying Client wins so origination project.,So like if paid ads Move somebody over to our new design then that does count And that would go under there one this month, yeah, so none of that happened basically Exactly. I got you So 44 K so that's gonna get better cuz 7k is gonna come off of that the follow in January, right that credit Yeah, I mean, we're not going to continue that credit, but it might just turn into a full on turn. Ah, OK. And to be honest with you, I would let them out just because.

 They.,They have.,There's hard.,It's not even that. Oh, we're in we got we got an advert. We got Yeah, we're getting back back to back back to business with them. They're getting a lot of qualified leads. Yeah, especially over the last seven days. It was picking back up over the last 15 days.,Oh, awesome. So you don't think we'll lose them in January?,Well, we might. So here's what happened. We came out of the gate swinging. And this is always bad news for us. Really, what we want is we want the first six weeks to be shit and then to get better. So they did really, really great. When they started in October for like three weeks, and then it fell off a cliff, which is actually something that we've been running into sometimes with people. And yeah, but basically, we are back into seeing lots of thumbs ups, which They got qualified opportunity So why did we lose all these other clients then?

 Because that's a lot of it's going by what so Oasis detox That one That one was never gonna be a good client there's a bad admissions team, and it was a rough client. Technically, they owe us money. And I think they're still getting services. We'll get some more detail on that. I don't know if that one actually churned. Wait, what happened to my note that I just made?,Disappeared.,Maybe undo? Nope. I have the thing open, and I never saw your note. So maybe it just didn't enter. I don't know.,Weird note there.,That was really weird. Okay, and then true self.,Other bad plan or what?,No, no, they did really well. They were with us for years. And I'm friends with them. They were super apologetic about the whole thing. But basically their deal was that this guy was buying into their company. Uh, and he's just like, all right, so it's something out of our control. Yep. That one's out of our control. Just bad timing. So both of those you can put as the same. Uh, but yeah, that, that shouldn't have any negative anything around it.

 Okay. Reflection, family intervention. I don't even know what that is, to be honest with you. Horseshoe Ridge did not churn. I was going to say, isn't that your buddy that we're working on right now? Yeah, maybe he was due for a renewal and we just didn't send it. And then neurobehavioral center. Should I just delete it then? No, leave it here until we until we solve it. Yeah. Neurobehavior center.

,Yep.,detox la.,They were a four month project. Oh, it was a project not a monthly. And they want to talk to us about doing SEO for their other site, but we don't want to do it because we're having results with that DetoxLA thing and we can't get it through the client's head that their domain DetoxLA is crushing it. They've got like this umbrella company that has no physical locations that owns all DetoxLA and their other places.

 We're trying to get to them like, hey, do SEO on DetoxLA because it'll make you money. That is making you money, that other thing might make you money in two years.,So it's another out of our control type deal. Okay. No, no, no.,There's opportunity here. They're not mad at us. The four month project ended. So yeah, it churned and they didn't renew. But they do want to do a renewal, just not in their best interest. So need to have some conversation. And the problem and you'll see where I'm I'm the fucking bottleneck, right? So like nobody is doing anything about detox LA because they're they want, you know Trevor has his person on there and they're not, you know, bringing it back into sales So it's basically on me to approach these guys be like, hey, I heard what you said to Trevor It's fucking wrong for the same reasons.

 I told you it was wrong four months ago the fifth Yeah, I think we need a process, right? Because as of right now, I don't think that's gonna serve us well. The Renew Group, I wasn't aware that we had churn here. Yeah, let me Let me get with cuz Let me get with Jordan pole and we need to figure out how they're pulling this data because it's not good. I whatever they're doing What it's from QuickBooks, but maybe they're pulling it wrong Yeah, so I had an issue with QuickBooks too, and I was dealing with Jordan pole on it.

 They might not even polling it wrong but but for whatever reason Jordan poll invoiced a few people that were supposed to get invoiced on the 1st of December on the 29th of November which would look like churn from oh yeah from a number standpoint exactly because but it's not and I'm hoping that the renew group group falls into that, and a lot of these may fall into that.,Why don't we have Jordan keep this updated here?,The client losses one. I'm just going to ask her. Let's get her in here. Get a water.,Yes.,She's typing. Yo, yo, yo. Hi. Coming back from lunch. Oh, all good.,Quick couple questions.,So is the Renew group Still our client I thought so I had never heard anything about it, but I guess they're turned why I think because they're I Don't know. I just saw on HubSpot that they're Like they were turned and I'm assuming their contract was up or something. I didn't touch him.,I don't think that's true I think that was like a miscommunication between Seth and Kevin and and you and what their job was because like Our process around clients that have churned is is super fucked up and you didn't build them, right? I Don't think so. They're off my MRR.,I Wonder why I Have no clue because I never got an email from them saying that but when we were me and Kevin and Seth We're just going over HubSpot stuff.,They told me revenue or a new group was churned Well, they're fucking wrong and they're not like okay, so we've got problems with Jordan some of the things we're doing is making Jordan Pohl not charge our money Well, I,don't know why they would turn I to turn don't they have to contact you and cancel wouldn't we know.,Yes, so if their contract is up there has to be like a new at least with these are the instances where they don't have to contact me is that their contract is up that deal is churned and then a,new deal is made. No that's not churned that's just.,Well it's churned and then in the bottom where it says revenue and active date it says renewal but like on On top of the deal, it does say churned because there's not an option that says renewal on there.,What the fuck is this? Okay. Are we serious? But was anybody told that they churned because like literally Like it seems as if Like, this was just, like, given up on, like, for no reason.,Yeah, I literally, it says, in HubSpot, churned, and I was like, I don't know what this is, but I guess they canceled.,No, they didn't cancel. And Trevor had a meeting with all five attendees, and, like, Trevor was never communicated that they churned. Doesn't think they've changed. This is not good. Yeah, I don't know. Okay, this is a problem. We got to talk with Kim Jordan Dahlquist. It's Kim's job to handle these renewals. And if she's not taking them serious, I think like it's a major, major problem. It's going to be really easy to win this deal.

 We'll be like, hey, we're so sorry your contract ended because you guys wanted to sign. And wait, did it even end? That's that's the bigger question, because I don't know. Well, if you don't know. Like nobody's looking like you're the one that does the billing. I'm not saying that it's your fault necessarily, but like, okay, so a renewal came up. Let's just look at this contract real quick. So this says, yep, it turned.

 So we need to call Rick right away and say, hey, so sorry, But October to November, November to December, December to January. So they would owe us money in December. Did you not charge them in December? No, their revenue and active date was December 17th.,So they were billed in December. I can double check that, but I do have it in HubSpot. It says their revenue and active date was December 17th.,That's the wrong date. I mean, like the last time they were charged was December 17th.,That was when the revenue became an active, at least that's what I thought I was supposed to be putting the last time they were charged.,No, it should be the last date of service. So it should say January 17th, because the December charge would go through for January. So you're saying though that they were charged three times. Total is $6,500 a month. Yeah.,Let me, um, I just got back to the office. Let me look in my laptop and see and double check.,If they were charged twice, you need to bill them immediately. If they were charged three times, we need to reach out to them immediately and be like, Hey guys, Your contract is over as of January 17th. And then we need to get on the same page about when the recurring revenue inactive date is because we're going to lose a lot of money here.,I know I was messaging Kim at one point when the contracts became done. And then she was like, I have notifications that are And I was like okay. So I was like I don't necessarily think that that's part of my position.,ultimately, it's It's got to be a team effort, but we've got guys that are just going pulling the data from the sources and Making this list of churn clients and then we have Tim who's supposed to do the renewals But if she doesn't do the renewal like I don't want you guys to just mark it churned and say oh, okay There it goes cuz Trevor's gonna continue doing we're going to have to work on that. The client thinks that they're paying us and,And Jordan Dahlquist thinks that we lost that revenue.,Yes, they were billed 1017, 1118, and 1217 Rooney Group. OK.,I mean, a situation had happened with Inc. 7 in which I knew that their contract was up for renewal. Kim said she was communicating with them, but they went two months without signing their contract and no one followed up. Finally, Kim had followed up and then I had to bill them for two months and I put that in the December sheet. So CalSunrise, their contract is up this month.,I don't think any for PPC I don't think anybody's reach out to them. Yeah, we've talked to them. Okay, we're, we've been talking to him. So, but all that just gets marked as churned in your sheet. And it's not all correct. So, okay. The renew group needs to be removed from this because the churn date, even if they didn't renew, would be January 17th. I'm going to remove that from your sheet. DetoxLA.

,okay neurobehavioral center and I figured out what happened with why california care and also um digital explorata were billed on the 29th and I think it was because I was off on the 29th and I didn't I wanted to make sure that their invoices were still sent even though they were supposed to be due on december 1 and I think I was just like panicked to make sure they were you can you can make the invoice stay different.

 Yeah, I think I when I invoice them, I accidentally put the invoice date as 1129. Yes, we're billed. I didn't miss the billing on those. I thought I missed it from California Care, but I didn't.,It was just billed on like the incorrect date. Okay, that that fucks up our, our our deal there.,Yeah. And normally, I don't do that.,So I apologize. All good.,Just I I think I can change the date, if you want me to.,Change the date. OK.,Yep, we're trying to fix the books.,Pretty sure I can. Let me make sure I can. OK, I got to go, guys.,All right, see you guys. Wait, what did I do? Did I do something wrong?,with your new group. No no you didn't but we failed and it's not your fault.,I just want to make sure if I needed to change something that I and then moving forward I should be putting the revenue inactive date is last day of service not the date that they were last charged. I can go back through today and double check all of the ones that me and Seth did to make sure that the revenue active date is the last day of service.,OK, cool. I got to go and get on this meeting. But I'll be able to meet with you again, Jordan Dahlquist, after.,Cool.,See y'all later.,All right, bye.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: it worked for me

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: hwo did you get the json file?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: you rock thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: and we can use my resources instead of fiverr

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: this is awkward lol

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Whenever we are ready for video just lmk moving forward

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ok wish I knew that before making her an offer

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So I wouldn't worry about it for now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: There probably were very few cross sells

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: 8 Week Sprint Weekly Meeting
Meeting Participants:Jordan Dahlquist,Mitch Marowitz,Shannon Lee,Trevor Gage
Start Time: 2025-01-06T14:57:13-08:00
End Time: 2025-01-06T15:19:46-08:00
Transcript: you What up? Hey. You changed your hair since I saw you last. Yep, last meeting of the day. I let her down.,Let your hair down.,Nice. That's awesome. How'd your day go so far? Not bad. It was loaded with meetings.,You know, Google, the Google calendar is giving you insights now into like your time. And so I was like looking at it, I was like, you know, it gives you a week by week breakdown of how much your time is spent on Yeah, it was like 20 hours. I was like, Yeah, that's like half my days in meetings. But a lot.,Of course, it's only tracking the full hour, not necessarily how long you ended up actually on the Google call, which I find is usually less. That's true. Yeah. But yeah, still. Do you like vimming? Do you vim like hotkeys and stuff like that?,Hmm, just in docs. I had I'm a bit of a whiz in docs, but...,Google docs?,Yeah, but not in other places. Oh, okay.,If you like really fast calendars, really good calendars, I use VimCal. It's freaking awesome. Oh, really? It's just so much faster to book calls and you can Vim the entire thing. So it's just instant and it does all that kind of reporting stuff. You can have multiple You can have all your emails hooked up to it. I could screen share a book and show you.,Yeah, that's interesting.,Also, you should check out Superhuman for emails.,I know Preston was into that for a while.,I don't know if he still is. Dude, Superhuman changed my life.,At least you like Inbox Zero. I love it. I can dream.,The thing is you can have it remind you of stuff like basically you can say remind remind me of this in two hours or remind me of this tomorrow and then you can clear your inbox because it's like you have You're forwarding it to a future you yeah anyway It's really cool because When you want to give someone like your availability for example, you can just hit availability and like mark out times that you like and Or you can use AI to do it.

 You can hit Find Times. So anyway, you can block off a bunch of availabilities. And then you just hit Copy. And then that's your email that you can send to the person. And it has your booking link and everything in it. I can still look up other people, see their calendar. I have all my other emails up here. And then you can also just book your own calls, but everything's hotkeys. I'm using my cursor right now so you can see, but like, you can actually use keys for the entire thing.

 So it's pretty cool. Anyway. Yeah. And then superhumans a lot similar talk, you don't have to pick up your mouse.,Hey, what's up, Shannon?,Hello.,How are you guys doing?,Your plants are looking lovely. Thank you.,I don't even need to take care of them.,Watch those plants. Like a Tamagotchi.,Hello. The hair's down, Trevor. That's right. It's after three.,You know what that means. Dude, everyone here has hair. Except me, so I don't know.,Not missing anything.,I see a little bit there, man. What's that yellow stuff? Oh, I have hair. I've been shaving it for like a year. I kind of enjoy it.,So yeah. Thing not joining again?,It joined my last meeting. Why does it keep doing that? I don't know. Maybe AI. Mind of its own. It's gone rogue.,I wonder if because we're in the same workspace and yours is here, maybe it doesn't even both.,That's possible.,That could be, I don't know. It could be a step up from the meet and geek when there's like three of them trying to butt into a call. Yeah, right. If that's true, that'd be really awesome. If it's not true, we need to get it figured out. If you want to invite it, you can. I mean, we're not going to do anything that crazy today. It's just kind of an overview. All right, cool. Well, this is our first meeting with all three of us.

 So that's kind of exciting. Hello. I have this time set up every week for us to go over our eight-week sprint. And then I also have one-on-ones with each of you. And hopefully, we can keep the 80 eight-week sprint calls about the eight-week sprint and then our one-on-ones are about your departments and all that good stuff and Basically what all kind of brought this all to fruition is Preston is trying to help us systemize our departments and just get more efficient get better what we do in terms of our internal processes and documentation and Goal setting and all this kind of stuff which I know can be really hard to do when you're in the trenches every day, but it's kind of a necessary evil.

 And sometimes you have to just push through a bit to get some of this stuff done because it's going to help your future self. So this is the kind of investment where this is actually going to make your life easier down the road in the coming quarters, halves, et cetera. So anyway, I definitely want to make sure this eight week sprint isn't something that's taking up massive quantities I do think there's elements of it.

 That'll be challenging trying to pull things together you know get some inspiration to come up with ideas for your department things like that, but It shouldn't be something where you're spending like 12 hours a week on this or something like that. So If you do find yourself spending that much time talk to me and I you know Either I can help you or you're doing it wrong something like that The goal is to be really effective and not time-consuming.

 So along with that, we have a consultant named Laurent that we've brought in and he helped directive scale up with this exact thing. So processes and productization, documentation for each department, all the way from sales to onboarding, to offboarding, to everything. And so he, we just contracted with him to work with us over the next couple of months to assist with some of that. And I can screen share and show a bit of what he's going to be doing.

 But the really nice thing is this eight-week sprint actually really aligns with what he's already going to be doing also. And so the cool part is he's actually going to make your jobs easier because he's coming in and bringing a bunch of these resources and solutions. And all he's going to be, basically, basically doing is meeting with you once or twice here and there to pick your brain on things about your department.

 And then he's going to go back and do a lot of process layout, documentation, building decks, all the way from pitch decks to call agendas to everything. So it's going to be really amazing. So what he's doing really ties into what we're doing with the eight-week sprint. And I reviewed the eight-week sprint with him. We actually ended up reorganizing some things to make sure it all lines up. But the reason that's cool is because normally, you guys would have had to do more legwork in terms of actually building and creating things.

 Whereas now, he's going to be doing a lot of that legwork in alignment with what we're doing in this eight-week sprint. And so the goal here, a lot of times, the eight-week sprints can be something where we do a bunch of work, we create a bunch of Google Docs and presentations, and then it doesn't really land in any results for your department. It just kind of is like this doc, but how do we actually implement it?

 And so our goal is to actually have this land in change. You know what I mean? It's actually going to impact how things are done to make it run better. So I'll do a little screen share of our Sprint, let's see here. I'm going to share my entire screen. Hopefully it doesn't go haywire. Let's see here. All right, can you all see this?,Yep. Cool.,So this is just going to be kind of our timeline document. And you guys already have access to it. But up here, you're going to find a link. Link to a template doc. And this template doc is just to try to make your life easier during this process. So you don't have to like kind of figure out the structure of everything. But for week one, it's kind of like you're just filling it out, basically. So just take some time to think about it, reflect on 2024.

 You're going to be going into your analysis of what went well, what needs improvement in 2024, a financial overview, which be simple. If you already have this, great. If you don't have this, we need to work on building out whatever we can, even if it's very simple. Growth milestones. This could be big wins throughout the year, big changes, new service lines that happen, anything along those lines with finance.

 And then a SWOT analysis, which I already put in an example SWOT analysis here. So this should be fairly straightforward. I do want you to definitely be thoughtful about it and not just clod the entire thing or GPT it, but have some actual thoughts and then maybe have clod help you. But I'd like to have real compelling thoughts and ideas here in this SWOT analysis. And then lastly is simply just respond to the question, what would need to be true to double your department's revenue in 18 months?

 Who would you need to hire? What resources do you need? What tools do you need? Yada, yada. And so that's gonna be week one. So that template, you can access that and duplicate the entire template and use it for yourself. So make sure you do that. Don't use the one that's at the link there. And then, so yeah, week one, we're gonna be working on that. Another thing down here, and there's a little list deliverables, you're free to duplicate this director sprint doc too.

 So you can actually use the little checkboxes if that's helpful, however you want to do it. But you're going to just submit that SWAT document to me via Slack whenever it's done. And I can also help with that in any way you need. Please let me know. But I would like to get it before our next call to review. So hopefully by Friday, possible. And then on our next call, we'll look at it together and just do a quick overview.

 And then part of what Laurent's doing, I linked right here. So this is a spreadsheet that outlines everything he's going to be working on, which I don't want to overcomplicate this for you. You don't need to worry about all the stuff that's going on in here. But if you go to Assets, one small project I'd like your help on is if you have access to any docs or assets that fit any of these categories, I'd love if you could paste the links in here under,the current.,So like he's asking for ICPs and personas, things like that. If you have that for your department, great. If you don't, don't worry about it. You don't need to create it. I'm just saying, if anything that you see in here already exists and you know about it, just help me by pasting it in here or send it to me in Slack and I'll paste it in here. But I'm trying to gather up everything that already exists for the company.

 And that's linked there. And then lastly, Laurent wants to set up a meeting with you guys one-on-ones for sometime next week. And so if you want to send me some time slots that work for each of you, or I can just check your calendar if you're fine with that, I can pick slots that seem to be open, whatever you prefer, and I'll get that set up with them. Do you guys have a preference either way?,I would just prefer for you to check my calendar.,Cool.,Sounds good. I'll do that.,Ditto.,Yeah, that works fine for me. All right.,Sounds good. And then, so I'll just kind of do a little bit of an overview of the rest of the eight-week sprint. So week two. To be doing a service offering review. So we're going to be looking at our current service offering for the client. We're going to be looking at efficiency, result rates, things like that. I'll have more detail on this. I'll provide more detail before we actually get into it.

 So I don't want you to look too far forward and get stressed out or anything like that. Just focus on one week at a time. You know, a lot of this is general and then I'm going to dial it in as we get closer. So service offering review. Then we're going to do a sales strategy review. And this is actually going to involve the sales leaders like Chris and Paul. Then we're going to be looking at core opportunities for 2025.

 So vision statements, strategic opportunity documents, things that we can do to help improve cross selling, improve upselling, things like that. Development, this one's going to be really cool, because this is what's going to educate determine our bonus structure for people that are in your team. So for every person in your team, we're going to be setting up leading and lagging goals for them. And that's going to help them have a bonus structure in place so that they can actually be growing towards something and getting paid for it.

 And then next, we're going to be doing a roadmap development of 2025. And this is where we're going to basically take everything that we've done up until then, and put that all into one initiative for 2025 that we're going to work on for the next year together. And again, I'll be working with you on all of this stuff. And then lastly is just refining it on week 7, and then putting it in a very simple presentation deck.

 It doesn't have to be fancy. It's mainly just some way for you to present your roadmap for 2025. And that's it. Week 8 is just finalization, feedback, communicating plans, and then moving into next steps and things like that. As far as expectations for each week, just try to have the last week's deliverables done before the next call. So if there is too much, if you have a really crazy there's certain things you can't get to, let me know and I can try to support you.

 Like I said, I want this to be effective. I don't want it to be like a ton of hot air. So I'm not trying to create a bunch of work. I'm trying to create effective results. And so that's my main goal. And so, you know, don't worry about making things fancy, wordy, anything like that. What I'm looking for is just true insights directly from you. So yeah, just try to be prepared for that next call. But the deliverables, please try to send to me, you know, prior to our weekly call so that I can kind of review it.

 So whether that's Friday evening, Monday morning, whatever works for you. If you want to chat about stuff during the week, I am absolutely here for that. And we can also go deeper into your department on our one on ones that we have tomorrow. And I can help answer questions and help you kind of support your process there. So, I think that's about it. Any questions I can answer? Nope.,I'll just, I'll probably have some as I work through the week one, but not right now.,Cool. Where can I find the financial overview and that information for my department?,Yeah, do you not have anything currently?,There's no tracking?,I know Preston showed me some during our meetings, but I don't think I have access to that.,Yeah, I kind of have the same. But yeah, Preston does have something like that. He showed me so I was planning on just asking him Because yeah, I've been dug too far into the financials.,I'm sure he has something similar if you Shannon Yep, that sounds good reach out to Preston feel free to CC me and I'll make sure you guys get that if he doesn't I'll figure out how to get it in your hands and if it's Too outdated or too complex or anything like that. I can work with you to create a new one and try to just create a simple new one if that ends up being better, but yeah. All right, cool.

 Also another quick announcement that I was gonna mention We have this new NRR tracking sheet. I'll share my screen real quick. So can you see this? Sorry, I hate asking that every time, but sure, okay. This is gonna be our new NRR tracking sheet that you guys will each have access to. And you'll be able to go in update whenever you gain or lose a client or upsell a client. So it's a little messy right now.

 We're still building it out. But for example, the purple here is client win details. So you upsold a client or cross sold a client. Client loss details is a client that churned. By the way, ignore this. Like some of these have not churned. This is just not all correct data because I had someone working on it for me that doesn't have all the data. Basically, any time a client churns, we're going to put it in here.

 Any time a client cross-sells or up-sells, we're going to put it in here. And that's going to calculate each department's NRR. So then each month, we're going to know what our total NRR was. So this is the December one. We're going to have one for January, February, and ongoing. And so we'll be able to actually And then that's going to also support future bonus structures as well. So the more money we can retain or even be in a positive, the better, obviously.

 So you don't have to do anything about this right now.,I'm just kind of previewing it to you, just so you know. Cool.,So how do you guys feel about this? Is this okay? Is it too much?,Let me know your thoughts. No, that's good. Um, well, uh, yeah, it's all in the process of clearing things up. So yeah, I'll go for it.,Okay, cool. All right. Well, great guys. Appreciate your time then. And, uh, yeah, we'll be in touch. I have calls with each of you one-on-one tomorrow, so we'll chat more about it then.,Cool.,Sounds good. All right.,Later.,Yes.,Bye.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let's go off of that then

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok, I did the 8 week sprint call with Directors.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you let her know?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You and shannon can throw the pdfs into chat gpt and output a csv doc and then load into google sheets

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Are you abel to access your teams calls?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Didn't know it did that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Wow ok that's super cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: :exploding_head:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And then create a GPTS that has all knowledge

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: we should pinecone our entire company's call transcripts

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: That should really help you with visibility

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: i just had an idea

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Anytime we say we'll do something or a client asks for something on a call, it gets sent to asana as a task

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: One idea is we could program it to pull "client promises"

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yep

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Going to be sick when i'ts done

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: it's pretty complicated actually the setup

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: this guys seems to know his stuff tho

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm getting my GPTS setup first and will see how it goes

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: awesome on that!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah if this guy works then we will do it across the board for each dept.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I need to buy a $200 fiverr project but seems like they don't accept amex. Do we have another card I can use?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah totally

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yeah I'll ask him

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: let me ask

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I wonder if I can have him send to that account the request

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ahh

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I have the vendor already under my account

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Sorry I should have thought of that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm having him send it to the webserv one

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome, yes. <@U03REVDN1QT|Shannon Lee> do we have any existing website pitch decks we can reuse?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Will be there in 30 min

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm driving into the office

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U03REVDN1QT|Shannon Lee> what date could you take on the WAVE project?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ready when you are

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: no worries

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: PPC Operations 1:1 Weekly
Meeting Participants:Jordan Dahlquist,Mitch Marowitz
Start Time: 2025-01-07T09:27:52-08:00
End Time: 2025-01-07T09:55:03-08:00
Transcript: Peace.,Okay.,you make.,Hey. Hey. Sorry.,I had an interesting call that we'll be doing a little bit different type of work, which is fun. Like GA4 reports and attribution and stuff. For a client or?,None of our clients.,I mean, technically it would be a client that pay us, right? Or if they do, but it's this OASI It's a like, um, they do organic social for Airbnbs essentially. Um, and they're having a hard time getting attribution for their organic social.,Oh, so this is another agency that's we're going to help.,Yeah. Yeah.,I'm going to see what I can do. Um, and build something out on, uh, yeah. Google analytics for, which, yeah, it's fun. We don't do much of that. And I've spent a decent amount of time learning about it, especially a while back when it was like forced upon us. So.,Are they paying us for that or how's that partnership work?,I think Preston said we're going to do like this first one for free and then see how it works for him. And then we can potentially do a bunch of other ones. That. I'm trying to get Seth to do stuff like that. Probably going to be a loom thing.,I don't know if he's that level, but I know he's gotten pretty good at that over the years.,Yeah, perhaps I'll get some insight from him.,real quick. Cool. Right on, man. So when are we going spear diving? That's my question. Shoot, whenever.,If you're planning to go out, let me know. I haven't been out in a little cold right now.,Yeah, yeah.,I need a new wetsuit is what I need. I have a big old hole. I haven't been in the water very much this winter. I went though, right before. Was it Christmas Eve or Christmas Eve Eve. Anyways, around then, when I realized I had a huge hole like right on the side. So I got to put that on my list. I have a big old list of like should I got to do by wetsuit needs to be on that list. Dude, I bought a wetsuit like a year ago.

,All right, you're in it. Actually, it's like year and a half ago, but it's like brand new. And then I tried getting in it the other day to go surf and like I guess I just came gained a bunch of muscle because I like my shoulders could barely get the neck closed. And like, I was like, man, I know I didn't gain body fat.,So it must be nice. Yeah, I'll probably have the opposite problem. I was like, much not much bigger. It was probably about the same weight. I've just gained fat. But this this year has been tough for me as far as being able to work out. Yeah, yeah, I try not to complain about it too much, but that's why I'm constantly like moving my desk up and down Yeah, that's good.,Yes Trying to try to deal with it. Uh, yeah I went to this chiropractor, but he's not really a chiropractor, but I went to this basically chiropractor in Austin, Texas that he had this like six-month program or whatever and It wasn't just cracking your back. It was like exercises that you do at home and stuff and it literally fixed me like I had really bad lower back pain from surfing and different things and some days I was like incapacitated like could barely walk and Neck problems all this stuff and I did his program and it literally fixed me.

 I haven't had any issues in like over a year now and It was all about it's like less about getting better or popped or whatever, it's more about fixing the muscles through specific exercises to realign where it's off, you know? And it really worked, man. I was, like, blown away. And there's actually a company that does it here, but I think the nearest one's in, like, Carlsbad or something like that.

 But anyway, maybe try to find something like that where it's, like, someone that can help you with the rehab Rehabilitation exercises to fix it not just get Yeah, send me Like I don't know if you have anything to point,me in the right direction I went to a guy who was like, yeah, like a chiropractor PT guy. Yeah, honestly, it did help And then I don't know I kind of like re-injured it. I stopped going back in it Anyway, so I need to get back on that but yeah, I've been trying to do different things. But anyways, I don't want to get too far into it because we have limited time. But yeah, if you'd send me what you what you.

,Yeah, I'm tracking down for sure. All right, cool. I'm going to keep these weekly one on ones pretty. Quick, I mean, I'm down to get granular and go down into detail and stuff like on these calls, but they also don't have to be long, like I don't need to be long. So mainly just had a few questions that I thought we could go through each And if you have specific things you want to go over, let me know and I can put that in our weekly agenda.

 But for me, mainly just an overview of, um, what did your department work on last week? What did you work on? What are you working on this week? How's your eight week sprint going and how can I help you with anything? Those are basically going to be my main questions. So, uh, and then, like I said, if you want to go over anything more than happy to, um, and I think that's it. That's gonna give me a good idea and like stay more connected with you and what you're working on and stuff and help you better if I have all that knowledge, so Yeah, if you want to start off with what,you worked on last week, that'd be great Okay What did I work on last week I have like amnesia if that's the right word sometimes like things I've I've done Yeah, I Know I've just been consistently trying to add to the knowledge database thing and You know, here's the most recent strategy we've been working on With like dynamic location insertion that I did yesterday So I've just been trying to work on this.

 And then get the more data for it. As far as like the slack exports, which I haven't done anything with, but but those are there. Yep. So I just basically pause on that for now until I get this pine cone thing figured out, and then we'll probably use that. Perfect. Yeah, makes sense. And then I've also, since I've been doing a couple like onboardings myself, I have been editing the template with just text as I go.

 And so there's a number of different things I've done here. Some of these have multiple tasks. And I mentioned using project roles so that they get assigned to the right person. So now when a project started, it will auto assign the task to the person. I made some due date changes. So anyways, basically, So basically a lot of things just regarding the SOP and the knowledge database stuff is what I can just wrap it up as.

,And trying to get rid of older stuff that's been lingering in the template. That's awesome. Cool. That's great. Our training call with the team tomorrow. Good.,I haven't gotten started on that task that we that I need to have ready by then, but I do. I am going to finish it today. Yeah, and I'd like I'd like you to kind of run that call, too.,I don't want to be like stepping in and doing stuff, you know. Um, so I'm like absolutely more than happy to, uh, jump in on any part of it or do part of it if you want me to. So just let me know. But other than that, I'm just going to let you kind of lead the way and I'll just be there.,Um, but yeah, if there's a specific thing you want me to touch on or whatever, let me know. Okay. So then, um, obviously there's the task. And using the type form that will then enter it to Asana. I could go through my notes on the previous meeting. Yeah, here's the doc link again, if that helps.,Oh, yeah, I think I have it just open right here.,This?,Yeah, if you go to the top, that bold text is the stuff. And then if you go down, I think a good way to introduce the call to everyone would be to go over the pain points. So if you scroll down, oh, I can make this editable for you too, by the way. Now it's editable for you. Sorry about that. If you go down, there's the list of all the issues we've been facing. And the way that I came up with all those was I interviewed everyone in your whole team.

 Used my cloud project to pull all the pain points. And so this is like, this is like universal pain points for me. And so if we go all the way down, keep going down, right there where the red check marks are. Those are all the things that people brought up with me. And so the cool thing is, is that, you know, we did these interviews, we found out what pain points people are facing, and these are them.

 And then we're bringing solutions to them with all these items that we have listed up above in the bold So it's kind of a cool way. I could even intro the call and explain that. But basically, we're just getting really active in resolving problems and making things more efficient. So yeah, it's one way to approach it.,Cool.,Key points.,And then walking them through each of those and how to do it and what the new process looks like And then They need to also know that you're gonna be checking in on that stuff, you know Like this isn't just hey do it and now we forget about it. It's You're gonna be you know, checking in are people using cloud are people using Cloud to write ad copy and things like that. Also, they need to know that just because Claude outputs ad copy does not mean it's perfect.

 And they absolutely are probably gonna need to make edits. And so people need to know that. They need to know, you know, don't be lazy, read through it, edit it, make changes if you need, it's gotta be good.,So yeah, anyway, those are some thoughts on that. Yeah, the ad copy, that's also something I'm gonna want And then this week, I guess we can just merge right into that question.,So you're going to be working on that today. We'll do our training call tomorrow.,Cool, well, yeah, I think I know what, I got to have ready for tomorrow. And then I'll get going on the stuff we talked about yesterday. Yeah, probably tomorrow. Yeah. How do you feel about that?,Do you have any thoughts, feelings, questions?,Not yet, honestly, my my focus hasn't been. Fully on it, not that I don't care to do it, I just haven't sat down and been like, okay, I'm doing it now, you know what I mean?,No, totally.,I know we just rolled it out yesterday afternoon, so it's all good. I'll definitely, I won't be shy to reach out if I have questions or whatever. I sent you the thing I got from Preston right away, but other than that, I hadn't dove into it yet. Okay, cool.,No worries. Yeah, and if it's ever feeling like a major Let me know so I can try to help you out. Happy to jump in. And then my last question, is there anything I can help you with this week?,Anything to take something off your plate? I don't think so. You're working on the pine cone thing. So I guess, yeah, we'll do that. Just wait on that. How long do you think that's going to take?,He said it's going to take a week from yesterday, basically. So by next Monday, I should have something. And then that's my version. And then I'm going to need him to set up one for you. So that'll be a week.,Cool.,So you have it in two weeks or less.,Right on. Yeah, because the only other thing I was going to say is to help organize the pull the important data from our slack messages and potentially team meeting data to pull into a cloud project. But yeah, we'll just cross that bridge when we get there, I suppose. Yeah. Are you talking about for pine cone?,Or what do you mean? Exactly.,Just in any sort of way useful. Because we still have a bunch of data available within the Cloud project, not enough for all the meeting data. But yeah, just other contextual stuff. I'll continue to add to it, but Yeah.,To me, I look at our Cloud project as like a V1, and it's kind of like good enough for now.,It's an MVP.,I would view it as like a 0.1. Yeah. So this is a minimum viable project. Product to get us through the next couple of weeks and start getting the team even used to using stuff like this. And then I'm telling you, this Pinecone setup is going to be a beast. It's going to be sick. And it's going to be through ChatGPT, not Cloud Jacino. But he's setting up just a massive database that this ChatGPT can actually pull from just basically an unlimited database of content and then answer questions and do all that kind of stuff.

 And we can train it and all that. So it's going to be what we've built, except a mega version. You know what I mean?,Yeah, perfect.,Yeah, I would just leave it for now, unless you think there's a reason not to. But I would just leave things how they are for now. I wouldn't be spending too much time on it.,And then I would just merge over to the Pinecon once we get there. It's kind of what I figured.,So yeah, I'm good then. OK, cool. Any issues with your team you're facing that I can help you with?,Anything at all? Any feedback you want to share? No, I did everyone get into read, read and then also asked everyone to Loom.,Oh, yeah.,I know a lot of people are in read because there's a lot of calls populating, so that's good.,I think everyone got on read, yeah.,Yeah, that's great.,And then I don't know how many of them are doing it, but it looks like a good number, so that's good. And by the way, I reviewed some of them, and everyone does really good on these calls. I watched a couple of Fabi's as well and obviously like I do feel like she could use a little coaching but everyone has a really good positive attitude on the calls they seem knowledgeable so I like that yeah yeah,we have a good team yeah it's really cool yeah everyone that's everyone that's still here definitely can can handle their own and Fabi's good too she just she says she's a is too much sometimes, which is coachable, you know? Totally.,Yeah.,So anyway, I highly recommend people start using Loom to even answer questions for clients. People love when, instead of writing a big, massive email to answer a client's question or explain something, just have people send a Loom. You know what I mean? You can walk them through it, just like you're on a Google call and say, hey, I answered your question. Here's a video I made for you. Here's the link.

 That could be a good thing to go over on our training call, by the way. I'd put that down on my notes, yeah. Yeah, that'd be great.,Yeah, I think they have the limited five-minute thing, but they, you know. OK, that should be fine. That should be fine, yeah. It's not for these big training things, but for them to answer a quick question, yeah, absolutely.,Yeah. Most clients don't want to watch something over five minutes anyway, so it's actually kind of good.,Yeah, I think probably over a minute or two. They don't even read my emails fully sometimes, but anyways. Okay, cool. Yeah, that's a good point. So, all right, man. Well, yeah, I got what I need. I'll catch you up if I need anything else. Sounds good. Thanks, Mitch.,We'll see you later, man. All right. See you, Jordan. Bye.,it.

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Design Operations 1:1 Weekly
Meeting Participants:Jordan Dahlquist,Shannon Lee
Start Time: 2025-01-07T09:58:59-08:00
End Time: 2025-01-07T10:18:56-08:00
Transcript: Hello.,Hey, how's it going Shannon?,I'm good. You're in office?,I am. Nice. Yep.,I've been going in a couple of days a week.,Nice. Yeah.,Yeah.,Awesome.,I'm going to be going in, um, I think next Friday.,Okay, cool. Awesome.,If you're there. Perfect. Good to meet you.,Next Friday or this Friday?,Next Friday.,Okay. I might, I will see how it goes. I kind of come in on days when I have a lot of meetings.,So yeah, makes sense. Yeah. The rooms are nice. Yeah, totally. For sure.,I've been just using this conference room every day. But right on. Well, appreciate you taking the time to meet with me. I know you're really Yeah.,Yeah.,Are you able to do camera or, um, I, I cannot, I'm sorry. Okay. Alrighty. Um, all right.,Well, let's go ahead and jump in. I just, uh, I'm setting up these one-on-ones to kind of go over just any, uh, department questions, initiatives, things like that. Um, just to kind of have a weekly touch base. It doesn't have to be super long. It could be as short as like five minutes. But if we need the whole 30 minutes to dial into anything or working on something, we can definitely do that. So just to help me, at least when we first start working together, it'd be great to know kind of a couple of things.

 Like, what did you work on last week? What are you working on this week? And then that's going to help me understand kind of what is happening in your department. So maybe we could start out with that.,Yeah, what was the department working on, or what was the projects and everything?,Yeah, kind of like, what are you working on as far as the department goes?,What are you guys pushing forward? Yeah, so I'll just start sharing. Might be easier to talk through it. Sure. This is how we just keep talking. Of our stuff. And me and Maria, we meet three times a week. If we get another person, I think that will have to be daily, daily check-ins. At least that's the plan. But for now, since it's just us two, three times a week works fine. So we have these projects.

 Let's see, we have one, two, Three, four, five. Five active projects. We have a lot more, if you just look at it at face value. But a lot of these guys just kind of drop off and just don't respond. Oh, got it.,Like the client, you're waiting on them to respond, and so you move on to something else.,basically yeah so like this guy drug and alcohol rehab center of San Diego I don't think I've I haven't talked to him in like months now because he just doesn't respond I think before to prevent things like this happening I know that they wanted to do a system where I think it's the current system. I just don't know how often it actually gets implemented. The clients are supposed to pay half of the project fee up front, and then I believe after one month, maybe two months, I don't remember, they're supposed to pay the rest of it.

 Okay. And that's supposed to, you know, get their feet moving, but I don't know if that's actually happening.,Oh, interesting.,Okay, let me make a note of that and I can ask Jordan about that. So yeah, and then besides that, we have a SEO This is where the SEO team can ask us for any help. Which I think isn't much right now, right? Yeah, they don't need very much help at all. So this was kind of just like what we wanted to do. To help them if they needed it, kind of like an emergency. Like if one of them is like really overstacked and needs help building out some pages, they can ask us for help.

 Gotcha.,And then PPC is the exact opposite.,Yeah, we have a lot going on. Yeah.,Speaking of PPC, that training call tomorrow to show everyone how to use the type form and stuff. So is that good to go?,Did you have any other questions you need us to add to it or anything like that? It looks like everything that we needed was there. I just figured that we can, when we start testing it out, we'll be able to see what we're missing. But as a base, it looked really solid. Okay, great.,Awesome.,Yeah, so we'll show them how to do that. And then that's going to create a task every time and slack you a notification. So definitely just let me know if you need to change anything. If you don't want the slack message, if we need to add questions to it, if it needs to go to a different board, like whatever, just let me know.,Hey, sounds good. Yeah, I'm excited for that.,Yeah, I think it's gonna be fun. Everyone um and I think I made it so that every question is required too so like they have to have all their ducks in a row before they can submit it.,Yeah. So that's cool. Yeah um so yeah and then for me I've well there's just a lot going on but um What I wanted to finish this week was, you know, working on that new PPC service, but I wanted to ask you for advice. If there's like a template that I can use, or like, in terms of like, exactly the new PPC design service that we want to offer clients. So like any template. Or process that I can follow for getting everything I need to present something like that, or making a slide deck that people can present to clients.

,Sorry, I'm not quite remembering what this new PPC service is. What is that?,Am I forgetting? Yeah, it's basically a new service that Preston wants to roll out. It's like, right now we kind of just do design services for free.,Oh, is this the new CRO thing you're talking about? Yeah. Okay, got it. Sorry, I was lost for a second.,I don't think I explained it very well.,So yeah, do we even know what that exactly looks like, Like what we're of what the scope of work would be, what we're going to charge for it. Do you have any idea?,Or is that what you're asking me right now? Yeah. I want, I'm a little like overwhelmed. So I'm like, is there a template that I can follow to just kind of write down what seems right? Yeah. Well, what has Preston told you?,And maybe I can go and meet with him and get all this dialed in and then come back to you with more to be able to help you more, you know?,Yeah, let me see if I can find it. I think there was a spreadsheet.,Yeah, anything you have, I'm happy to jump in and help develop it, build a deck, whatever we need to do. I just need as much info as I can get. And I can meet with Preston about it too. I'm chatting with him later.,Okay, awesome. Yeah, I'm not sure where the spreadsheet went, but I could find it and send it to you. I just remember that there's different tiers. It comes with like landing pages and a be testing for the client Conversion optimization stuff. Yeah. Yeah It was like yeah, I think it was like one landing page a quarter or something like that it was like more than More than what the default PPC client gets, I think every client just gets one landing page.

 But they don't get testing, and they don't get variants, unless the PPC team decides to make copy variants for them.,All right, yeah, I'll get more info on that. And I can try to get you some more support there, for sure.,Thank you. Yeah, no problem.,With the landing pages, I'm curious, do we duplicate them ever? Or is there a way we can expedite that to make it just more plug and play?,We have a Figma document of all of the landing pages, just kind of like an article. Archive. And the purpose of that was for PPC to explore and see like, oh, I like this landing page that we've done in the past, or like, I like this section. And then Mitch, or I guess the department had a problem where they weren't liking how the designs were turning out. And so we had like a big meeting about it and they asked, well, what's the difference between this process and how Maria and I design websites for our clients?

 Because, you know, those are those look good. Those are satisfactory. Those go above and beyond, basically. So we're like, well, we have we have multiple designs to the client and they're all from scratch. So that's kind of why that happened. So they said what?,I'm trying to follow, sorry.,They said they didn't like it because what? It doesn't matter.,They didn't, yeah, the quality, they felt like the LPs were kind of meh. Got it.,But couldn't we just create like a few really like cool ones and then just be like, pick one of these three designs, you know, type of thing. Yeah. Out colors and fonts or something.,Yeah, I feel like that's what's been happening recently. OK. There's like one LP that they like and they're like, oh, we just want it to look like this one.,Got it. Yeah. OK, I got you.,Well.,They've started using fiber for a lot of stuff and we're.,Yeah, because our department just got a little.,Yeah.,Well, the good news is that we spent like over $2,500 last month on landing page designs. And so I'm actually hiring a landing page designer right now. Awesome. Yeah. So that person can either just be under paid media department, or they could be under your design department under you. Probably makes sense to put them under you, but yeah. I'm hiring someone right now, and it's going to be a little bit before I have some final candidates for you to pick, but I'll let you know.

 Okay, awesome. That's exciting. Yeah. And it's going to be someone in probably Serbia or something like that. But I just hired eight people for the SEO department from Serbia and North Macedonia, and they are amazing, like really good English. They're super They do really good work. So I think you're going to actually be pretty impressed.,Awesome. Yeah.,And there's a little bit of a time zone crossover. Like our 9 AM is like their 6 PM. So there's a little bit of a period where you can actually talk to them. Yeah. There's a time to meet. Yeah. Yeah, exactly. And I think for landing pages, it could work because it's very project based. Yeah.,So yeah, I'll keep you posted on that.,Cool.,Yeah. Yeah, so that's exciting. And then that should help with all that. And along with that, I was wondering, because Trevor was saying he ends up having to build a lot of the, I think they're called resource pages or something. Yeah. And he was saying that he wants to just duplicate those too.,So is that something, is there a reason we don't do that? That was a reason why we made the SEO request board too. Just for some backstory or like backing up a bit, when our director, so when the old director of design left, we basically had to pause our website project and like sales of website projects. Yeah. Just for that adjustment period. And during that time, there was like lacking in work and what I kind of had wanted to do was have design be more of a supporting role, like an internal design sector basically.

 And so I wanted Marie and I to take all of the resources pages from SEO and build them out for them. That was kind of my plan, which didn't happen. People didn't request resource pages, but yeah. But I think back then when the design department was a bit bigger, we also handled basically all of the resource pages for SEO.,So is that something, if we get this new designer in, they could help with those also?,And then we could move that back over to design? OK, cool. Yeah. If we can measure the cost, how much time saved for the SEO department as a whole, and connect that to financially, Because that means their workload, they could take on maybe an extra client or something, which is just extra revenue. Yeah, totally.,My goal is to just find a designer that's an absolute beast, that can just crank out one or two landing pages a day, you know what I mean? Or resource pages, and that's just all I do.,Yeah, that would be awesome. Yeah.,that we can be cranking out you know 20 to 40 landing pages a month we're going to be like solid and that's where we can start to look at rolling out that cro service because we'll have the ability to,actually do it yeah so I would hope that um with that new hire they could handle kind of like external design requests yeah I'm not external but like internal design Um, and that'll help everyone out Yeah Okay, great It,sounds good All right. My last question is just is there anything I can help you with this week? Sounds like I'm already gonna help you on the zero stuff.,Is there anything else you need help with? I think that's it Yeah, and then I'm just gonna be working on the week one Uh for the sprint If you have any questions, I'll just Slack you.,OK, great. Yeah, and if you feel overwhelmed at all, if you want to jump on a call, feel free to huddle me. Like I said, that A-Week sprint is not something to put you on the hook. It's more of trying to work on the stuff and just get it done, whether you do it, I can help you. I can help create spreadsheets. I can do whatever. So just keep me posted.,OK, thank you.,Yeah.,All right. Well, thanks for your time, Shannon. We'll chat with you soon.,Talk to you later. All right. Bye.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Is 6 months because the client takes a long time to get you what you need?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Had we already quoted them a number?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: $20k is too low for that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: way too ow

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Oh so WAVE is 250 pages?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I get you now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: wow that's big

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: A site lik this should be $250k lol

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If you get time to jump on early I'm ready

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We should make 50% profit minimum

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can help with this if you aren't sure

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U03REVDN1QT|Shannon Lee> what I would like to know is what would be a good price to charge that is realistic and where we make money

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I could createa. spreadsheet to map it out if helpful

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: let's include this in training tomorrow

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Change anything you need

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Here's the agenda for monthly client performance calls

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Would be cool to do it in the conference room and throw everythign on the screen

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can we make the trainig meeting in person tomorrow?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We should chat about that when you have time this week

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I forgot to touch on CRO service rollout with you

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan D / Preston Weekly
Meeting Participants:Jordan Dahlquist,Preston Powell
Start Time: 2025-01-07T11:00:34-08:00
End Time: 2025-01-07T11:30:12-08:00
Transcript: What up, what up?,Sorry, I'm late. No, you're good, man. How are you feeling? Really good.,Having an awesome day. Awesome week, actually. Good. Good, good.,Yeah, how about you? I'm good, but I got to cut 30 minutes short just because there's a big renewal and I just want to show face because it's like that client I watch in Alina Lodge and they're a big national client. They're not a big spender with us currently, but they're one of the best kind of case study types that we have. Everybody knows, loves, and respects them.,Love it. Yeah, so I updated our little agenda Let me bring it up.,I didn't do my vision stuff. And I think maybe we should just start working on it together. We can do that. Because I probably, we can just kind of openly talk about it. And I got as far as I got. And I don't know that mine needs to be super detailed. Because just just the overall kind of I don't want to get too specific That's what I want them to do about their their Department and and just have it align with kind of the overarching goals.

,Yeah, yours is just generic like Not generic but like just company wide So All right, cool. So for my agenda We got a lot of our stuff done last week that we wanted to, which is good. So let's just go down the list. So SEO, obviously, we're working on getting all our clients moved over. That was a great call this morning. We have another one later today to wrap that up. And then we can get our conversation going and get the decks built so we can actually do it.

 So that's good. Other than that, I don't know if there's anything else we need to go over for SEO.,I have my one-on-one with Trevor later today So maybe something will arise there, but I think overall it's we're on a good path there Yep, I agree just Trevor's Really uncomfortable with the whole thing And and has a lot of anxiety around it. So just be aware of that Not that that's a huge deal and he'll push through it. But yeah, when we have our call later today, there's like tons and tons of opportunities for upsells.

 So I think we just have to strengthen our approach everywhere that we can because some of these people that are underpaying us, like we need a new negotiation anyways. Yeah, I would say the same thing When we were going through it this morning, I was just like, rather than presenting them with like, Oh, we're taking this away because we have to we could present them with, Hey, guys, like, it's a new year.

 Here's our results for last year. Like, here's some of the things that aren't working this year. Let's come up with a new scope for this year. And, you know, that'll be more in your best interest. Yep. And this is what we can do We're not doing guest posts at all anymore. Here's a couple options for you. And here's the one that we recommend and why? Rather than uh, we're taking guest posts away Because you suck And I know you you were expecting them now, you're not getting them and that makes you mad.

,Well, screw you Later All right, cool All right, and then for PPC, we're really cranking. I've been doing so much with Mitch. We've got a cloud project wrapped up. So we're basically, we have a training call with the whole PPC department tomorrow for an hour. And we're rolling out all these new initiatives that we've built out with me and Mitch. So we've got a new cloud project that answers questions.

 So no one has to ask anything anymore. We've got a Claude ad copy creator that'll generate ad copy like 90% They're very little editing. We've got a Claude landing page copy creator that we built That can help create all the copy for that we have a new Asana project process with type form between PPC and design department that's going to improve the communication breakdowns downs and the Miss deadlines that have been happening there We've got the entire team using read AI now, which has been amazing.

 We can review calls, provide coaching to the team, all that kind of stuff. And then I also created a meeting agenda for client calls that I wanted to show you. And then also teaching them how to use a little more for async and client calls to help create a better client experience, too. So we're putting them in all of that tomorrow, and it's going to be freaking awesome.,Do you have any any employees that you have any like pain points with? Because it sounded like maybe you do.,What do you mean exactly?,You're pretty private, right? Yeah, I am. OK. If you had mentioned that that Sam was lacking follow through, just wondering if there's plans to address any of that or if there's like other employees with similar things and like if you're tracking that in any way or have any plan because because in my mind the person that does your job really well our good employees love them and our bad employees hate them and and somebody like you fires and and hires until you you get the result that you're looking to achieve.

 I'm not saying that you should just start firing a bunch of people. But at the same time, I have a belief that it's our job to find the best people in the world that we can afford. And it's their job to prove to us over and over again that they're that.,I agree. I love that you have that perspective, because that's how I see it, too. And it would be a bummer if we don't see it that way. So that's cool. Putting in my headphones here. As far as Sam goes, can you hear me OK, by the way?,Yep.,Yeah, so I mean as far as she goes I I am She just doesn't really listen when I tell her how to do something like with workable and stuff. She'll Like say she hears me and says she understands but then like absolutely doesn't do it and it's actually Resulted in us losing like a bunch of money and ad spend on LinkedIn like a thousand bucks like lost because she didn't do it right and so like that really pissed me off and then And even after that, lately, she like doesn't do it the way I'm telling her to do it, even though she's saying she will.

 So it's just like there's no follow through.,Like it's happening over and over and over.,So but on the plus side, she seems to be really good with the clients. Like I've watched some of her client calls and she's like very good energy, really good with the clients.,And so she's professional. And and actually she has some good managerial attitude about her so that the people under her do respect her. Yeah.,So I don't think she's someone that I feel like we need to get rid of or anything like that. I just think that I need to, as time goes on, I'm going to be probably bringing some of that stuff up with her.,And then one thing to keep in mind is that maybe an account manager underneath her Like, like, we could have three account managers under like, the proposed two to one is an ideal, and we're, I'm getting a lot of like, Sorry, I'm talking to Mitch because Mitch is worried about. The onboarding of new clients, and so I shared this with him. And Where is it? It's like an incoming. I have it on sales needed this week.

 So I shared this with him and you It made him a little bit antsy. I think we need this because I was like, okay, we have these three and these two are definitely coming down the pipe. And this one probably 60% chance. And so this one is already a client. So it's not like a big worry for Mitch. But then Mitch had two that he's kind of pushing off. So there's Need Treatment Now and Oasis that are gonna be big clients.

 So those are gonna be like 6,000 and 10,000. That's like a horrible idea. Well, cause Mitch is just isn't putting They've reached out to Mitch and he's not putting them in the sales cycle because of his own own Anxiety around the whole thing Horrible idea but but after I showed up this he had me up on slack shared a screenshot of his text message with one of them that's waiting on legit script like that really wants to get started as soon as they're ready and He's like I personally talked to him a number of people.

 So that list is maybe only a third or half of reality. But I haven't even reached out to them because we're not ready to take them sadly would be bigger than those clients you listed Atlas and Oasis. So we like it because of bandwidth or what's his issue? Because of bandwidth, which he Not the one that should be controlling that because all of that stops our budgeting to Acquire new employees Etc.

 But he is I mean we could go hire someone like we can make it happen We have to keep We have to continue stuffing business in or else.,Yeah, you know, it's like it doesn't matter if we don't have bandwidth right now. We'll get bandwidth with if their money's there.,Yeah, so I can like we can get about 40k in revenue right here.,Yeah, very, very easily.,We need to do that. No brainer. Yeah, well, I mean, this 21 I'm gonna get either way. Yeah. But this, this 16 keeps Mitch in an easier position than because and a us entirely. Yeah, you guys have the candidates, you guys can hire one and bring them on. Yeah. Like Laurent said, the 80% is their experience in the platform. So just just find somebody with good experience in the platform that we feel can do good on the client side.

 Yep. Okay. Other thing that we're missing. Other thing that we're missing that I think you need to get to Mitch right away is this. So you need a deck that handles the whole first month and a... An onboarding deck? Well, first and foremost, Not even an onboarding thing, but you need a startup timeline. So yeah, first 60 days should just be mapped out. So what's this?,Looks like we already have it.,This is directive, the one that they use. Why don't we just use that? I copied it. So we'll just call it a startup package, just like they do. Uh. Uh.,Here, let me just copy this whole thing.,I'm just going to slack you. Can you download a Word doc version so I can edit it? No, don't do that.,Please send me a Word download if you can.,There you go. OK. Thanks. All right, cool. I'll get that done. Anything else for PPC before we go on to dev because I have some questions there in our last 12 minutes Yep So that's all all right cool so for design For this wave proposal, okay, so 250 pages is going to take design department six months to do. And that's a freaking massive website. And I've run the numbers and like the phased approach and the hours that we're going to put into it.

 And like, we need to charge like 200k for that.,Not 20k.,I, we're not going to get 200k for that. There's no way that they would pay that. So we don't have to pitch it to them. But but we've been able to make money on that sort of stuff charging like 30k So maybe it needs to be more than that, but I don't think we're I don't think we can get a hundred K from them maybe we could try getting 50k, but it'd have to be a super solid proposal and You know we could be open to getting That money over the course of you know a year Whatever or you know, we could be like, okay.

 It's a six-month thing. You got to give 25% down and Payments of this amount at these milestones whatever you want, but So we don't have to propose this to them.,I Just don't think we should unless we are absolutely certain we're going to be profitable. That's all because Shannon's telling me this is a freaking massive project.,And but Shannon always does.,Shannon over what it is, 250 pages. That's like insane, bro.,Like if they're all building this. But think of it this way. It's it's 20 templates. Uh-huh. It's not 200 custom design pages. It's it's 20 templates that All 250 pages fit into great. Okay, so If I totally agree with you if it was 250 individually custom design pages, mm-hmm But it's not yeah, so it's like 20, okay, and I already know Daryl Stevens Builds websites for like 60 K for something comfortable Because that's I think what he charged Dallas and they have hundreds of pages and and I think we just need to Shoot for a bigger number so that if we do get it, we're excited about it And if they,don't do it, then we don't care. You know what I mean?,Yeah, absolutely So I'm with you, but it's got to be in the the you know 40 to 60 K range, okay It's not a $200,000 project that would be a huge ripoff and so the things you need to define is a price point for each custom design template and how many there are yeah and then you need to define how many pages in each template, and those pages should cost like a sixth of what it costs to design the template.

 Because we can have any bozo paste the content in there, and it's not like a tough design piece, if that makes sense.,Yep. OK.,And then and then you guys should come up with a what the timeline would look like It won't take six months It will take It will take four months Okay so We literally sold zero websites in December so them talking about how much work it is It's it should be like music to their ears. Yeah.,No, I know that's why I'm like, I don't really It doesn't make any sense Like I don't understand what they're actually doing and she's saying she's like super overwhelmed and I Don't know it's kind of weird like she didn't even turn her camera on in our meeting and I asked her to and she said she couldn't I don't know. I'm having like weird a weird experience with Shannon, but like she's also super smart.

,Yeah, she's also really smart.,I can tell I'm just like super smart.,She's super cool. She understands like some code stuff. She's worked on some pretty complex. So I think what you need to do, rather than worry too much about what she has to say about her workload, have her define what she's spending her time on. I've been trying to suss that out.,Yep.,Just tell her like, look, like, like, you're the director.,Like, I don't want you to be overwhelmed with this stuff. We need to build a system that works. So very, very clear descriptions of what you and Maria spend your time on. So that we can turn it into an offering. Right now, we don't even have an offering. We just throw together a website that's 7 to 10 pages for $7,500. That's all that there is. And then once we build that offering, we can define the roles involved, and then we can budget for who we And what we need and then we can build out this department Right totally And and like so be like hey, this is gonna be like a super rewarding process for you because Because Your title right now as design supervisor Like you're not a proper director because it's just you and Marie Yeah, you're gonna go away from being an individual contributor to a much more important piece of this whole thing.

 And with that comes more responsibilities, but they're not gonna be the responsibilities that you're used to. And if we're successful, it comes with a lot more money too. Yep. She's raved about you. She thinks you're great. Really?,That's awesome.,Yeah, but again, I've just I've totally neglected them. Yeah, because it's like, okay, we need this service. Just try to make it not lose money. That's the only thing we're trying to do here. Yeah, we try to make this not lose money. And we're good. Yeah, totally. Okay, cool, man.,This gives me some really good stuff to attack this week. And I'll get after this.,Okay, I think that's about it for now we're just cranking along Cool cool. Cool.,Well I'm I'm happy.,I Just need to prioritize getting these these sales in the books which is Which is fine. So that SEO scope super super important and trust Trevor's anxious about it. I think that's our really big like, hey, right now.,Well, the reason he's anxious about it is probably because he doesn't know that we can deliver it. Right. I would assume.,Why would he be anxious? Well, because he's built goodwill with all these people, and Trevor has a tough time worrying about the money. He's so worried about the client services. Yeah. So why would he be anxious?,Because it sounds like he's anxious that this won't work for them or something. But we're pretty sure it would, right?,I'm positive it'll work for them.,Why does he not think it will work for them, I guess?,He doesn't think that.,So what's he anxious about?,The actual sales coverage and the burning that goodwill that he's built. And it's it's his name on it. Yeah. And well, and yeah, he just needs to look at it from a technical standpoint.,Like this is what we were doing. It works for a while. We're moving into a new era. Twenty twenty five. Here's a new strategy that works way better and we know it works better. We want to usher you into this new strategy. Do you want to do it?,It's like, yeah, you shouldn't be anxious.,If anything, it's good to go to clients with new things. You're just doing the same old shit forever. That's when they start to question things, you know? All right, well, I'm going to let you go. I got to run to the restroom.,OK, and then Alexandra said, hi, Preston.,I like the approach you've shared, and I think it will be possible to get links. She said we're back to work tomorrow and we'll get the new camps in motion and happy face appreciate you taking the time to share your input and check in.,That's amazing. So she's on board. Love it.,I'm glad she thinks that it'll get links. I know Absolutely, if it's executed properly, it does get links. And not only that, that's what everyone else that's doing this successfully is doing. Yeah, exactly. So yeah. We just got to make shit happen. Let's do it. It's wild that somehow she thought that what we wanted was fucking guest posts on dog food websites.,I think it's because we overemphasize the we want your experience and knowledge. Yeah. I think we pushed that way too hard when we actually we didn't want any of her experience or knowledge.,So Yeah, oh, yeah, we'll figure it out. Well, I thought it was All right, cool.,Talk shortly. All right, man.,See ya

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool no worries

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can come to you or vice versa

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: we can meet in person if you want

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I have edit access to the wave proposal please?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: There may be like 20 templates?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you help me define price point for each custom designed template and how many there are will be needed for Wave? Also help me define how many pages within each template?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey hey! working on website proposal sheet

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: need to move it out?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just ping me when ready

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok I'll leave the call

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey <@U05A4CDP37U|Jordan Pohl>, quick Q

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: (website project clients specifically)

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Shannon was asking about billing website project clients for the second half payments. Apparently we bill based on timeline not delivery. And apparently some of them may need to be billed based on how long it's been. Can you lmk if this is up to date on all clients?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: canada or us

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: should I try to hire in CA or us?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: r.e. hiring a ppc Am asap - what's the salary for that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok thanks for checking on that to see if we can bill anyone. Also, how can we make sure it's always timeline based moving forward? Do we need to re-communicate policy to sales or whoever writes the SOWs?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do we have a policy guideline doc or something we can update? Or maybe we can create one.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Let me know if you like this!

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U0106DW71NJ|Mitch Marowitz> I know you are a little worried about taking on some of the new business opportunities, so I'm going to make an AM hire asap for you. Will review our candidates and start seeing what I can do.

We need to keep grabbing business right now. With our extended onboarding we now have, we can line things up nicely with the new hire also.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And jordan needs to also so she can manage billing properly

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Or can you send?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I send out a notice to the sales team to run all SOW's by me and Jordan Pohl before sending to clients?

Were having some real inconsistency in our SOWs and it needs to follow a policy and right now they aren't.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I want to see every SOW before it's sent to a client

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Some ideas:
1. Make them design a simple landing page on wordpress or figma
2. Make them pick from multiple existing landing pages and rank them on quality + explain why

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm getting applicants for the Landing Page Designer role. I need to send out a challenge for them to do.

What do you guys want them to do?

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: <@U025QMUHGTD|Preston Powell> what do you think of ? Once we get this finalized we can build out deck. ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: For new clients, we have a 60 day startup one pager that the managers will follow and share with the client and they will go over it on their calls

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Another thing to add to tomorrow's training agenda

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Finishup
Meeting Participants:jd@webserv.io,Preston Powell,Trevor Gage
Start Time: 2025-01-07T21:58:34+00:00
End Time: 2025-01-07T23:00:09+00:00
Transcript: Okay.,Peek-a-boo All right, so I was just on with Billy he's gonna want to move forward on SEO and cancel PPC that's what I suggested he do just cuz like the campaigns will run themselves and he got his value out of it and we just think it's a better idea for him and But we're going to talk about that real quick on the phone tomorrow and then get a contract. He'll sign it and then we'll be rocking and rolling.

,Grrrr!,Cool, gotta get this sheet of doodle back up. Where is it? Here we are. Okay. Get 6,500, arrive. Cool, yeah, this is easy. Hey, we're not doing guest posts anymore. We will add your PR outreach campaign as part of your But these guest posts are going away either way We charge a thousand bucks for this But we're willing to do it for you guys for you know, or we charge a thousand more than you're paying But we're willing to do it for an extra 500 Just because we don't want to just take your guest posts away and not give you a viable option And then if they balk at that we'll tell them to To fuck themselves, how does that sound that's what I like to hear?

 I'm sorry to bother you, but I'd like to Cool but yeah, we're gonna need to approach all of these with I mean, they're in a good spot to talk about it because their traffic just after like really big growth this year. And we can just be like, dude, it's a guest post.,So all the good stuff.,Yep. In the context um arrive uh traffic and just take a pitch as a new opportunity only charge 500 more when usually I don't think you'll get pushback there. You might get a no. But if we get a no, we'll just tell them We'll talk about what we can do. Um, but yeah, we really want to fix this, uh, this issue for you guys. That'd be like, Oh my God, they're so proactive and great. I don't know anything about cab and psych, like not a fucking thing.

 Oh, in other words, the tests and their own guest bus. Yes. Oh, so just run it all together as monema. We're going to say this is possible.,Let's.,Include. Right? But,Need to.,Get to what? 6k and pay per leg. Is that good?,Okay.,And then we can avoid this coming up in the future by just including the service charge in our pricing.,Yeah.,I think, yeah, that's just the way it is. And never, ever, ever bring it up. Because the service charge will be included, and then you're just, it's a pay per link thing, and people will like it. So, okay, our fee was 6,500, but now we know that our scope with PR outreach is 7,500 plus a pay per link model. Okay, what's your link budget? Typically, we tell people that they should have $3,000. However, it is pay for performance.

 And in some months, you're going to spend $1,000. Some months, you're going to spend nothing. Some months, you're going to spend the $3,000. But if you need us to stay within a limit, we can do it. Cool. Healthy life. Preston can. And have this convo with Trevor. Let's have them switch to Outreach. Because They are just three guest posts, not much. And it's probably about time for them to do that.

 Anyway, it'll probably be a better setup for them. Give us $500 more. We're going to run one campaign per month for you to a resource page. Veronica on Nova Transformations. Uh, okay. They have 4840 guest posts. Okay. Yep. So we try to get them to 6,500.,And so Ron was just texting me about working with Dina. Yep.,That's why I said switch to outreach, not Anything else?,Cool. Then we're at Glendora Recovery Center. That guy is ridiculous.,That guy, did I tell you what he told me? No. He fucking hit me up and he's like, oh my gosh, so glad I found you guys. Our beds are completely full, and it's all because of you guys. And I was like, OK, that's amazing. Thank you so much for calling me and telling me that.,But it's absolutely not true.,Shut up, Preston. Of course it is. You're ridiculous.,Let's look at this thing Before you guys there was nothing there and now we're just full and they are moving the right direction I'm not I'm not disputing that at all Like a like he'll send me random emails like,phones are dead Brittany confirmed phones are dead and then I'll hop on a call with him and he'll be like He told me what he basically told you one time and then another time he's like I'm thinking it's made,because it's Christmas but been dead Yeah Yeah, it's up and down and all around but mostly up so He's an interesting guy.,Mm-hmm So for healthy life, I Think he is doing he's doing Dina but but not like outright Fiatina, is that the idea?,It's just PR. OK. Sorry, I lost this spreadsheet.,So we're on Glendora.,Okay, they pay 6,500, okay Try to get to Let's just try to get to 7,000 and edge big benefits So, seven K and,Yeah, with all of these, we should come in and be like, Hey guys, like, let's look at the performance so far. It's been picking up. It's looking really good. But what we've noticed, we've gathered a bunch of data across all of our clients. Our guest posts seem to be having less and less of an effect. So we've spent the last several months trying to craft different ways to build more valuable links for our And let me show you a couple ways that we do this So rather than doing guest posts we want to move we recommend you move to this one.

 It's a little bit more expensive However, here's all the benefits and you know all the indications seem to Indicate that you need them You're just at that point now And this is going to really help you to continue that upward trajectory And even improve it Whereas the guest posts are gonna create diminishing returns and and not really work anymore So we're trying to move as a company away from guest posts But hey, this is way more expensive for us to do we hired all these people But it's more beneficial for you So we recommend this one the one that we want them to do.

 And it's going to be, you know, X amount more. But here's why you should do it kind of thing. And if they're like, Oh, well, I don't want to do that, because I don't want to spend any more money. And we'll say, Okay, totally, we're gonna move away from guest posts either way. How about we do this? How about we put you on this thing for the next 90 days in lieu of guest posts, and then see how you like it.

 And then after that, if you want to add it on, you can. And we'll just make new contracts that say we're going to do us for them at no cost for 90 days. And so they're not paying any more. They feel like they're getting more. And then if they don't continue it and pass the more money, this goes away after 90 days.,Yeah.,So you lock in your current price, cut guest posts entirely.,Exactly.,We just do it. It's good intermediary stuff.,Yeah, I think that's That would work really well I think that's a a good fallback for the people Because it's not good to say. Okay. Well, we're moving away from guest posts either way and you just lose them It's like a hey, we're moving away from guest posts either way We'll give you a new scope that includes these even though they cost a little bit more For the next three months. We don't want you to have to pay to them.

 We want to prove to you that they work. And then, you know, in three months, we can have a discussion about whether you want to continue them.,Yeah, I think that's good.,It's a good opt out without being like, well, then we've we've come to an impasse.,Yeah. Hey, don't worry about it. We'll just throw it in for three months. So you can get the experience now. You can try just the tip. Just for a minute, just to see how it feels. It's going to feel great. All right. True Life. Are we on True Life? I don't know what their deal is. I don't Much about them. I forget who they are.,Yeah, they're not the most communicative They miss meetings a lot. It's Josh's account. I don't feel super confident with it, but They don't have great results But yeah, it's a tough client a little bit just in terms of no communication not rough communication But we can give them give it a shot I mean the same thing is I or similar thing to Nova, I guess.,Try again. Well, the good news is that they get 4D830, I suppose. So they're not really valuable at all. We try to get them to 6500. If they balk at it. So I'm going to their website. And remember who they are? Who are these people? There's a big long empty testimonials block on their homepage. Was that something Josh built?,No, it's some issue. It's like it's pushed to the side for some reason. It's like slanting to the left.,I just launched the new Horseshoe Ridge RV site and it didn't go live.,Didn't take?,Well, I think it's just those AWS name servers. I think they take longer.,Oh.,I went through it with WP Engine and everything, and they're like, yeah, it looks good. It's just a propagation thing. But yeah, it's not going well. Or not even that it's not going well. It's not going at all. What are they called again? Oh What true true life I was trying to pull up there so brush, but it's bad. Oh Yeah, it's uh When did we start with them?,We It would have been They're from res maybe august yeah, I think so, huh?,Well, they're a lot better off than they were in august But they were they were peaking in october Kind of weird probably just some one-off vlog post. Yeah, they're better off than they were in August. Yeah, well, cool. We work some sort of renewal deal with them. Yeah. But if you think that is potentially going to lose us the deal, we could push those back that do nothing and approach that once has no communication.

 Don't approach until we have approached most others.,I think so.,There's a new group meeting already regarding. So no problem there. You don't even have to approach them. They're texting with Kim. They're talking about paid media, but they're fucking idiots So Get to 85 There's not gonna be any pushback we could lose that client, but I mean they don't sit there They don't say that Grata house They're a touchy one,to have those calls gone Touch and go like it's not the end of the world they they have like patience for the process with SEO, but you know PVC gets They're doing much better over the last two weeks it's,finally getting back to where it needs to be I And I gave him a free month. So maybe this one should also be pushed to the bottom of the list And maybe we should Maybe we should do nothing Push to laughs on list possible. Anchor tides. I don't think they'll have a bunch of pushback. But how are they doing? Pretty good. Yeah, I think they're pretty happy. It seems like a stable okay cool well then oh yeah and they're they're growing nicely um should be looking decent I mean they they got hit by this last algo but uh even better timing to bring that up so I think we should try to get them to 7000 rather than 6500 just because we're gonna pitch them on our a dollar PR and they are seeing some growth and they stopped spending on paid media and totally opened a call and they they seem to like me so I can be involved in that if you want I need less tabs, dude, I cannot find it again.

 Trevor, why'd you do this to me? I got my own tab issue over here.,I just closed a bunch.,Close tabs to the right. Let's see where that gets us. Okay, no pushback. Get to 7,500 or 7,000, right? Pitch both options as good. Let's talk about algo update. Cool. Silver linings. This should be an easy one. Just add PR and outreach work newer, bigger scope. That should be easy. What the hell is resilience recovery?,It plays out in Florida. Do they suck? They're not the most, like, attentive or whatever.,But I think we're in good standing. OK. These ones, we, It should be pretty easy because we don't even have to bring up the link issue Or just be like hey guys you guys been on a on our most basic scope for a long time like and Here's the growth we've seen Like and it does look like it's cramping slowly But like it's gonna be really hard to get to the next level and let's just work a whole new deal.

 Hmm Don't you think?,Well, I mean, I don't know if they've been with us for a long time. Where is it? Since July, yeah, I guess, yeah, five months.,That's one of Paul's ones.,so I can loop Paul in on it.,I'm done.,Thank you. Peace.,Okay, sorry, I got sidetracked by Jordan Dahlquist. Okay, this was resilience. Try and pitch. Upgrade. Yeah, get to 6,500. West Valley They're gone, right? I mean, they're not paying but they're still under contract Do they they get on calls with you guys, right? Yeah. Yeah Okay. I think they just missed one payment, though. I don't think they're way behind. Their card just declined like the other day.

 Okay.,are fine. Didn't we up their scope?,Let me check. Pretty sure he signed it.,Redo, redo. You're not finding it?,Ryan's blowing me up.,Let's see.,Okay, we have to talk to Paul. Can't let him send out that Alena large scope.,That's fine.,So the new scope for Refine start on November 25th. That's four pages of content, content brief.,No links.,Who is this?,Refine.,How much is the scope? 8k. And it started when? 25th of November. Okay. Okay. That was the web maintenance slash design package, right? It doesn't mention web maintenance So they're a casio, yep, and then and it says that's the 30th to the 31st is when that's billed Is the date on the contract the 30th or the Says the service agreement is entered into on November 25th, 2024. Okay, I'm going to change this.

 Okay. Much better. Okay, cool. And then they're on this web maintenance slash design that is also dated the 25th. That's 1500 bucks and it's a three month thing. Are we doing it? Web maintenance? Yeah, but it was supposed to be like a little bit more hands on. It's 1500 bucks a month.,I'd have to check with Shannon. And I mean she was looped in with Laura, but Laura's not there anymore. So I assume that they passed the torch Okay Yes, Mitch.,Whatever is gonna be easier for them. It doesn't really matter SEO tracking and then yeah, and maybe we change the Opportunity to be like bob and then viable opportunity just because I want to have something for like cash base That's a viable opportunity. That's not necessarily insurance-based yep an admission yeah if you can send them to GA for great as as key events but it's not like that important Just because if it does send them, it'll just be like a counter.

 It's not gonna attribute the source right in GA, right? Oh Well, if it can attribute the source correctly, that'd be great but But the GA for is an afterthought because we can just build the in call tracking metrics and screenshot that and put that into our SEO reports. Because really what they want to know is how many admits did they get and where did they come from And if GA4 is not a suitable reporting platform for that, that's fine.

 Yeah. I mean, I could probably get it to work, but I'm honestly not going to as it's not a big deal. Yeah, yeah, yeah. Don't worry about it. Don't do it at all. We'll worry about that down the road. If the SEO team really wants us to get it into GA4, we'll worry about that then. Cool. Then I will talk to you shortly. All right, bye. Cool. Yeah, so refine's a tough one. I don't know what to do, because we just sold this contract.

,Well, we're not doing links for them at all, so it's not a problem.,Oh, OK. Shouldn't we add links?,Probably, but I mean, maybe.,I feel like maybe, We should just. OK, so let's get this to zero. And let's just tell them we're going to give it to them. The PR.,Yeah.,OK, we'll tell them.,We'll just tell them hey look like we're gonna typically we charge a thousand dollars service for you to do this we're just gonna do it for you guys for free because we think it'll help you a lot and We're homies, but really they're paying enough money to get it anyways Okay Well, yeah besides the four pieces of content and the content briefs and stuff. That's a it's something Yeah, no, it's definitely something, but Yeah, let's just run PR for them because I think it'll make them happy and hopefully it pulled some money out.

 OK. Cool. They did come through.,In process of opening that scope cool 405 recovery Yeah, this one you're gonna have to try to Scope to 6500 and either I think PR outreach might be Might be the wrong move for them Because I don't They're at 5k.,Let's get them to a little more first We've set the groundwork for I mean we pitched in scope and renegotiation but Paul might know more than me, but Okay, we've definitely been talking about it for long enough Yeah, because,they're finally, like, into the couple hundred traffics a month. But their authority is so low. So, OK, cool. We just tell them, like, look, it's time. Quit dicking around. All right, that's going to be easy.,No matter what, I think they did do PR outreach for a while, but maybe weren't happy with it Or maybe it was just too expensive, but you can see how that Yeah This this is the detox No, I have,the detox at the very bottom of the list because I think they're not paying currently Oh Are they behind on their payments or?,You told him that we weren't going to charge him in December.,I don't know if they're going to be paying again and OK, then yeah, just cut this to zero.,Don't give it to them. OK.,I just. Just check in with them. And cut them if not. Cool. That one's easy, too. Okay. What are these bottom ones then yellow The last ones aren't a therapeutic partners and stuff yeah, it's just people that pay too low they under 5k Okay, well Yeah, I'd be cool though like fire some of these guys if we can't get them up because then you know, we're taking on some some big clients here.,Yeah, for Wood Dragon, I think they're behind in payment and they pay like almost nothing. So we might just want to try to fire that one. Smith Welding, we might just, because it's not treatment center, we might just keep them on steady guest posts.,They actually don't pass anything.,Okay.,So guest posts or no, no, don't give them another guest posts ever again. Okay. Like we've given them enough guest posts or enough.,So no more guest posts.,Yeah. Yeah. Um, and then I'm going to have a conversation with Kyle about them paying, uh, us. Can we do a call rail cleanup to like, sometime later this month? Because it's really big again, and that's okay, except for We're paying for so many companies that aren't ours and then we just need to build a process to try to get people to Get their own account first and only use our account as a fallback for Them being unwilling to get their own account Okay Like why is Helena Lodge in our call rail like it's a company that we paid for that's not even in there there.

 Yeah, that was a test.,We can get rid of these.,Yeah, but they're all recurring charges. I believe.,Weston, PA. They did get a Facebook ad call once. Last 30 days, they got four calls. The longest one was 43 seconds from Holy Crap Hospital. Holy Crap Hospital. Yeah It says Holy Cross, but I know what they meant Goal Okay, try to add PR outreach with Wayne's budget Hmm rise and this one will be cool because we can kill two birds with one stone and that one Rise sobriety center The hell is that?,I was just talking to Hannah about that. They can't get their Google business profile approved. They're out in the Where is it? I Don't know LA suburbs somewhere But yeah, it's it it's a tough one we might go them to pay more but our main like contact over there was their marketing guy who got fired so we are kind of on shaky ground we talked directly to the owner now um but yeah not great results but it was a brand new site with no fucking google business profile so tough to get leads glendale california Yeah, Glendale, that's what it is.

,I was thinking Glendora, but I knew it wasn't that. They don't have a team? Yeah, this is sketchy, dude. Would you go to rehab there?,Nope.,Yeah. OK, well, I don't know what to do there other than Uh. They get 4 DA 40 plus. OK.,I don't have a team page. It's going to be hard to get them much of anything. And if we do an outreach campaign, they're going to need, uh, resource pages, which I don't think they have.,Right.,No, we'd have to build them.,Yeah.,Uh, and they, why can't they get their Google business profile approved? I don't know, man.,It, uh, they're idiots.,Is that what it is?,They've done the video multiple times.,It keeps being not verified. It's the one that I created that window decal. For and like sent it to him.,It still didn't work, so I'm at a loss. I don't know. Do you think they committed like a bunch of fraud and I think they probably. It looks like a place you could go and die. Oceanside mental health. Uh.,Yeah, we can just have have the talk with these guys have the top three. And guest posts don't work and we. Cool. Are we done clinically Alps? I think you gotta keep getting them guest Suggest PR... Weren't they on PR before and didn't like it or something? Yeah, they couldn't respond in time. Okay.,They're like, we don't, we wanted, we responded to these ourselves, thank you, and then they just didn't do it.,Uh, okay. Is there new people there new marketing person same like expert, okay, uh Bring of issues with pr and past If able to overcome the issues with pr then fine 70 plus guest posts five of them It replaced our outreach. All right. Well, I'm sure the decent 70 pluses are all used up.,Okay, so let's try and replace what they have with outreach and just keep them on the same pay and then just dangle the PR and be like, hey, we have PR now, it's cheaper than it used to be because now we do a pay-per-link scenario. I know in the past we had trouble with it because you guys didn't respond to the queries And you failed us. So if you want to try it again, we can try. But what's going to be different, we also have this outreach thing.

 We're going to include outreach. We think it's going to be better than what you guys have. Not asking for more money. But if you want to add PR outreach again, we really, really recommend it. And here's how it works.,Make sense to me cool Choice house. We've already talked about them front range clinics easy-peasy Should we pitch PR?,Range yeah.,No, they're on the do-nothing list.,They already get it Okay Nice should we pitch Uh, resource page outreach, or do they not have research pages?,They kind of do. It's an oxygen site, so we don't have like a good method for building out like too fancy stuff, but we could put one together.,Okay.,All right. Well, then do nothing. Yeah.,Newport Beach Recovery Center?,A brand new one, low scope. No links.,Let's see, where are they?,No change.,Yeah, we don't get links. We'll get upsell them. It's maybe a little too early, though.,After March. Yeah.,Cool.,That'll be an easy upsell. As long as they get results. Or even if they think results might be coming. Because they were paying GoDaddy like $7,000 or $6,500. I don't know why in the fuck they decided to sell them for $5,000. I had them all teed up, ready to pay $6,500. And then I no-showed the call, which was absolutely Absolutely, my fault. But Kim and Paul had the call without me, and they fucking downsold them.

 That's pretty funny. Okay. Cool. Well, take Smith welding's guest posts immediately. Seven summit pathways we need to figure out. But it's not high priority. Okay. Damn, this is a lot of meetings. Yeah, it is. So let me just tell everyone we're rolling this stuff out in February. I think, are there good account managers that you can delegate this to so you don't have to do all of them?,I probably need to be involved at least in some way with all of them.,Why?,Well, because I said I would. And I want to make sure the message.,Yeah. That makes sense. There's no, there's a kind of a what's in it for me thing too, which, which the truth is for the account managers, there's not really, we don't have anything built to have something in it for them. Cool. Well, Let's say that we're 50% successful. We'll probably make $20,000 or $30,000 a month here. Um, okay. Then are we done?,Yeah, I had to jump on a meeting. So I think that's about it.,I think we got a good plan Okay, and then shop or though we have to continue paying for these guest posts How do they get? Eight and two is the scope Small outside of that That's pretty much the entire scope.,Yeah content briefs for their internal writing team.,Okay.,Would we say it's going good or no?,They might want to step it up, but you know, they're always like, we need to tie domain authority to sales.,And it's like, well, that's like three levels of separation.,Um, You guys need links, but when they were rebuilding the site, we couldn't do much else. Now we technically could, but it's not really our forte.,Shopify, e-commerce, SEO.,So we kind of just landed at links by default. But it's not going to be a great client. It's probably marginally profitable at this point.,Yeah.,They're really cool people though. And, uh, you know, they brought Oster into the full, they were Massimo people and they represent opportunity. Um, they want to do another one too, which is, uh, this compression stockings business. So that will probably start once the website's So, um, and that one will be a little bit more of a fresh slate. Be interesting, like doing some e-commerce SEO and like coming up with a different scope for it because I gotta go.

 I'm sorry.,All right. All right.,Love you. Bye.

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: There is a new design request! ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If we can get the messaging locked in then we can hand it over to kevin for design

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do we feel like we know enough now to do this deck design call?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Feeling good about call later? Do you want me to handle any part?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You have a lot going on

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Happy to help

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: k I'm going to cancel the call then

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Unless you want to get on and discuss it with me?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok great

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you send me the exact question copy and I'll get those added?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I dont see a share request from another email

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hi Milica! I shared it with your webserv email already, are you able to access it from that?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: thank you!

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: Do any of these times (PST) work for you? If it's easier, you can click on a slot below to book: January 9 (Thursday): • January 13 (Monday): • • January 14 (Tuesday): • • January 15 (Wednesday): • ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: but I'll add the rest

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So there is one already for where the emails will go

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Should be gtg

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok those are added!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Here's the breakdown

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I need to get a sexy deck build out for a website proposal

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: awesome!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'll get this over to kevin to design

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What's the best way to task you with design projects?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I just want to be sure I follow your process and not be "that" annoying guy

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: cool

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Heres an old outdated deck that is actually for the correct client but nothing in it is accurate

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: one with deliverables and one with paynent milestones

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: also note there's two tabs on the sheet

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: awesome, you rock, thank you

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: This should be true for all websites moving forward

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: The SOW will be based on timeline based milestones, not deliverable milestones for payments

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: no rush

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Within 1-2 weeks at most

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It's non-urgent urgent :rolling_on_the_floor_laughing:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: but it is now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It wasn't

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: They can put N/A if doesn't apply

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I just made it so every single question is required

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: 1. Great thanks, looks good
2. Zapier may be able to populate this based on a response, pretty sure it can actually
3. Checklist stuff?
4. Yes we should change to task id

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yeah we can work on the prompt responses

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: We just need to give it a frameowrk

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can you talk in 30 min and we can dial everything in before the meeting?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: let's jump on the link

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: yo

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: added now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: wow how did I do that lol

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: awesome thanks

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Process Training Meeting
Meeting Participants:Fabiola Morales,Jordan Dahlquist,Keaton Nalle,Mitch Marowitz,Nick Chepkevich,Sam O'Leary
Start Time: 2025-01-08T11:01:27-08:00
End Time: 2025-01-08T12:16:26-08:00
Transcript: There I never been up there, but whatever the Pacific Palisades are they're cooked, too Yeah, it's crazy my house was rattling all night and still is from the way that's wild Are you still in El Salvador no, I'm I'm,back home away from home.,Nice. Cool. What's up, Sam? Hello.,How you doing? Good. How are you guys?,Doing good.,Better than I deserve.,Why? What do you mean by that? I don't know.,Just what Dave Ramsey says, and I've been watching his videos. Videos lately.,Crack me up, man. When the people are like, yeah, I took out a, a loan. That's like 60%, a car loan. That's like 60% of my income. I'm like 70,000 in credit card debt. His responses are so funny, dude.,Yeah. Some of them are really crazy. It's like, how did this happen? You're like 25 and you're like in $2 million in debt. Yeah. Like, I don't even get it. All right. Do we have everybody? Yeah, I guess we're good to go. Cool. All right. Well, I mean, I'll just kick it off real quick. Mitch is actually going to run the call, but we have just been grinding to try to fix a bunch of just like low hanging little systematic issues to try to help PPC work better, faster, stronger.

 And so a lot of it's come down to building out Cloud projects that can help answer questions and create guidelines. And we've got those working, I would say, like 80% to 90% well in terms of the responses. And Mitch is continuing to work on those to get them optimized. But we're going to do a little training session on how to use them. And then we have a fancy new type form submitting design requests to the design department, that's going to really help them.

 And it's going to help you because you can just go to one type form, enter all your info, it's going to go to them, it'll create a task for them automatically. It's going to avoid a lot of back and forth. Using read AI is really going to help us massively. Some of the main reasons is because we can use it for the sales team to hand off summaries to you guys. So when they close an They don't have to fill out a form.

 They don't have to meet with you. We can ask AI to generate a summary about everything that's been promised to the client, all the client details, and it can educate you on the client for the onboarding process. We also created some templates for monthly meeting agendas for clients. We've created a 60-day one pager to help improve the onboarding process with new clients. And streamline that. And then that's mainly it.

 So I'm gonna kick it over to Mitch and he's gonna jump in and basically walk y'all through all this.,Yeah, thank you Jordan for that. So yeah, the first thing I wanna go over is the knowledge database for just general questions. As Jordan said, it's a, work in progress. But it does spit out answers. The answers that it gives like he says probably about 90 maybe like 95 percent accurate. You may have to ask it to dive in a little bit on details. But let's pull it up real quick and then just Go through it.

 Has everyone made that project? Yep. Okay, cool, cool, cool. So here is the one, let me see. Let me see, multiple tests. I was unable to fetch the document, but I was able to download it as a doc and get it to work. So if you do have issues with it loading, let us know. But let's say, I'll just open up what I've done. How can I increase my quality score on Google ad search? It provides a link to this video and It explains what the video is about Making sure ads are extremely relevant search terms all the things you guys already know essentially And so then I asked it how to do dynamic keyword insertion and it does explain fairly well how to do it and then like things to be careful with and some like additional nuances.

 This one here like be careful using dynamic keyword insertion with near me keywords. This is something that we've talked about before as they could look strange. If you need more info on that you ask it to dive deeper into why they might look strange. But it does provide good information there. Location insertion, it has the exact script, which we've been talking about today, that can break with caching.

 But essentially, It works pretty well. You just need to potentially ask it to dive in deeper. And if it doesn't know, it'll tell you that it doesn't know and things like that nature. And so if there's additional things that need to be mentioned, just let me know and I'll try my best to update it as soon as I can.,I was going to add too that we sandboxed this. So it's only going to pull data that Mitch has provided information on. In other words, it's not going to give you anything outside of what Mitch has provided it. So if it doesn't know, it's because we don't have documentation around it yet. And so if you find something that it doesn't have an answer to, definitely let Mitch know. And another thing to note is that it's conversational.

 So if one of these bullet points like doesn't quite make sense, or you're curious why it's saying something, just literally ask it. You know, why this? Why that? Like, what do you mean by this?,And it can help answer questions for you.,Has anyone tested this yet?,Has anyone tried it?,I did. I asked what could be an issue with the G-click not appearing or call checker metrics.,That is awesome sick So the cool part too is that actually pulls the loom video links to it literally It like you'll see in the response if there's a video available about that topic It'll share the loom video with you of Mitch literally talking about it. So you'll see in the prompt results It'll actually share the loom with you and you can just go and watch the loom on how to do it. And also sometimes it forgets to include the loom video.

 So make sure that if it doesn't give you one, you can always ask it, like, hey, do you have a loom video about this? Is there a video that has this information? And it'll provide it.,I will try it right now, because when I did it, it was, I think, before you guys uploaded the video. I just asked it, is there a video? And it just gave me the video. That's cool.,Yeah. Yeah. The videos are like past week edition. So yeah, this is basically AI Mitch at your side 24-7 unlimited access All good, I mean that's essentially the gist of this so makes sense to everyone right For like Like when you go to all, so we're only using,the paid media group guru project that we created. When I go back to all projects, there's a bunch of different ones. Is the SEO team also using this or are those like, okay, that makes sense. I assume some of the people on there, like the new, new hires, right? Are people, yeah. Cause I was like, who is, you know, like Amara.,Yeah, there's going to be probably dozens of these because each department is going to have projects like this that do different things that we're building.,Okay, so we just use the paid media guru?,Yep, just use the ones that apply to you. All these ones with the client names, those are specific to PR outreaches and pitches, so that's not something you'd ever want. Used probably.,Yeah, we're working on having something as far as like a notion that we've talked about for a while and organizing them. So like having projects linked out rather than just everything in here might be a thing moving forward, but you should be able to find it fairly easy. Yeah, too many things right now.,Sorry, I keep jumping in, Mitch. I know you're running this call, but we're working with a consultant right now named Laurent. Has anyone heard about that? No. Okay. So Laurent helped Directive basically productize their entire agency. And obviously that's like Preston's cousin or whatever. Anyway, we just brought him in and we're doing an eight-week sprint with all the directors right now. And this eight-week sprint is going to look like a vision cast goal setting, documentation, process set up for 2025.

 And it's, we're like running really hard on this right now. And then Laurent's going to help with putting all that into a notion, a notion database that literally has categorized resources for you. So it's going to be like, here's where your one pager agendas are. Here's where your monthly agendas are. Here's our process for how you onboard a client. Here's your cloud projects. It's going to have everything.

 And so that's over the next 60 days, what we're building out just so you guys know.,Sweet. Yeah, it's going to be awesome. Okay, cool. So the other two things are, and Claude are, we went over the landing page copy. I'll go over it again since Keaton was on vacation on the last meeting, but I want to go over first one I'm kind of excited about is ad copy for our addiction services campaigns. It is the, yeah still sharing screen, addiction services search ad copy generator. You know maybe I'll just paste this into paid media library.

 I had fun with this one. So let me just go through. I'll just open up one I did. So I just started off putting test. But if you prompt it, it will make sure it ask you for the relevant information before moving forward. These are pretty much all the ad groups that we work with currently. And so it essentially asks like, what ad are you, what ad group are you trying to make an ad for? I even uploaded the campaign CSV.

 So it should be knowledgeable on what the structure is. I literally just had to put rehab ad group I could obviously put a lot more about the client and other details and tell it other things But just doing this as simple as it was I was Yeah, that was me having fun with it Sam So I told it to take on the personality of Gandalf.,I love Gandalf. I was wondering about that.,That's fine. That's awesome. Oh, yeah Between Gandalf and Dumbledore Yeah, maybe we'll have a Dumbledore one moving forward I have more fun Doing it this way so it makes things more exciting we talked about like using pins and stuff and headlines and So this will show pinned headlines And essentially like how to do everything and they're Of course like with all of this stuff you need to review it, but it turns out like pretty pretty darn good You know, these are all headlines that I would absolutely use And how I'd use them.

,Yeah, I definitely want to Emphasize that is like do not just copy and paste like actually read through each line make sure it's seriously what you want. Definitely quality control, because AI spits out some weird stuff sometimes. And I don't trust it always.,For sure. But yeah, that said, I think this still absolutely kills. There's these four descriptions. And I mean, you guys are looking at it right now. I think it looks pretty good. So it's really that easy. And would be great to have one outside of addiction services, and we'll get to that. But since this is our niche, this is why some of the projects I've been working on are addiction specific. So yeah, that's essentially it.

 Landing page copy.,Addiction Treatment and Landing Page National Targeting.,I'll get that into Slack as well. You forget where it is, but Where's the I thought I had content attached to this. Looking at the wrong one. You might be in the wrong one. There we go. So only I would have been able to see that one. So this is the one you guys should be able to see. This has instructions. So before you prompt it, it will ask for the treatment center name, shorthand name if it has one, unique specialization and program details, stuff that should be in the paid media questionnaire.

 Unique value proposition and differentiators, uh, key certifications, et cetera, et cetera. Um, and here was one that I actually am using right now. And, uh, so here's just me putting in all the information that it asks for. If you don't list that information, um, it will ask for it to move forward and Here's, let's see, here's what it came up with. So it asked for additional things. It was like, what is the, what number do you want things to go to?

 So it actually works really well and comes up with some pretty good stuff. So it's a very specific template and it's, you know, just sort of the one we rock with a lot. I do want to make another one. Pretty soon with different structures. But you can ask this one to structure things a little bit differently. It's going to come up with this at first. But after it comes up with this you can ask it to you know add an additional section here or here.

 But it's just going to start with this at first. But yeah that said Keaton and Fabi I mentioned it in the Slack channel, but really excited to see how that stuff works. I mean, all the dynamic location insertion stuff, really excited to see how that goes. But if, yeah, we have another template type that kicked butt, then we'll go with it and get it into the Cloud Project and Template But again, you can have it reorganize sections.

 This is just what it starts with.,If we end up like people finding that they need to share a lot of feedback on things that are not working, may even be useful to start a channel on Slack of like a feedback channel, AI feedback. And whenever you just find something that didn't work right, just throw it in there and then Mitch can update it and fix it.,Yeah, I really like that idea for sure.,Cool, let's do it. Yeah, better to have it and not use it then like we're just, you know, throwing random messages in different places.,Yep. 100% agree. Cool. So, any questions on that?,No, just that it's going to be very useful.,Yeah, those alone should save you guys a lot, a lot of time. And I'll make sure that the like new skeleton or whatever is updated, but I have that ready. So any new campaigns that are like these national ones, these big clients should be like super easy to get started. And we have a month-long process, which we're going to get into. So you'll have more time and should be able to spend less time on all this stuff.

,For example, if we enter, let's say, the project on Claude, we cannot see the history of the questions that have been asked by you or someone Can you just share like what do you all the information like as an example so we can have it?,Like how to prompt it. Is that what you're saying? Exactly.,I was actually thinking that's a good idea, Mitch.,Like if you do share the project with us, but that prompt doesn't show to us. Can you open the project now and take a look because this one here This is the prompt it's in the description I mean, you don't see the prompt but You see what you need to prompt it if that makes sense. Yeah In the prompt it Is Asked to ask you for more relevant information so you can literally just type in Or what do you need from me?

,You can literally just say, Hey, I want to work with you. What do you need from me?,Yeah. Hey, I need a new landing page for this client.,What do you need for me to say the content? Yeah. And it'll ask, I need this information first.,I'm trying it right now. For a new client.,Um, it might take a minute to get all that stuff in there. So, um, but, um, cool. Well then, um, moving on quick note on the read AI Jordan mentioned already, it's required on all client meetings. So just make sure that it joins. Um, I don't think it joins like impromptu meetings that aren't on your schedule. So if you need to, if you need to, you can just open up, read AI and add to live meeting, paste the meeting link right there.

 And then it'll join. I have a question.,Like, how can we make sure that it's, that it's, that it has joined because it has joined all my meetings yesterday, but it doesn't show like it, it doesn't show like, oh, it's here, you know?,So one thing I discovered, which is new, I didn't realize, but whoever created the call, it's going to invite one note taker, and then it'll share it with anyone that's on the team. So in other words, every person's note taker doesn't need to show up to the same call. Should already be doing it. Like, for example, right now, none of you guys note takers are here with is already, you know what I mean?

,So it's not gonna send more note takers, it only needs one. And I'm seeing that, for example, there was a meeting that it didn't show up to, which was a meeting that I did with Gino from Grada.,I thought it was there and it didn't record it.,Is it possible you used a different email to book the call?,Maybe it's my work email and also the new so now I'm realizing also the new port. I had one on Monday I thought it was working because it recorded the grata like for the grata Did you accept it into the call? Yes.,Well, it didn't say anything like no taker it didn't know taker is is Sam on there is someone else on a the call that is the meeting owner? No.,So well, the one from Newport actually, the owner is is Trevor, but he didn't show up to this week's meeting because he only shows up every two weeks. Did his meeting?,Try to do his note taker try to join?,Honestly, I think I didn't pay attention because I didn't I didn't know this by then. But then for example, the one with me and Gino that I did want it to have record because I did need to prove that I've explained everything to him that I recorded and I'm the organizer, but it didn't request,me to take the note taker in. Okay, if it doesn't try to join within like, you can also go to your account.,There's a calendar tab on the left side over there.,Yeah.,You can actually toggled over to read Mitch. Yeah, the one that makes you see how you can say add read, as long as that's toggled green, it's going to show up for that call and try to get in. Let me go again. I don't know what flexible means.,But yeah, I was looking at that earlier to allow read to reschedule for the optimal time as your calendar changes, read focus time, periods of positive engagement, and historical meeting duration. So I would just leave that off for now.,Meeting that has already... Yeah, you got reports.,So like this one is gonna show up for me and shared with me because it's Jordan's note-taker and not mine, but it will show up here.,Yeah, no, no, I'm trying to see like if, no, on the calendar to see if it here like the same many that we were seen and say enable to see if it was with the genome one, but I can,do it. I would see it here and I don't. But if the note taker isn't present, like Jordan's is present right now, then it's not there.,For example, Trevor is the owner of this Monday Newport Beach recovery center meeting, but he doesn't show up to all of them. If he doesn't show, I have to admit Trevor's because he is the owner, right?,Always keep that in mind. Yeah. Okay.,Probably better also, like whoever's actually running the call regularly to be the person managing the calendar invite. Yeah. Recommend keeping that regimen or that process. For sure.,That's a good point. So like when we set up these Weekly Syncs, if like an associate director is in the meeting, the account manager should be the organizer. And you can change if you're in the meeting and it's, I know there's a way, well, this isn't my meeting, so I can't change it, but,Yeah, I'm gonna ask Trevor to give it to, because at the end, I'm the one that shows up every week and not have.,Yeah, I try to do that too, cause also like, if you need to change the call or reschedule it last minute, you can't do it. Cause like someone else owns the invite and like, it's just better whoever the main POC is should be the person running it.,Google should have the option to have multiple organizers.,Yeah.,I always try and transfer the ownership to you guys if I do initially make it.,Yeah. Um, cool. Yeah.,And then let's run through the, agendas real quick.,Yeah. So, um, we want to have all our calls, um, have like a good flow and a good result. Um, and we, you guys do a really good job. We do a really good job of that. Um, but we want to have something a bit more structured. Um, so that, um, there is a similarity working between account managers and, of course, onboarding new account managers and other things. We just want to have something structured.

 So let me pull up the meeting agenda. So it has essentially five sections, previous action items and updates. Is the first. So, yeah, it has five parts, previous action items and updates, performance overview, issues and challenges, strategic planning, and then next steps and action items. So, when you start the call, the first things you want to talk about are obviously, yeah, reviewing your for my last meeting.

 So whatever they may be, and by the way, Read is going to do really good at giving you action items. You should show them real quick. This is going to be sick. Recommendations, right? So here's an action item for me. So it goes through all these different meetings.,Actually, you can go to the last call. So just go to like a report. From your last call with the client and then just yeah like I don't know whatever you can just go in and it'll give you the action items and you can literally copy paste them right in this is a good,example because I was noticing that it's sometimes confusing whose actions items they are yeah this outlines it it doesn't like it's saying like brandon has my action items or like vice versa like it's not yeah the accurate of whose,action items whose yeah I got it Yesterday too, when I did an interview, it was like, I was just telling her, oh, like these would be the next steps. And then the action items was saying, like, I'm going to reach out to her for the second interview. So like, it was just inaccurate.,No, that's very true. It's not always going to, sometimes it puts in action items that aren't really an action item. So like, it's going to take your own editing, but at least you don't have to keep it in your brain. You can go here and grab the things. It may not be the right person, but you can, at least you don't have to remember it. You can just go here, grab them, edit them, and drop them in.

,And to build on that, it does link, it has a video recording. So you can go through and watch that video clip and being like, oh yeah, this is okay. This is what I said. You know what I mean?,That's another question I have, but Fabi, you go first. Oh, sorry.,I just wanted to ask real quick. So for example, if we copy and paste, let's say this auction items, cause you can copy. So that you can literally just copy, which is amazing. Right there, do you see? You have a little thing to copy, great. And we pasted on that agenda that you're gonna show up right now. Is that agenda, can we show it to the client? Sometimes I'm sharing my screen and I have to take notes and they're seeing what I'm taking notes, but I know that sometimes they're not completely happy.

,Not- I'll jump in, Mitch, to answer this one. The idea behind this agenda is that you actually send it to them, you prepare the agenda, and you send it to them prior to the call, at least 30 minutes in advance, ideally, like, further, if possible, send it to them so they're ready for the call. And then you do the call and you're screen sharing the agenda and you're discussing each item on the call.

,Okay, sending an email. Okay, okay. Why is that harder? What do you mean?,Well, it's just sometimes for example, we jump from another call to another so I say this could be something that's prepared a day in advance and schedule the email, you know, I mean like It's all you have to work on this 30 minutes for the call It's just like the idea is to get it to them beforehand.,So they know what we're gonna be meeting about Why don't we turn it into a Claude project so that? You guys can have a meeting and you can literally talk into it. You could go over the account on your, um, like weekly optimized things. And as you're going through it, type into the cloud project so that you have key metrics to go over. Um, and you can just go through and make notes about this and then this can spit out your, do that in a phase two.

,We still have a bunch of stuff like this that we want to build out to help you guys.,We want to make it easy and not take a bunch of time, but we just want to have something structured. Yeah, totally. Can we start with just using it, et cetera, and move eventually towards that of the Claude thing?,Yeah, that's what I was saying. Don't worry about Claude for now. That's going to be future. He was just coming up with an idea. That was impromptu. Right now, the main goal is that everyone's using the same agenda format. The calls are flowing the same. It can be quick and easy. The client knows what to expect. They already know what you're going to discuss before you get on the call because they have the agenda.

 You're screen sharing it on the call and discussing each item, crossing it out and just creating consistency. That's the main goal.,And the meeting agenda is going to be a different for each because I see that it says date on the top. Is it going to be a different document each time or is it okay? It wouldn't be easier to like have it per tab per dates. You can do that.,Copy and paste a single document. That's a really good idea. Yeah. Yeah. You duplicate this template. That's the running agenda has a date and you can even do folders.,Cause that's how I have them. I have per month and on each month on the folder, I have each tab that I have the meeting.,That was a great idea, Fabi. Good job. For sure. Love it. So, yeah, add a new tab for each month and then they can always go back and reference the past months and whatever. And that'll be great. This is really going to help because it's going to help the client be on a flow. You know, there's no like word of mouth and memory and who said what and like all this kind of stuff. It's on paper. There's a running list.

 You know, they know what's going on. Everyone's on the same page. Kind of eliminate a lot of confusion. That's really gonna help out with Grada. Nice. All right, cool. And then where can they find this, Mitch?,Is this in, where is this gonna live? It should be in the, yeah, reports would be a good place. Cool. Oops. Also, when you first introduce this with the client, make sure they understand that this is going to be the structure moving forward.,I think it's good to educate them and be like, hey, we're rolling out some new systems in 2025. This is our new meeting agenda. We think it's really going to help streamline the meetings and help you get all the information you need And so if you don't mind, we can follow this, you know, for our first call or whatever.,All right, so this part, yeah, just make sure you add the action items in their status updates, performance overview. So this is where you will dive into, you know, talking about our, you know, with addiction treatment service clients, viable opportunities, viable VOBs, you know, and VOBs and all those different metrics, typically like being like top level and not going into like the nitty gritty details.

 But yeah, explain what's been going on in the past week, um, or past month. And, um, you know, hopefully it's in line with the, uh, NSMs and goals that we've set. Um, and I wouldn't go very far into crazy detail. Um, yeah, we just, you don't want to dive too deeply too quick. Um, Obviously, a client, this is, you know, this is not going to be a monologue. This is going to be like a human interaction.

 So they might, you know, ask questions and certain things. If they ask you a question, don't dive super, super deep, you know, think of like a concise answer. And then if they, you know, pick your brain like I did as a kid and go, why, you know, then you can start diving in a bit, but don't go haywire on getting super deep too quickly. Let the client ask you questions. Are you guys doing more weekly calls with clients or monthly?

,What's the regimen right now? We're weekly. Yeah. Weekly. Okay. So I had made this monthly, but we need to change that to say weekly on the top.,Yeah. I think there should be usually what I do. Is, you know, we have our calls throughout the week. And then whatever meeting comes out after like the close of the month, you're going to review the month and see like how we did for that month.,Go ahead, Sam. For since we do meet so frequently, sometimes we don't have issues or challenges or like of these might not be needed or necessary, can we remove them from the agenda?,I would just put NA. I would just put NA. No issues. No. That way the client understands there's a space for it, but that there's nothing going on.,Yeah. OK. I just, the only thing that I see is like, for notable wins and achievements, if it's week over week, know, and we might not have something to mention there.,I don't want them to be like, Oh, is this a bad thing that we don't have, like, you know, when week over week, what we could do, maybe a weekly agenda would be more appropriate, like we would have a weekly and then this could be the monthly because this one's a little bit more comprehensive.,Yeah, I think this would be great for the monthly one for sure.,Why don't we keep this for monthly and then Sam, could you work on a weekly version, just duplicate this and create a weekly agenda version that that you think would be more appropriate?,Okay, cool. That'd be awesome. I actually, I mean, yeah, I agree. We should have something a little bit different, but during the week we might have notable wins. And even if we didn't crush it on viable VOVs or whatever, there should be something to highlight, ideally, And I know that's not always true. But the positive side is it can only get better.,Just kidding.,For example, we want to be positive with the client, right?,Yeah. A positive thing, for example, right now, Create didn't have any admins last month, only one admin last month.,But the positive thing today will be like, hey, we're building like, we built this beautiful new landing page for you guys. And I know they love it. And we already have Finally we have pictures of your facility and it matches completely what we want and we're gonna be using this so we can finally taught a target Full California that you wanted stuff like that, you know that for them. Yeah is a win.

,I Mean, let's see totally disagree Sam. I feel like Why don't we just try this for the weeklies and it ends up if it ends up being like just way too many things like we could adjust but maybe we try I Just want to say again.,This is I don't like want to be too free to call it like a loose structure because I want you to Abide by it, but it is it is a human interaction. So we're having a conversation, right?,So it's not gonna be hey We need to hit this bullet point this bit like it's you know, you're gonna stay in the flow of it It's just kind of ideas The one thing I don't see on there that I talk about all the time with clients on calls is like when we go over specific cases So like I'll have quest on a call know like what's up with this viable VOB and like they'll be talking to the people answer the calls and their admissions team will be on it.

 So like any back and forth with the admissions team and like about specific cases, I would probably throw in there. But yeah, other than that, I think it's really good.,Yeah. Yeah.,Like lead, lead review or something. Yeah. Something like that. Yeah.,Even at the end, I would say that we should leave that at the end.,Cause usually that's what takes us more time. Cause most of the clients are like, Oh wait, let me check. I have to go through DAS's or wait, let me check. I need to go through this or ask this person, stuff like that. I think that usually takes a lot of time and it's not gonna be enough within the 10 minutes that we have there.,Yeah And also those little time markers are just like you can change those But yeah, if you need to add a bullet point please do like this isn't The idea is that this should grow not shrink. Like if you need to add stuff to it, that's fine and then if something doesn't apply that's on here just put not applicable like just But as like, we don't have any updates for that this week, or there's no,optimizations right now or whatever.,You know what I mean? OK, cool. Let's do the one pager. I know we've got 15 minutes left.,And then, Liam, too. Do you want to hit on that, Mitch? Yep. Yeah, I guess we can review that again later.,Cool.,Oh, like, did you want to go through every part of it? Sorry, what were you suggesting? Oh, no, I didn't mean to interrupt if you wanted to go through the rest of that sheet.,I thought we were done. Well, yeah, we made it like 20%, 25% of the way through. I'll make it quick, though. Budget pacing and spend analysis. There's, with like, especially conversion value bidding. The campaign overspends and underspends. So if there is a high overspend, you might want to keep them aware that it did overspend recently. So we might go through an underspend period and calls might slow down.

 The reason I say this is because when things do slow down, clients tend to panic and this varies but they, you know, they might hit us up. So being proactive about this does help with, you know, this depends on client to client, but anyways. So this doesn't need to be a huge point, but it should be something that you have an eye on. No burdens and achievements. This should be kind of, in line with any recent optimization efforts that you have made, hopefully.

 And so like if we made it a change, how has it affected things? So these two can be kind of overlapping heavily. So yeah, highlight wins. What is our optimization efforts done? How have they affected us? And then that brings you down to issues and challenges. Of what we're doing. We have a goal in mind. Are we facing a problem or challenge? And then what is the solution to it? We wanna be solution orientated and have solutions to problems or potential problems that arise.

 Go ahead, Fabi. I have a quick question.,For example, in the, well, there are two, in the optimization one, I'm just a little bit concerned that, for example, if we haven't made, if it's going to be also like weekly, if we haven't made any big changes within the past week, and if we apply the, does not apply there, the client's going to think like, are you doing nothing? You know, but it's actually just because sometimes we make changes that they need to be, we need to give them time.

 And we haven't seen the result yet almost immediately. Or for example, a small result can also be like, Oh, our CTR increase in our cost per click decrease because we did this and we have a high, it's an example, we have a higher quality score and the ads seem to be working better or stuff like that. But it's something that it was probably done and they're aware of it from the meeting before, but this week we haven't done it, you know.

,That should come down to challenges because the challenge that you face is waiting for the appropriate amount of data to come in and for one, the campaign to optimize and too, for you to see if a change that you made is actually going to work. So we don't want it to make it seem like we're not doing anything. We want to be this data-driven strategy, both for our eyes, but also for the campaigns. So that just needs to be emphasized to the client that if we're changing things all willy-nilly, it's gonna work against them.

 So our solution is to be patient sometimes. We've made the right decisions based on the right data that we've seen and we need to make them confident in us that we've made the right decisions.,Okay.,Cool. Just the last one, is it okay, like for example, there has been a challenge that has been there twice, like in a week, like, sorry, twice, like, sorry. One week is the same challenge as the other one, like within two weeks in a row. For example, I don't know, let's say, hey, we still haven't gotten your ads disapproved because of this or stuff like that, you know, sometimes things that happen.

,Well, we have a solution you should have made progress with it within the action items. So, yeah, if there's a problem, you should have done something about it.,Yeah, I think something, when it comes to the issues and challenges, I always try to make the issues, try to pad them as much as you can, you know, like say the ads weren't approved yet and it's been two weeks or whatever, like figure out a way to word it better, like just be like, Yeah. Ads aren't approved, but we know they're going to get approved soon, or we assume they're going to be approved soon.

 I'll keep you updated.,I'm going to email you the second they're approved.,Yeah.,From Google. They said they were working on it, you know, just yeah. Make it seem like you're almost giving them a solution with the, with the issue, you know, even if it's kind of like, whatever, out of your control.,Yep. Um, Strategic planning, this can come into, you know, how much data do we have to move on to the next step of, you know, removing lead as a primary action, switching to max conversion value, and other things. So you guys are great, and you guys spot opportunities and optimizations all the time, so you should be able to get this down. And then next steps and action items, Um, which is going to bring you back to the, you know, beginning of the next meeting.

 Um, so, uh, if you have a new landing page you're working on new ads, um, tell them that. And then, um, the next meeting you'll say, Hey, this is what happened with those action items. So, um, but we can move on, um, to the startups, um, and how we're going to start accounts mentioned that we're not going to just say, hey, this is going to take, we're going to build out everything in a week, your ads will be launched.

 And then, like, it's not even made clear that the campaign is not going to deliver for the week and people are upset. So anyways, this structure is going to make it really clear to the client, what's happening during what week. We also want to have this visible to the client so that they know where they're at. And you might want to have it up on your call as your sharing screen and literally checking things off so that they know where we're at.

 So this would be another thing that you would copy and have in your Slack channel, easily accessible. Perhaps I'll add it to Like a session buddy, this should be something that you have ready. Let's just go week by week. So yeah, kickoff meeting, team meeting, intro, an engagement, getting access to all the accounts, receive customer data, that would be like a paid media discovery questionnaire, right?

 Goal setting, and this is kind of expectation-ish, but, you know, okay, we're gonna build out everything. This is how long it's gonna take. And, you know, we're, here's our goal. We're not gonna, we're likely not the first month of ads running, we need to gather data. But once we get everything going, this is where we want to be. We might need to do a Google Ads audit if they already have an account going and it's a campaign we can work with so that we can identify low-hanging fruit, quick wins, what we're going to do early on to improve their account in the quickest manner.

 Development is going to be different client to client. You can think of this as essentially, TAM is Total Adjustable Market. So if we're to build out a search campaign, we might want to know the search volume is for a given query, you know, like our, like, what's the search volume going to be? How much can we spend on these keywords, essentially? So it's, it's that sort of stuff. We also did TAM development with, Keaton, remind me of the, Ausar.

 We're doing like business to business stuff. We built out an audience to see what was appropriate to target for them in their total addressable market. I want to have the date ranges here. I skipped over that, but if we're starting a client on the 13th, this could be the 12th through the 18th, kind of like how we have performance tracking sheets. This is what we're going home uh first weekly sync and is someone trying to talk I hear like a mic tap no okay uh first weekly sync um this would be essentially status updates uh we have a month to build everything out right um or a month to get things launched um and so this is just status updates essentially uh where are we on the action items that we've mentioned.

 This and by week two should have completed the TAM development and our keyword research which again is kind of overlapping there. Getting started on landing page design with the type form, which I realized we didn't get into, and we need to. So anyways, goal setting, build campaigns and review week four, final out approval, setting expectations, how long it's going to take for things to deliver, how long it's going to take things to optimize, and actually launching the campaign.

 And then week five, essentially just ensuring we're on track, might not have any results, but just seeing how things are going. And week six is similar. We may have some adjustments based on really early data points and etc. So, um, but yeah, I realized we didn't go over type form. So I was gonna add on top of that about this doc.,This is meant to be really a client you managing yourself off of it. This is literally for the client. It's for them to have a visual. So every time you're meeting with them each week, they can see the progression of what's happening over that first five or six weeks. And, um, some of this stuff may be delayed. You just don't check it off until it's done. And it's okay if you're on week four, but some couple check items from week two or three are unchecked.

 It's okay. It just means like they're seeing the progression overall of what's happening. They should have this doc, like you email it to them. You could include it in the repeating weekly calendar invites. So they always have access to it and you'll screen share it during that first 60 days. And you'll walk through it with them and explain what's happening. And then once the 60 day sprint is over, that's when you'll start to use the regular client agenda.

 And that's what we showed you earlier. So starts with the 60 day launch phase. You're gonna go through this, share it with them.,Then you go into the regular agenda. Does it start like, can you scroll up? Let me just start real quick. Should it start immediately after the, like the week one? Is it gonna, let's say, start running or start counting after the kickoff meeting, let's say?,Yeah, it's like week zero, week one.,Yeah, no, because I'm just asking Chris, for example, with Laguna Shorts, They have been contacted since last week, um, which would be like first week But they just finally like answer it as and we're going to have the first kickoff call next tuesday So when is it going to be but they sign the first? You know what? I mean? So when does this actually start after the kickoff after design?,You know, can I share some thoughts mitch? Um technically when we send them the sow it should include a link to book a call, their kickoff call. And it should be like right away, you know, but that's something we could probably work on in our processes.,But- We do. Kim, I believe Kim does, but they didn't respond for a week or so. So they're just ghosting you. Yeah. They were out of town and then we had to get Preston to call them and then they responded, Oh, sorry. I was in Colorado. Like, Oh, let's get to it. So.,What do you guys think is the best route? Cause I mean, on one point they're paying. So like we're on a- on a pay timeline, but at the same time, we're not really starting until we have that call.,So what do you guys think?,Yeah, I think we'll just have to adjust it as it happens. Okay. Because for example, what did Kim say to me is that they have signed but they're not paying yet. So maybe it could be like once they officially have start paying. Yeah. Could be instead of like signing.,I think Sam's right. It's just gonna have to flux a bit. Yeah. But what I would say is make sure you enter the actual date ranges there next to each week so that they can see a nice breakdown for whenever it does kick off.,Okay.,So yeah. Should we add there the kickoff or is that like the team in current engagement review? Yeah, that's what that is, yeah.,You can call it, you can rename it if you want. I don't really care. A lot of this stuff, I'm sure we're going to find ways to improve on. So like, don't look at this as like set in stone.,Yeah. That's a great starting point though.,Yeah.,I think just like, like we just did with the kickoff, just making sure that like, for example, they receive customer data, maybe like the same, we can do like two points and be like the PPC questionnaire filled out by client or something, you know, right now it's going to be reminded. But when you ask me like, what is the cost?,Yeah.,Is it like, there could other little things that you need to actually add in here too that are happening because it's good for the client to know like, wow, they're doing a lot of work, you know? So like, if there's other things to add in, please do. This was me just literally slamming it out really fast and just trying to get something on paper. So like, feel free to add to it, adjust, but definitely follow this framework.

,Yeah. Like maybe we could add just like tiny, like under, we could add a little more, for example, on the access accounts, we can just be like, make sure the list of what we need, like Google ads, analytics, that, that, that.,Oh, like you can check off each one. You mean?,That could be good. Yeah. Because that way, kind of like what Sam did with the pre kickoff, she did a checklist that I think it was pretty good. Maybe we could just add some stuff from there.,Yeah.,Okay, does anyone need to get on a client car, you know good I do Maybe you should send a limb later.,I don't want to keep you from Why don't we do it on Friday on our team?,I mean if you guys don't like it's pretty pretty quick I this is the type form Jordan I'm sorry would you mind like just reviewing it quickly I and so I can get on this team challenge I guess I'm stoked that we're getting all these things done you have more time and that things should be able to be built out quicker and then this last piece is Just so we don't miss anything on design requests, so things don't get lost in the build outs.

 So yeah, this should make everything a lot better for everyone involved. But anyways, talk to you guys later. Thank you, Mitch.,All right, I'll just show you this type form real quick. It's honestly pretty straightforward. Straightforward. Let me screen share.,All right.,So this, we built out a megatype form that applies for any kind of project you could ever want to do. With the design department. And it's pretty cool. So basically, it starts out, it's going to ask you what your name is, what kind of project you're trying to do, is it a new project, is it a revision, etc. If it's a revision, it's going to take you on a more simple route, basically to just get the revision data of like, what is the Asana task ID that you're trying to revise.

 So if it's a project they've already done, and say it's a landing page or an ad creative, and you just want something changed, like copy or whatever, you're going to do a revision project. You're going to input the task ID from whenever that initial project happened. And then you're going to provide the details of your revision notes. And then it's going to ask you, when is your hard deadline? And hard deadline means it has to go live.

 I need this back by this date. You want to include, and then that's it. If it is a new project, it's going to ask you the client name, client website, any logos, colors, fonts, et cetera, the client's discovery questionnaire. If anything is not applicable, just type NA in the response. You don't have to respond, but every question is required that you respond something. But if it isn't available, or you can't do it, just put NA.

 I will note, though, if it's something that the design department will need, and they can't really do this project without that, don't complete the type form. Get all your ducks in a row before you fill this out. So if it's a question that you should be able to answer, but you just can't answer it, you may just need to wait before you submit this. So it's going to ask you, what type of design project is it Is it an ad creative?

 Is it a meta ad or is it a Google ad? So then it's going to, if it's a landing page, for example, it's going to ask you questions like what's the topic of the landing page? What's the domain or sub domain? What do you want the title and description to be? What are the service areas being targeted? What services or products are you highlighting? What is the goal of the landing page? Google doc with the actual landing page copy.

 And this is where that cloud project comes in with your, Uh, landing page copy, remember? So you're going to put that in a Google doc, put that in the response, the exact URL that you want the landing page to be published to the swap target phone number, the client's DNS records, where are they located? Account name, blah, blah, blah. It's going to ask all these questions.,It's going to ask you replacing the existing like LP request task in Asana.,Yes.,Okay.,Currently we're tasking, like the design told us they don't have capacity for any landing pages. We've been using Fiverr. So is there that process built into this as well? Or is this just if they were to build out the landing pages for us?,If they were to, and I'm also hiring a landing page designer right now and they should be hired in the next like weeks. So yeah, it might take like two weeks, but we are going to have that person and then you can start to use this. Awesome. Okay. It'll ask you if you need a form on the landing page, where is it going to be sent to? What are the questions? It's target audience. You'll notice questions like, what is the preliminary V1 deadline?

 And that's like, in other words, when do you need to review this by so you can be ready for revisions and have time to make revisions before a hard deadline right here. That's amazing. So that's going to help a lot. And then say you don't want a landing page. Oh, I want a meta ad or a Google ad, it's going to take you down a different path to here. If it's meta, it's going to say, or Google, they're both the same thing.

 It's just different. They're the same questions, just different applications. So topic, goal, select all the dimensions that you need. Google doc outlining the exact copy. Again, that's where your cloud project comes in to create all the copy. And you're going to put that in a Google doc. And then paste the link to the Google Doc here, always ensuring that it's publicly accessible for the design team to access.

 How many total ad creatives are you requesting? What's the target audience, preliminary V1 deadline, hard deadline, additional notes, things like that. And so yeah, this type form should technically be able to route you through any design requests. And if it doesn't have an input or something like that? Like, let me know so we can make it optimal.,I have a question. Well, two questions over there. First for the logos and stuff like that. Usually what what design does is that the date they take the logos from the client's website? Or do you think should we should be asking the logos directly from the client since we start the like the onboarding process with them? Because what they usually do is we just give the design a client we give them in the website and they take it out of there.

,Yeah.,So if you don't have access to anything, then just put N a, if you do have access, put it all on a Google drive. So if you can download it off the website, you can pull it from wherever, put them into a Google drive file and then share the Google drive file link.,Yeah.,Maybe like this is Nick, by the way, is he gone? I think he had a meeting too. Oh, okay. Um, no, but what I mean is, so, We could just do, um, we could just do like basically a, um, a Google document with the link of the client and be like, take the logo from here, like download it,from here.,There's no problem with doing that.,Sorry. Yeah.,Like, um, no, no. So you said, can you go to the logo one from when building a new landing page? Yeah.,Nick doesn't have a meeting so I'll see if he's able to join us again.,Okay yeah I mean this is good for him to know because he's going to need to use it so. Here it says provide logos color codes and font names stuff like that. Usually what I mean is what you what we currently do is the design team already takes it away from their website. We don't give them that specific information so here could we just be instead of uploading those Take a google sheet and be like this is their client's website.

 Take it from here.,You could literally just paste whatever you want here. It's just a short answer so you can Provide their website. You can put in a description. You can tell give them instructions.,You can do whatever you want Okay And the last one for the ads when you said like also google doc Can we do the same with a single document with the dates and the name of the ads in the same google doc? So we don't have multiple documents and it's like I would say messy just maybe like this here where it says provide a google doc outlining the exact copy of that ad yeah and what's your question can we do can we do like um because we request sometimes for example um at least for an air star we request that I think I know they're going to be gone but for example now that we're running facebook ads for some clients we're probably going to be requesting monthly ads um But you know, we will end up having 12 or I don't know how many documents if we do it.

 Can we do a single document and just place the dates? Do like tabs with the dates and the copy?,Sure. Yeah. I mean, if I'm understanding correctly, I think that's fine with me.,Sam, do you have any thoughts on that? No, that sounds great. My only kind of feedback on this is as far as the design elements, I'm really hoping that the design team, especially if we're going to hire someone, can really, we've been helping them a lot with getting everything for them, then all they have to do is just the design part. But I'm really hoping that they could, especially with this new hire, kind of step up and help us out more.

 So in regards to, for example, the one step that says provide font colors, logos, they can grab all of that easily themselves.,So do we know the reason I put this is because when we onboard we should technically be asking them for the brand deck, right?,We don't, they, usually the treatment centers don't have any of it. So we just grab it from their website, but like finding the colors and logos. So just as one example, I would like to meet with you later to kind of discuss like the cross-functional aspect of our teams. But yeah, I'm really hoping that with this new hire, they'll be able to help us out with a lot of these design web aspects.,No, we definitely could. The only reason I'm putting it here is if you have it. If you don't have it, just don't put anything. Just put anything.,Yeah, because we do have them a lot of times.,You would just literally type in, like, pull from client website. Here's the link.,As long as that's okay for them, if they know that. Because a lot of times they'll be like, oh, where is this? I need this to get started. And it's like, well, you can also grab it. It does help us out a lot. Everything else needed to build out a landing page when, you know, our focus would be paid media. But yeah, that's great. We'll do that.,I would say the best response is just type in and say, uh, assets will need to be pulled from website. Here's their website URL. Okay. Perfect. And then they, they understand that that's what you're looking for. Okay, cool. Is Nick running again or is he out?,Let me see what he, he said, shoot. I had to jump on a call with NBCG because I'm out tomorrow.,Okay.,I didn't see that on his calendar, but he he had to call all good If he's confused on anything, I'm sure you guys can help him out So, all right, cool. Well, I appreciate all your time.,Sorry it went long and Thank you definitely there's an open feedback loop so if you're running into issues bugs, whatever just let me know or let Mitch know either way Yeah do you think it's like the learning phase for this implemented? Because there's so many changes? Like, how long would you give it till we have it smoothly running? Because I'm the type of person who panics and I want to do everything by the book.

 And I'm going to be like stress already because we have a zero tolerance policy. And if you screw up any of this, I'm just joking. No, because I'm gonna like I'm gonna try to use all of this new process for Laguna shorts, you know, but at the same time, I saw that I just was handling new clients.,So What I can do is I have this bullet list of basically all the things that we talked about today. And what I would recommend is just I'll send it in the paid media channel. And I would just recommend pinning that or trying to remind yourself and just spending time working on all those things and hopefully you can integrate it. And when we get Laurent going and get the notion going that's gonna help a lot with where you can find all that stuff, but,Yeah, because I'm gonna try to like, at least I'm gonna try to do it by this, you know. Yeah. And maybe on this one I can ask questions and stuff like that. And maybe on the second client, it's gonna be easier for me to handle it by myself, you know.,Yeah, there's gonna be a little bit of a flow. I'm sure it'll take you two or three calls before you're used to what you wanna have in the agendas and how you're gonna use it and everything. Definitely try to abide by as close as you can, because it is a good structure. We thought through it a lot. We really tried to make sure it's good. But yeah, I'm sure it'll take you a few calls. It's no big deal.

 I think it's more simple, all the stuff that we went over. It's just as complex because we went so deep into each thing. But it's really just Cloud. There's three Cloud projects. So using those, add copy, landing pages, and media guru. So that's pretty straightforward. There's using the type form if you need a design project. There's using read, which you're already doing. You don't have to think about that.

 And then using the two agendas. So the 60-day launch for a new client and the regular running agenda. Other than that, that's it.,That's all we went over today. I'm mostly talking about the two agendas. And I guess they're going to be added to the template, Sam, to like the Facebook Google Ads template. So I'm just going to delete the existing one in Laguna Shorts and redo it with that one.,OK, yeah, I think you can only archive, but that works.,Okay.,The only thing is that, um, it also is going to be based on if the clients or if the sales team is onboarding them with the understanding that it is a month build out. Okay. Because sometimes we get those one-offs where it's like, Oh, it's sooner.,I just, yeah. Well, I can ask Sam. I can ask him.,We'll confirm that Laguna shores for sure is on that one month.,Okay. Sounds good.,Yeah. So yeah, it's really, just those two agendas one is for kickoffs one is for ongoing and for the ongoing one the main thing I really want to want you to do is send it to them at some point I don't care if it's two days in advance they just need to get it in advance so that they can like know what we're gonna do it shows that we're on our shit is what it is when a client receives an agenda in advance they're like whoa these guys are on it and then screen sharing it on the call and walking through it that's all you know and then making sure they have access to it so that's really yet.

,Thank you, Jordan. Cool. All right.,We'll see y'all later. Thank you. Thank you.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Will read thru this and get back to you by AM tomorrow

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm happy to add you! I was going to make it optional for you guys though since you are in a different time zone. I can invite you and the team with "optional" invitation if you like?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I'm happy to add you! I was going to make it optional for you guys though since you are in a different time zone. I can invite you and the team with "optional" invitation if you like?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: :tada:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: It's more focused on overarching company stuff

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool I'll add you and the team as optional.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I invited your whole team, you guys are free to join anytime but just let them know it's not mandatory

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: :slightly_smiling_face:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Be sure to let your team know that it is optional for them and not mandatory

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool I just sent out invites

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Some of this stuff I could use Jordan's help to populate like team/culture stuff

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: The weekly-all hands is setup, and I created an agenda . ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Wondering if we can do annual reviews and couch the new strategy into it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Have we had annual review calls with clients yet?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: so it's seamless

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: r.e deck above^

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can try to play around with some ideas

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Think "Apple" style messaging

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So they can grasp the ideas easily without reading a lot

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Leveraging more small one-liners an headers

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Was thinking just the amount of copy

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Did you see page 2?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: With sub-points specifically around nrr for each dept.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: What I could do is compress Business updates and Critical discussion into just NRR discussion

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: but we could just use it same for the weekly call

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Page 2 is for the monthlly financial focused call

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool, I refined it to focus primarily on NRR performance metrics and I shared it with dept. heads so they can populate it before each call.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you prefer it's in a slide deck or is doc ok?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just needs to get in there somehow

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok yeah I can do that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If possible yes

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can also help with it or we can get someone else to help

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: So I'll work on that for now

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Preston just asked me to do a slide deck instead of a doc

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: we'll get it figured out

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yep no problem

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: but agree a slide deck would be nice

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I did make the doc pretty plug and play

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: cool thanks

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Even if it's from something else is fine

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Just generic with already branding etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you have a deck I can use to create something?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: One of our checklist items was meetings between Asd's and Ams - that would essentially just be Sam in PPC, correct? I don't think there are any other asd's right now in seo etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Preston also asked me to setup weekly Departmental meetings. Is that something you already have in place with your team? If not I can help get that setup and design a format for you. Let me know what day/time would be best for your team as well.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Preston also asked me to setup weekly Departmental meetings. Is that something you already have in place with your team? If not I can help get that setup and design a format for you. Let me know what day/time would be best for your team as well.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Did you envision those being 1:1 type meetings or group meetings for each sub-group?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: 10-4

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Here's all we have so far:
Weekly All Hands
Dept. Head Sprint Call
Dept. Meetings
Asd/Am meetings
Dept. Head 1:1's
Cross departmental slack standup

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: To review goals and NSMs etc.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think he means an all-hands meeting for your department

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you follow any specific agenda?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok awesome, can you add me to that

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: (I say team lightly, since I know it's just you and Maria :slightly_smiling_face:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: And yeah I will be on them as well to support

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Morning Shannon! Preston also asked me to setup weekly Departmental meetings. Is that something you already have in place with your team? If not I can help get that setup and design a format for you. Let me know what day/time would be best for your team as well.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you have an agenda you use?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok cool, can you add me to the Monday one?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: ty!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I like these kinds of calls earlier in the week so nothing is forgotten over the weekend

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If we could do it on Tuesday it would be awesome

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: One thing Preston asked me to focus on in the meetings is client results and employee development. So lets think about that as we go forward and how we can implement in the call if not already doing so.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Cool sounds good.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: One thing Preston asked me to focus on in the meetings is client results and employee development. So lets think about that as we go forward and how we can implement in the call if not already doing so.

• Goal/NSM pacing update
• Pain point resolution
• Team/culture update
• Innovation discussions

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: • Goal/NSM pacing update
• Pain point resolution
• Team/culture update
• Innovation discussions

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Might help them too

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Can I share your swot example with mitch and shannon?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: i love it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: all good

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: we will as we move into the future

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Ok great

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: One thing Preston asked me to focus on in the meetings is client results and employee development. So lets think about that as we go forward and how we can implement in the call if not already doing so.

• Goal/NSM pacing update (you probably don't have this yet which is fine, but we can work towards it)
• Pain point resolution
• Team/culture update
• Innovation discussions

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I think we should have each person share their NSM's on the call each week

____________________________________________________________
CALL TRANSCRIPT:
Meeting Title: Jordan & Laurent - Weekly
Meeting Participants:Jordan Dahlquist,Laurent Matson
Start Time: 2025-01-09T10:06:28-08:00
End Time: 2025-01-09T11:02:47-08:00
Transcript: vocal cords and the headache wise.,Yeah.,But it looks pretty clear today, but I don't know. If you go inland a bit, or closer toward LA, it's really bad. I mean, it's like an apocalypse over there.,I've seen it. Yeah. Yeah. Are you safe?,Oh, yeah. I'm like, probably like 60 miles from the fire. So okay. Yep. Do you Not really, no. I mean, it's in like Hollywood Hills and Ventura and stuff like that. I don't really know anyone that lives up there personally.,OK. You don't know any celebrities? No.,Yeah.,Right on.,Yeah, totally, man.,Wow. All right. Yeah, well, let's dive into it. I don't know if we need the full hour today, but thanks for setting this up. This is a good time. I think moving forward. Yeah.,Cool.,So next week, I think I do have a weird little overlap actually. It's just like the only time, which I forgot to mention. Do you have like time next Thursday, like around this time that works for you?,Yeah, honestly, Thursday is like a weird day. That has like no meetings ever. So it's pretty much like we could book at any time right now.,Okay. What about like 12 p.m. 9 a.m. My time? I mean, 12 p.m. My time, 9 a.m. Your time. 9 a.m. My time?,Yeah, so it'd be before- I can do like 9.15, because I have an 8 a.m. To 9 call that goes like all the way up to nine o'clock. And I probably need to like, take a five minute break in between, but yeah, I can do it like 9, 15 to 10, 15 or 9, 15 to 10.,Yeah. So we can do that or we could do it like after this call and I'm free starting at like, uh, 2 30. So like 11 AM your time.,I mean, either one's fine, but 11 works too. Um, I mean, I do like to kind of get in and answer some emails in the morning, but like no big deal.,Let's do a later one. Then you want to do like starting at like 1130 a.m. Your time Sure, that works.,All right, perfect All right, I'll send an update All right.,Thank you All right Cool. Yeah, so got a few things to take a look at today and You know, I think the overall Idea here just to keep progressing and look at things on earth things, you know, we're not going to try to boil the ocean, get everything done in one meeting, but we'll just keep progressing. Yeah, absolutely. So let's take a look at my next step here as we'll take a look at the assets and stuff we're collecting up here.

 I have three director meetings next week, and I want to get a sense of who they were and what departments they're in. So Mitch I know is with Paid Media. What about Shannon?,Design.,Okay, and then what was the other guy's name? Is it Trevor or something? Yeah, Trevor Gage. He's SEO. All right, cool. He's on Friday with you, I believe.,Yeah, all right.,So he'll have some time to take a look at that. I'll email them today with like a quick kind of briefing with them to prep for that conversation. They're not long calls, but I think it's a good starter and that's fine. And I want to give them a little bit of upfront notice so they can review their product line here and just get a sense of like the way they see it, how it's constructed. Maybe they have their own documentation for this, but just get everything mapped out here.

 And then the second piece would be on the positioning that we'll probably spend more time on going through positioning for their department, which I can kind of guide them through, but hopefully they can take a stab at this before the meeting to get a sense of this. And that basically creates your capabilities deck, which is basically positioning plus services at like kind of a baseline level. We have those two things nailed down.

 We can then begin to build it out more fully.,One thing to note, is they're, they are so slammed this week. It's like absolutely painful. I mean, his calendar looks like the American flag right now. So just warning you, you know, he probably isn't going to have too much time to like prep a lot or do a ton, but he works crazy hard, but yeah, just warning you. All right. Well, that'll be good.,And this is why we're doing this, right? This is that. Really nails it because it's like, you, you always want your directors to kind of be able to do a few things at once. And the reality is they're probably like head deep in client and ops, you know, and, and just a lot.,Yeah. Like we're doing this eight week sprint, so I've got them on that kind of stuff. And there's a lot of new initiatives we're rolling out with Preston.,So, yeah. And I'm going to hopefully the, I mean, the work we're doing pretty much sits within the sprint, I would say. So ideally what I'm briefing them on everything supports them here, right? And that's what we talked about a little bit earlier in the week is the idea is that they kind of come into this moment with the week. I can help extract some of like this information from them and get them thinking about it.

 And then they can move on into the next week and it can kind of sit with us to develop and actually turn it into something. So that's kind of our focus here. All right, so to wrap up, on that. Shannon. She is the head of design. All right, and you think it'd be worth kind of I you know, I know, for this initiative, we talked about SEO and paid media. You think it's worth like, having her map out her this as well, like basically like her product line?

,Yeah, I mean, I think it's good. Um, we're going to need it. We need it. So I do think it's important.,Okay.,So let's add that in here. And that's the one that we want to convert into more of a CRO plus design, right? Yeah.,And we need to get it to where it's actually profitable too, which I'm kind of working on a little bit already, but yeah, it's kind of just an, um, malignant department that just sort of departments, but also doesn't support them. So it's really weird.,Yeah.,It definitely should be an add on price. You know, and I think that's where sometimes it gets incorporated into like a paid media fee, but obviously it, it, it really is an add on, but at the same time, like we need it because you know, creative and performance, especially on the, like the CRO front that yeah. That's the sabotage, a good paid media campaign anyway. So we do need that. Here's a question.

 Do you have a designer in-house or someone that does deck building or makes things nice?,Yeah, it's Kevin Hall.,OK.,Am I able to work with Kevin? And how do I get onto his radar with things to develop? Just Slack him or email him. Tell him what you need.,He does all the decks and everything.,Okay.,And he kind of, he says he's his own traffic studio kind of guy. Yep. Okay.,Just hit him up. You can see, see me if you want, but yeah, he's a cool guy and he'll get whatever you need.,All right. Yeah. Cause I'm, I, I like to think a couple of steps ahead with a couple of these areas. And I think I already have like a pretty good vision that I've seen work really well for design and CRO. Um, and I'm thinking maybe supply him with that outline and if If he could just put that into web serve branding, we'll have a pretty good head start on that vision, if that works for you.,Yeah, absolutely.,I think that's a great approach. OK, cool. What's his email? Is it kevin.hull at webserve?,It's probably just Kevin. Let me look.,All right.,Just kevin at webserve.io.,Cool.,He's got the Kevin locked down, so if another Kevin joins their show.,All right, cool. So I will email those folks. That was my first point.,I'll do that today. So they're set up a little bit for next week, looking ahead. Again, the whole idea is to support them for this Week 2 initiative for them. One ask for you is if you can update the template like you did the other document, just so they're in the same order, so the team doesn't get confused.,Oh, great point. I didn't even think about that.,Yep. I'll get that updated.,And they're currently working on this one here. Yeah, interested to see what they say. I mean, the analysis is kind of funny. Like, when I think of a SWOT analysis, like, we all probably have a different reference point. But like, they can be pretty robust with a lot of different, like, inputs. Is pretty simple. So like, no big lift for them, you know?,No, I'm trying not to scare them too much because they're already all freaking out. The positive side is I already saw Trevor's SWAT that he's building and it's like, on a spreadsheet, it's like really broken out nice. It's like very in depth. So his looks really good. So that's going to be good for SEO. And then I haven't actually talked to Mitch about it, but I'm going to check in with Mitch and Shannon today and see how things are going.

,What I will say there in like when you're working with like multiple execs like that, a nice thing to do is like, like you just did like identify the best example that's in development, and it might be just a function of being like, sweet, I'm stealing this and like now you equip Mitch with that. And now everyone's working off the same template, you know, Mitch could probably, he'd probably be psyched to use Trevor spreadsheet.

,Yeah.,Trevor right now to get the link to his thing. Yeah. And then you'd have it all uniform, which would be nice. So let me come down to service offerings. Yeah. Yeah, I mean, we'll cover some of this in the conversation we'll have. But OK, no real questions on that.,Let me add that reminder to myself to update that doc. One second here. All right, I'm back. Cool. Let's jump to assets for a quick second here.,And maybe let's just do a kind of a power run through.,So yeah, so I asked them, I shared this with them and asked them to start populating it. But okay, I think a lot of this just doesn't exist, to be honest. Yeah, that's my question.,And do you feel like, Yeah, I mean, part of the process is everyone probably has stuff. It's like, what do you have in your corner? Right? And so get everybody to populate the sheet.,So I'll follow up with them again on my call next week and try I like push that. Maybe I'll go through it even with them a bit, line by line, and be like, do we have this?,Do we have that? See what we can come up with. Like this one? I know Preston has it because he showed it to us on a call once.,He has the winning by design outline here. Yep. So that one. I'm pretty sure that was.,Directives. Directives, though. It's not even ours.,Right.,Well. Yeah.,I can check in on that and see. Yeah.,Yeah.,I mean, I have some versions of that too. Then if it's like just has nothing in it yet for web serve, but it would be good to get that in there. Yeah. Paid media proposal. By the way.,Yeah.,So Kevin is the guy that makes all this stuff. So if you were to hit up Kevin and one of your questions could be like, hey, can you fill this out? He has everything. He knows where everything lives. I think that would even be a better route than the directors.,I love that. Who designs the stuff? Has it blocked in? He is the missing link here. That's kind of true. OK. So SEO proposal, I think that was maybe a PDF I got. But we need the deck link in there.,Again, Kevin will have that. He's the mastermind. Perfect. I didn't think of that before.,Sorry. That's great.,That's great. I'm also still like, even getting my polls on WebSurf, because I've been here a month. So I'm kind of like, OK, who does all that?,I'm trying to get it all going. Well, this is going to help tremendously, because you'll just have everything in one central tab, ideally. And then we can be like, all right, what's weak? What's not? What do we want to build? We can add a prioritization column to this. Right now, it's just kind of documenting. Tip on this stuff, and this is just me more being obsessive when we're adding stuff is just to copy it in, and then click the shortcut, just because it comes up.

,Yeah, totally. Super clean.,Yeah, I can do that.,Onboarding this document This is our startup one pager that we just rolled out this week that we're going to start using. Yep. Onboarding deck. This is just, I didn't know where to put it in there.,I just. Yeah, no, this is useful. Um, um, yeah, this is kind of like strategy phase or project phase. What are we going to call it? Um, yeah. I think, I don't think I have that document on me. Um, yeah. So for like an onboarding doc, I like to create one that, that shows the handoff between sales and operations. And it's got kind of like everything in there from like the closed one in like email introduction and then like, all right, team sends email and then like Slack.

,I don't think we have that. That I know of, but you can ask Kevin. Right.,For sure. But yeah, that would be our first step.,Yep.,That's going to be awesome. Adding process stuff. So let's see, what else do we have here? Do we have any of these tracker documents for operations generally, like an NSM tracker or a churn?,We have an NSM one for PPC. See, which I could try and grab real quick. The issue is that it's really annoying, but someone else owns the doc. Let me see here. That's OK. We just want to get it all in here. I just shared it with you. It should go to your email.,OK.,And that's for paid.,Yep.,And then right now we don't even have it for SEO or design, but we want to get it built out.,It's just, we're in process on that. Yeah. It's tough to, okay, cool.,This is the direct, this is the one I built for directive.,Perfect.,And I think mostly it's pretty much up to date as of the last month, but beyond that, like, I don't think much is accurate.,Yep.,Yeah. That's sweet. I like this thing. Totally. It's like super, there's just a high level of account. Like when we introduced this man, we went from like, when I joined, we were like 33% NSM attainment. We went to like 70% like right away. And it was strictly because everything was accountable. Um, and then we could start like, just ask the right questions and be like, why are you like, there's just so much like waste and fat around it.

 And like once we got with it, it just like went way off. I can't wait.,I literally can't wait to get that fully rolling. Yeah.,But and then once it's so funny that like once we it's missing a couple areas, which are probably a good thing, but like when we got into it be like, Oh, well, this client just like move the goalposts and the goals changed. Okay, so we added like, like paused type thing. It's not like hit or missing. It's like, you know, yeah, in limbo, but then they stayed in limbo. For like three months, you know, like you can't just live in limbo.

 You have to like reset it with a client. So then we had to set like a date thing next to it. That was like that went to red after a week. It was like, all right, you have to update it. Add ons to like, the team are so slippery. Like they keep buying news to like, you know, because they're, they're so accountable for their stuff, but it kind of forces the function of being like, clients at like, you know, whatever That's why I don't know how we're going,to do this for SEO. And I'm hoping you have some insight, but it's so nuanced. And then even just the trust level, like for example, Trevor was telling me earlier this week that he doesn't even trust his team, that they're actually doing the work they need to be doing. Like for example, if they're supposed to go in and optimize a page or build a page around a specific topic, they're supposed to like build it.

 Resource page with like good data, comprehensive, useful information. And he was saying like sometimes, well, he has to check every single thing that they do. And he was saying, sometimes they'll just like read a dumb blog with chat GPT and it's like nothing. And I'm like, that is not good that you cannot trust your team to literally do their job. Like that's not a good place to be living in, you know?

 And so there's a lot of work to be done on the SEO side.,Yeah Yeah, it's like it's I think the first step and you kind of asked this in one of our first calls Which is like, how do you make the team like do stuff? Uh, which is like kind of like a general like change management and adoption question But first it's about being Like blameless as executives first to be like look like, you know This is where that services map is going to come in useful be like look these are like the 10 things we do This is like how you do them.

 That's all a notion There's like a loom video plus like a quick breakdown like you know what our expectation is that web serve for what like a sitemap or blog post outline or whatever it is looks like And then from an adoption framework there needs to be some level of like gatekeeping At least initially to make sure it's being done So that's tough if it's maybe just Trevor and then a team and he doesn't have that middle management layer yet because we're working on Yeah, that's exactly because that's gonna be on him somehow to like quality control that which is tough But you can do that once in a while.

 Like we have a client account tracker We know where the client folders are we should be able to dive in there any moment like look at those deliverables I had an idea for that.,I was like, what if we require them to Send you a 30-second loom video when they're done instead of you having to go find it and go look at it Like make them do the legwork If they did it, they send you a loom.,You can watch it on 2x speed, and you're done in 15 seconds. It's a great idea.,Are we doing QBRs right now for clients? I don't know, to be honest. I know we're doing annuals, but that's what we're actually working on right now. Example, with the SEO department, we're trying to roll out this new strategy with this offshore link building and PR team. And so we're trying to couch that in with their annual review. Yeah. And, um, yeah, there's just so much that needs to be done.

 It's kind of overwhelming. I'm trying to, you know, yeah, there is insane right now, but yeah. Yeah.,So, yeah, we'll go through this. Step by step. I think like in terms of parallel workflows, like I'll be spending a lot of time here over the next two to three weeks with the directors and the team and like trying to get this like locked in, which is obviously good from a sales perspective, but it's just more for like everyone to be on the same page with like, look, this is like what our services are, why they matter, how we do them, why they're different.

 Right. And it's kind of like that knowledge captured in that doc. So we can use it for onboarding. Training as well. In parallel with that, and obviously the marketing team can leverage that here. In parallel with that, we should be filling this out as we go and identifying, you know, gaps and opportunities that we can then kind of point the team to or be like, all right, this is what we need to do ASAP, versus other things.

 And, you know, eventually, it'll be diagrammed in here. But with ongoing, at a base level, we should have like, Yeah, we're gonna have a project phase or strategy presentation at the end of the 30 days. What does that look like, Monthly report, are we doing that? Or are we doing a QBR? That's usually a choice between like client MRR, like high value clients should get probably a monthly plus QBR. Just the QBR.

 But I do think every client should get a quarterly business review. So if we're not doing that, that's something we probably No, I agree. At some point.,I think we should be doing monthly and quarterly and annual and everything.,So. Agreed.,And there's a way to do that. Like the QBR is not as big of a lift if you're doing a nice job with the monthlies because the QBR is basically. Just recapping. Third monthly. You're adding a layer of like strategic recommendation and forward looking. And that's the side I always talk about. Like there's like, you know, strategy development. And like strategy execution, there's also client development, right?

 And I think that's the piece that web serve may be missing, especially if client retention is a problem, but like your job isn't just to like be a button pusher and be great at Google and LinkedIn ads, it's to retain and grow clients. And I think a QBR, if you're going to centralize a lot of like the client development function into one thing, it is the QBR because it's a force function to make sure that they are properly articulating the wins We've had the roadmap of looking right.

 And by the way, a lot of the work we've done to date, like should be very visual there. Like all the blog posts, like each unit should be on a slot, whatever. Right. And now Trevor should be able to jump in and look at a QBR tracker and look at them, be like, sweet. Like that looks like our products. Right. Or another one where it's like, that doesn't look like our product. Um, and again, it's a big team enablement area.

 Cause we should develop that QBR eventually. That's like, this is what good looks like, maybe February 2025. We do a round of them. We'll look at them in May and be like, holy shit, these two are awesome. These are our new master templates. And by that way, we let the team continually improve the product over the course of the year. So there's a way to do that right.,And we'll get there.,But yeah, that's important. So for these, I'll reach out to Kevin.,Anything else, you know, drop it in here. You would be, uh, so w one. Oh yeah. That could be, um, you can email Kim at web serve and she manages like, you know, most of the SOWs. So she could give you one or two examples or whatever, or if she has a template, great. That's all. I don't know what that, what do you mean by that? Like, I don't know what that, what do you mean by that? I don't know what that, what do you mean by that?

 What like for when they're onboarding Yeah, and for sales like it's it's kind of like we might not have that it's going to actually kevin kind of has that actually Okay, definitely and then icp and persona you got that messaging I Know preston knows he needs to work on that. He just probably isn't going to do that this week or next week But maybe I'll keep pushing him. Um, yep case studies kevin will have anything that's available there And I know we have a few for sure.

 Onboarding, all we have that I am aware of is that startup one pager. But I would ask Kevin, you know, in platform skills, I don't know, what do you what is that exactly?,Um, that would be like, if we're looking at our services, kind of like what we talked about, where there's like the in platform skill version of it, which probably like how we do something like how we do an SEO analysis okay where the client deliverables like is there a deliverable associated with it in like each each one of these tasks have one or the other if not both eventually so yeah process documentation like yeah that's definitely something we,don't have and then And then client deliverables.,Don't know. Trackers, churn, client health.,Other than our NSM dashboards, that's pretty much it. Oh, well, actually, I mean, clients have their own reporting sheets where they see, you know, that kind of stuff, but that's client facing. It's not necessarily gonna have churn and stuff. We did just start a new churn and NRR tracking sheet, maybe? Let me find it for you and show you. I don't know where that would go in here, but let me share it.

 I keep wanting to call you Trevor for some reason. It's funny, you remind me of a childhood friend of mine named Trevor. You look exactly like him.,It's really trippy.,Yeah, I just shared it with you. New in our tracker that is probably like 85% good to go, I would say. If you go to the December tab, that's where you're going to want to, that's where you'll see the, the actual up-to-date information for the most part, not in our chat here. Oh, yeah, let me go back to it.,There you go.,This is a Chernobyl tracker.,OK, that's a tracker.,And this is actually directives. This is a clone of directives, apparently. I don't personally like how this is set up. It's pretty clunky to me. But whatever. I'm just going with it for now. And then maybe I can clean it up a bit later. Go to December, the December tab.,That's where you're going to see updated information.,Whoa.,This is one of those sheets that makes a lot of sense who made it, but maybe not to everyone. That's why I hate it.,It's not intuitive at all. That's the skill.,The skill is not to make it for you, it's to make it for everyone else.,Exactly. So I want to rebuild it eventually, but this is the one Preston gave me from Directive, and he was like, just duplicate it. So I'm like, that's what we're doing right now. But line 7 through 11 is the main info.,Yep, got it.,And the 37K isn't totally accurate. Like, it's not actual all turn some of that's credit. I don't know. It's a little bit weird right now. But yeah. Anyway, okay. All right.,Wait, I lost December.,There we go. So anyway, there's that I don't know if that goes.,Yeah, everything should all like ongoing, like our core process. And you kind of mentioned this early on to like, we're like, how many trackers do we need? Like how can we consolidate them, right? First we have to kind of gather all the ones we have, what we think they are. This is right, like we should have a churn tracker, we should have an NSM tracker, we should probably have some kind of client health type tracker, which is kind of a bigger conversation around like, you know, NPS, CSAT.

 Are we doing that at all, for instance?,I know we're either doing it or trying to do it, but I'm not sure.,Do you know if it's MPS or CSAT?,CSAT.,OK.,But I know it's happening in PPC, but I'm not sure to what extent right now. Yeah. Get more info on that.,Right.,Man, it's going to feel so good when all these things are just documented. We know when we're jumping into things, when we're not in the right system.,That'll be like the day of my life.,It happens. It does, we do get there.,All right.,I don't know if we need anything else here, because these are pretty self-evident. But if we have some, drop them in. So I do want to touch on a couple that I think are useful for this next phase here. Because when you're building, when you're doing things like understanding our services and our positioning, there's a minimum viable info you need. Around ICP again and like why clients churn SWAT they're doing.

 I think that'll be instructive. So let's talk about churn. Do we have churn qualitative like reasoning behind it outside of numbers?,We do. And it's in a spreadsheet somewhere that I haven't been in in like a month. Let me see if I'm capable of tracking I'm probably gonna have to find it. But yeah, we do have a big spreadsheet with a list of Turned clients with actual notes on reasons why Great.,Useful.,That's a really important input to inform our message. I've been wanting to analyze it, actually, and just kind of go deeper into it.,I just haven't had time yet. But we can do that. We can make a note to track that down in my notes here, and then we'll make it happen. Excellent.,Well, I feel pretty good with that one now. Actually, I think I can kind of remove this here. Perfect. Good. We got some more detail around those. Love that.,Put this down a little bit. OK, cool.,All right, the other one is ICP. So what we have now is we have ICP information. So we basically have like a firm a graph like profile, which is nice. Um, I'm, I'm still not sure.,What does that term?,Permagraphic is like the company version of like demographics. I gotcha. Exactly. Yeah. It's, it's this stuff, right? So we're like a demographic is going to be like location, age, income. Um, from a graphics is going to be like about the company size locations. I gotcha. Job titles revenue headcount things like so that's the icp version of it the um, the persona version and that's why I'm always kind of sometimes people say icp for every for like everything and These things get confused.

 So icp to me is like ideal customer profile, which is firmographic based right add on to that is personas, which is like These job title who the hell are these people and like what do we care about? And this matters because this is a very specific niche that I want to understand more. And like when Preston talks about it, it's clear he knows it. He spent time here and it's like, yeah, these people have like insurance issues and they're trying to like, whatever it is.

 Like that, I feel like we need to detail a little bit. And I have this in like a few different tabs. This is the most easy version, probably like of like some basic persona type information. I would want to know things like, you know, what they're measured on or what their jobs to be done is, which is, you know, more of a specific marketing framework or challenges, fears, values. I don't know.,Like that's the starting point. Um, I almost, I think we're going to do ICPs in the sprint, right?,Don't we have one week that has ICPs in it? Um, actually, yeah, it's week two right there. It's in something, right? Right there. It's in what we're supposed to be doing next week.,Yeah, that's cool. Can you, what if we take that sheet you have, give each department head one of those and see what they come up with?,Okay.,Yeah, I do. I like it here because that's kind of my point is that we, this is, we do need to know it upfront to help inform a lot of other stuff we're going to do. And we can inform that from a few different avenues. So like sales would have a perspective on this. The directors, I get, do the directors, are they talking to clients a lot? A lot. Yeah. Okay, good.,So they can understand it.,They have their own clients that and then they also, you know, jump in on major client calls.,So, okay. Do I have a personas deck here?,I don't. Okay. I have some pretty detailed stuff to get there.,But yeah, this is a good Yeah, if you have a good template for that, that would be really cool.,That way they can just fill it out, you know, not have to think about it too much. Well, cool. So I do have this here, and this is in our folder already in ICP Sheet.,Let me get rid of this.,So I'll duplicate one for each head. Is that what you want?,I don't know if there's different ones for P meeting. I feel like it's probably... We could just centralize it to one.,How do we get combined feedback, though? What's the best route for that?,Yeah, maybe just that they add their own notes in to each one. And maybe they just put their name next to their notes or whatever. But this feels kind of like team effort, I'd say. Perfect. Yeah. I like it. And again, that's a version very simple. There's like an ICP map version of it where it's like, all right, if we have a couple segments now within healthcare or treatment centers, like, um, what percentage of our client base are they current AOV tier job title.

 Ideally we have some of that in here already. Cause that is more ICP level. Um, I just think I want to get a little bit deeper there. Like, like, you know, who are these segments? Um, I think I'm just there's a bigger there's a bigger insight that I need to look at this a little bit more. Um, But there might be I just want we want to understand like the tiers like this is giving us like overall like yeah This is who your most valuable.

 Yeah, it is that's useful, especially for like paid media marketing and stuff But like I think we want to understand if there are different types of companies Yeah, and like what they need if they if they have different needs so that would be like the firmograph kind of like understanding of that. Like, all right, what percentage, if there are different segments, what percentage of our client base are they?

 Do they have different job titles? Things like that. It's basically you're answering questions like this. We don't have to go too deep into that right now. And the persona build on it would be this kind of stuff, state of the segment, I call that. We're going to try to understand it by segment. Does that align with who we want to be working with? Right, just our most valuable right now. Is that who we want to be in 2025?

 Or are there either through or companies we want to work with?,So basically, I just am trying to figure out the best way to extract this from our directors in a way that's going to be accurate and comprehensive. So the thing is, is they're not going to necessarily be able to to do all the data stuff of here's the average revenue for different tiers. But what I think that would be most helpful is the personas.,So maybe I should just have them focus on that. I think so. Yeah, certainly for them, this is the starting point, because let's get that segmentation going. The start, I'll probably remove this so they're not confused. I'll keep that because that's kind of useful. Yep. Yeah. Like, are there, you know, there's going to be segments.,I just don't know what they are yet. Sounds good.,All right.,We'll be right back.,One minute. Yep.,Okay, I might take a stab at that. All right. Are you back?,Are you back, Jordan?,I can't see.,Where's the screen?,All right, thank you. All right. Cool.,So yeah, let's have them start here. I might take a look at the segments because, yeah, if we kind of want them to be down here, then they need to be doing it off of some segment. Segmentation. So I might take a look at this again. Yeah, I just wasn't seeing like a clear segment in here. I was just kind of seeing like,,I wonder if you can throw this in the cloud and ask it to find segmentation.,Yeah, always a good starting point. Yeah, this is, yeah, because it's kind of spitting out one segment. Like this is our most useful segment. So that's fine. It could be just one for now. I do wonder if there's more. And that's usually where, yeah, to your point, if you came back to our customer list, which this isn't it, but we do have one. If we uploaded this to an AI, and I built a couple of tools that would help with this, it might then be able to segment them for us.

,Yeah, exactly.,So I wonder if we actually We actually have, is there source data? Here we go.,Do we have it?,All right, all right. That's what I'm talking about. Yeah, now we're looking at stuff that could be useful. OK, let me take a crack at this and see what we have here.,How old is this?,OK, 2024, 1024.,So that's pretty recent. OK, cool. All right, good. Lets me get a jump on that.,I feel like finding all these assets and stuff sort of like gold mining. I'm just like mining around and drives and asking people. Yeah, totally.,It's funny. It is. It's very satisfying to get everything together. I'm pretty organized in this way. And it just makes me feel like very complete. I feel like we can actually get some shit done if we had all this together uh-huh yep um okay cool so for my call with the team next week on the eight-week sprint um can we kind of look at,that and I can get your feedback on anything you want me to make sure we focus on yep let me look at the sheet so we've got We're going to be reviewing what they did week one, which will be,good.,I'm going to have them all review it. I'm going to have them review it all on the same call together, because I want to have them all seeing how they're doing. I like the cross-pollination, you know? Does that make sense to you?,OK, cool.,And then it also kind of motivates them to do a good job, didn't want someone else like crashing it.,Yeah.,Yeah. Saves you a lot of time too.,And everyone, I mean, just together. Yeah. Okay, cool. So on week two, I had outlined analyze current offerings, um, performance, and then identify optimization opportunities in their service. Define ICPs are the objective. So the deliverables were performance analysis, including project Efficiency, result, rate, measurement of performance, success for each service. It's going to get a little tricky for them to figure out how to do because a lot of the NSMs aren't set up like for SEO and things like that.

 But hopefully they can get creative and come up with something. Do you have any thoughts on that, that point? Maybe I should try to build out some kind of a format that's more plug and play for them. And try to have it ready. I just hate, like you said, putting them on the hook when they're already so busy. It's like, I want to try to do as much legwork as I can for them.,Yeah, this is always what happens. I remember having this conversation with Garrett. He's like, the directors will build a product. And I was like, the directors won't build anything. They can't do their day job, barely. Also, they're not good at it. But that's a second story. Totally. So this is like, um, this feels to me like a little bit of like a week one thing. Cause it's kind of like in the SWAT of everything, the way I'm looking at it.

 And I mean, this is more on my side of it, but like the service offering it, we know it needs development and clarification. So like that, that part of it to me is like, what is our service? Let's define it, look at it. Do we have the documentation to support it? And then talk about positioning this to me. It. As far as service offering is kind of like, you know, department. To me, that's a department performance analysis.

 You know what I mean? So it feels like it's less about service offering. It's less about the product. It's more about the department, which feels like a week one thing. I wonder if you're going to get that in the SWOT a little bit anyway.,I think we should maybe just have them define what their service is then, the current service offering.,Yeah, yeah, I think in that one was the way it was written was like I think I would struggle with that as a director because it felt like What is like how efficient are we or like how time to me?,They'll probably just be able to kind of agree That's why I wanted to look at this with you, uh chat through it. So identify optimization. All right, so What this could look like could be a spreadsheet outlining?,Different aspects of their service or it could be use what we have what we're gonna what I'll share with them In an email, which is that services doc.,Oh, yeah, so I can just put Laurent Yeah, we'll email you. Yeah, I've been here. I'll add it in right now. Oh, yeah, please do Do you want in the It does it go in here.,Does it go in like the template? Don't know where your link or I guess you're linking stuff here. Yeah Yeah. Okay.,I wanted to keep it all in one, but directive had to impress and wanted to have two. So I was like, all right, whatever. I was like, I don't know why we have this and the other one, but yeah, that's true.,It's true. So yeah.,Define current service offering. Do you want to put your link? Yeah. Do you want to just actually, I made it shareable with you. If you refresh should be able to get it.,All right. We'll do that.,That's perfect.,And then they can just fill it out.,I added positioning, and I'll kind of speak to that in the email just because it's basically like just two tabs.,Love it.,And I'll set those up for them. Cool. Service offering optimization. Yep. And we'll talk through that, you know, to be, you know, I think, you know, again, it's like getting full visibility, it'd be like, This is our SEO for instance when I looked at the SEO proposal. I liked it. I thought it was really clean It was also very basic in like felt like kind of old-school SEO which is Probably fine for a little bit because a lot of treatment centers are very old-school right probably with their web presence Probably another layer that we want to look at with that like I know directive has been trying to go there for years, which is like content focused than SEO because actually SEO is so messy right now with everything that's happening.

 So there's really more of a focus on like content first and SEO is kind of a byproduct, but focusing on the content side of it. And AI is huge in SEO and content now. So we need a point of view on that. So I know those are gonna be builds that we'll need. So, but we need a talking point and they can bring recommendations to it.,Is that in the sheet you sent? Yeah, and I'll put that in the briefing.,That's kind of the point.,You've got AI automation, layer, notion, and asset. OK, got it.,Yeah, so first part, and we're not going to accomplish this all in the week, especially as they move on to the next week of stuff in the sprint. So I think the point for us is just to get this underway. Our first step will be, let's map out our main, deliverables and actions that we take what are they there's probably more here than we actually do which is great we'll cut down and then eventually we're going to want to layer in do we have a client deliverable for it do we need one if we don't so we'll add like a yes no there notion training eventually this will create our notion map for like the knowledge center of scmp media so you can click into it it's going to have each of these with with that that loom video version um and then ai automation is going to be basically like a workshop for us to figure out like, can we AI this or automate it?

 I mean, I already kind of have a point of view on that for a lot of these things, but I do want them thinking that way. And there's probably 30% time back we can get by applying that layer effectively. So we don't know how to arrive there, but we have to do all those things kind of in the order to make it make sense.,Yep. Agreed.,All right, so that makes sense. Client segmentation analysis. Yeah, because we need to do that as part of defining our services. So I think that can go into the ICP sheet, which I can also link to, if that works.,Success. Make sure I update their template. I'm honestly considering just getting rid of the whole template doc.,It's like so repetitive and kind of not in alignment. So. Template doc's a little bit confusing for sure.,It is, yeah.,I don't know if there's.,Just to get off of this, to be honest. And we're going to provide more for them.,You can also just take the template doc, add it to the other doc in like almost like the appendix of the sheet and be like, look for further like context, you know, you could scroll down and look for more,bullet points if you're, you know, but you could definitely do that. I'll just tell them that on the next call, like ignore template moving forward, just ignore it.,Right. What we might do here, if you don't mind me taking a step. What I might say is like, it's probably the original one, but that's fine. Review. So like they should review the ICP. This is all about us getting on the same page with everything that's going on. So like maybe they haven't seen that ICP. Deck, right so they should take a look at that They should probably do take it do persona development, which means That sheet that I had showed you I'll do that and success numbers on Cisco, you know, yeah, you know by Second like what does that mean?

 Cause if you're like, yeah, some are successful, some aren't. If we're trying to do that with an ICP lens, then it means like, all right, like who is successful and who isn't successful.,Yeah.,Otherwise it might be, I don't know, like, otherwise we're kind of asking, well, what, what are the variables within a successful one versus an unsuccessful one? It could be, it might not be ICP. It might be, might be the, the strategist that's on the account. Right. I mean, it could be a million things, but, um, Okay. Oh yeah. So you know what, what, what maybe this is then that might not belong there.

 That might be just tighter around ICP and personas. And then this one might be kind of like, yeah, it's kind of together there. And there's probably a bit redundant between those two, but I don't know.,Why don't we probably just remove one of those delete this and keep the successful versus unsuccessful engagement.,Yeah.,Okay, cool. Yeah. Yeah.,So that looks pretty, that looks pretty tight. That's a lot. If you don't mind on our weekly call, I want to just continue to look at the, the preceding week and kind of editing it as we go.,Cause I want to make sure it's actually relevant in real time. Not just like I'm having them do random stuff.,So no, I think this version of it's a lot tighter. And more foundational. And then from the work that we do, it's gonna, when we start answering these kinds of questions, like the right strategy almost like reveals itself, right? And then we'll be like, oh wait, it's very clear what we need to do next, so. And then I can get a headstart on like, great, I have enough here. I wanna get to a point where I'm like 80% confident that we all agree on our service lines.

 And then I can craft an outline. Well, I'll probably start with a positioning outline and maybe agreeing on that sheet, but then I'll create that first capabilities deck. And then I can share it with Mitch and be like, Mitch, what do you think of this? He can give me some feedback. And then we can probably asynchronously finalize it that way. Love it. Yep. And while we're now talking with the sales team.

 And now we're in that, and we can talk about that next week and getting locked in. So all right.,Great stuff. Really good. Yeah, I'm excited. We'll get this cranking. And yeah, let me know if you run into any issues. Feel free to CC me if you're reaching out to anyone. And I can help kind of push things through if needed. But everyone's pretty on top of it. So yeah, any issues?,Yep. Awesome.,All right. Thanks a lot.,Well, I appreciate it. Have a good rest of your day, man.,All right. Thank you.

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: where's that sheet with the huge list of churned clients + reasons? I can't seem to find it can you share?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: <@U04EKCA5R5X|Sam O'Leary> <@U0106DW71NJ|Mitch Marowitz> I need to send out some challenges, could you help me with an outline of what you want them to do? Even if it's quick and dirty bullet points Ill clean it up and put it in a document to send out to the applicants

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Few people were asking for 930 for all hands so they can settle in. I don't mind that, lmk what you think

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: There is a new design request! ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Kim and Sam

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Hey man

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Could you come up with a few Google Call backgrounds that we can roll out company wide for consistency

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: sick

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I can probably knock it out tomorrow

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Understanding NRR at Webserv

What is Net Revenue Retention? (NRR)
• The percentage of recurring revenue retained from existing customers
• Includes expansions, contractions, and losses
• Key metric for sustainable growth
• Next meeting: We'll dive into our actual numbers

Why NRR Matters for Webserv
• Shows the health of our existing client relationships
• Measures our ability to grow accounts over time
• Helps predict future growth
• Strong NRR = Sustainable Growth

What We'll Track Moving Forward
Weekly Updates On:
• New client wins :tada:
• Service expansions :chart_with_upwards_trend:
• At-risk accounts needing attention :warning:
• Clients considering changes :arrows_counterclockwise:

Success Story: Horseshoe Ridge
Rethinking "Lost" Revenue
• Client moved from PPC to SEO services
• Not a loss - a strategic transition
• Key Learning: Revenue can move between departments
• Goal: Keep the client relationship AND the revenue

Team Questions About NRR
Common Questions We've Received:
1. "Does switching services count as lost revenue?"
    ◦ No - internal transfers maintain our NRR
2. "What counts as expansion revenue?"
    ◦ Increased budgets
    ◦ Additional services
    ◦ Upgraded packages
3. "How does this affect my department?"
    ◦ Each department has NRR goals
    ◦ Cross-department collaboration opportunities
    ◦ Focus on total client value

Moving Forward
What This Means For You:
• Weekly tracking starts now
• Monthly deep-dives into numbers
• Focus on retaining AND growing accounts
• Opportunities for cross-department solutions

Questions?
• Submit additional questions through Slack to Jordan Dahlquist
• Schedule 1:1 discussions if needed
• Next meeting: Full numbers review

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: If you can't do it it's ok

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Do you have bandwidth to take on an internal deck design for monday all hands meeting?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: but this first week is different

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yep there will be one needed every week

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: I was going to try to use Gamma if you can't do it

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: you are a saint

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Understanding NRR at Webserv

What is Net Revenue Retention? (NRR)
• The percentage of recurring revenue retained from existing customers
• Includes expansions, contractions, and losses
• Key metric for sustainable growth
• Next meeting: We'll dive into our actual numbers

Why NRR Matters for Webserv
• Shows the health of our existing client relationships
• Measures our ability to grow accounts over time
• Helps predict future growth
• Strong NRR = Sustainable Growth

What We'll Track Moving Forward
Weekly Updates On:
• New client wins :tada:
• Service expansions :chart_with_upwards_trend:
• At-risk accounts needing attention :warning:
• Clients considering changes :arrows_counterclockwise:

Success Story: Horseshoe Ridge
Rethinking "Lost" Revenue
• Client moved from PPC to SEO services
• Not a loss - a strategic transition
• Key Learning: Revenue can move between departments
• Goal: Keep the client relationship AND the revenue

Team Questions About NRR
Common Questions We've Received:
1. "Does switching services count as lost revenue?"
    ◦ No - internal transfers maintain our NRR
2. "What counts as expansion revenue?"
    ◦ Increased budgets
    ◦ Additional services
    ◦ Upgraded packages
3. "How does this affect my department?"
    ◦ Each department has NRR goals
    ◦ Cross-department collaboration opportunities
    ◦ Focus on total client value

Moving Forward
What This Means For You:
• Weekly tracking starts now
• Monthly deep-dives into numbers
• Focus on retaining AND growing accounts
• Opportunities for cross-department solutions

Questions?
• Submit additional questions through Slack to Jordan Dahlquist prior to weekly call.
• Schedule 1:1 discussions if needed
• Next meeting: Full numbers review

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text:

____________________________________________________________
SLACK MESSAGE THREAD: Username: jd Text: ____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Thanks so much

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Yes those are great!

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Mind sharing it with the other heads?

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: Awesome I'll check it out

____________________________________________________________
SLACK MESSAGE THREAD:
Username: jd
Text: You rock, thank you!

____________________________________________________________
"""