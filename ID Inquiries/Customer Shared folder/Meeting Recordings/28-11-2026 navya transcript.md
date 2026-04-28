Thank you. Please carry on
training of the instruction documents or how to do it.
Please remember it because one of the things Marker said is we can ignore that book doesn't want to focus on that now.
Okay.
Leave it.
Okay.
So this completing instructions, the completion of instruction is causing some issues.
We need the client portal CRM and the ID portal saying the same thing.
There is no clarity for each either ID or client currently the last stage.
Okay.
So this part right?
Previously they have not provided the stages stage titled instruction complete.
So in this is like previously we had only stages till music files available.
Okay, I'll open any document and show any instruction record.
So I consider this.
So here we have the stages from open till audio files available only till this we had before before the feedback like we received.
So then what they asked is after audio files available they still want one more stage named instructions complete
and Okay, we are displaying in CRM instruction complete and also we have it in the portal.
I'll show you that as well.
Report.
Okay.
All instructions.
So here also we display the stage in all instruction we have stage field where we display that
other one is we have client portal even on client portal also we should display that instructions, stages and all that.
Like whatever the details we have should be showcased to client should be displayed to them like here stage.
So they Okay, right where instruction is in what stage.
So previously it was only audio files available, but now they've asked that.
So I have implemented that this instruction complete.
I mean, I think I have created this after implementing that.
So instruction complete.
Once the job is complete, that is there are stages.
Okay, if you want me to walk me walk you through the system like how from the right from the beginning to end.
So you will be knowing like what exactly this instruction complete is Okay.
Yeah.
Like if you don't mind if you are, I have time if you want like, Yeah, Yeah, No queries.
So initially my ideal queries, they reach the instruction.
Creation happens in two stages like two ways.
One is through the creator portal and one is in CRM.
So if it is through the creator portal, the clients, they'll come here and they'll create the instructions and they'll submit.
So I just check any exact address
used. Most of them.
Okay.
So they add the client reference.
Client reference will be similar to their premises name with some just identification and specific instructions.
If they want to give to the ID queries team they will add the instructions here and here there is a limit like we have added the rich text field here so that it only allows till that if the text is more than that then they have to shorten the text and they have to put in here.
So that is instructions to the ID team.
That client will be giving the instructions and just
instruction type. We have these many Cafe shop and all that,
and then priority level, we have specific event, high end normal for I normal, there is no instruction like a particular thing we have, there is a condition or mandatory fields, but whereas if it is specific event, this specific date will be a mandatory field for that.
Okay, so I will add this here MYS name, I'll have to add the same and the address just copy
and
this one post code
invented
and this thing we have licensing authority, premises license holder, designated premises supervisor.
These are not mandatory fields and this fields whatever you fill in here, the same thing will reflect in your CRM and in CRM it displays in three modules, one is premises, one is premises check and one is instruction.
So in all the three modules we have these data that will get sync with that.
So I just submit it.
Okay.
Once we submit, initially the stage will be with ID here, so it means the instruction is under ID in queries they're still not accepted it.
So instruction with ID.
But here when we see that on CRM the stage will be open
refresh.
So so on CRM we have three different stages open like here open query with client and computer checks.
For all these three we consider as with ID and on hold as well for first four on CRM if the record is in whichever the stage right from open to on hold.
But to the client it will be showing us with ID only when the stage moves to instruction allocated from then it just shows the exact.
So until unless it is not instruction is allocated the stage says with ID on the clients portal.
Okay,
yeah.
And now once they receive it, the client will be triggered like instruction.
There is a email triggered to the client, so they'll be resolved.
So one more thing, so the instruction will be saved in in both creator report and also in CRM.
Right.
Correct.
Correct.
Whenever you are updating the stages here, we will be making create API to update the value in the report.
Is it right?
Correct?
Correct.
OK.
So whatever you update here, it updates there in the creator portal like vice versa.
So if we do any updates on the creator side, it won't get updated here.
Right?
So we resolve
Sorry, sorry, sorry.
You cater is a read only view, Right?
So it doesn't have any functionalities like it will only show data from the CRM.
Apart from that, it doesn't hold any automation workflow to workers, a stand alone.
Correct.
Correct.
Yeah.
That's right.
Okay.
Yeah.
So whatever you change here, it shows there and also there also we have some automation and on portal like whenever the instruction is allocated.
So here also we trigger the workflow.
I mean we trigger the workflow basically to the CRM only like we trigger the workflow here.
So it gets changed like instruction stages gets changed and also it reflects everywhere in the system across the system like creator as well as CRM.
Okay,
yeah, yeah.
So once the instruction is logged, I email will be triggered to client and a license check, license check will be created upon the instruction creation only.
So that is this one PC 222.
So and one more thing is the premises also gets recorded mean they created here.
So first thing what they have to do, what they actually do is they go to premises
here.
Sometimes in their use cases the clients might not have entered the right address here.
So for that what we have added is they wanted a map widget.
So we have added this map widget here.
So before like whatever they have to do when the condition is first thing they have to accept it or they have to approve this premises.
So to approve they have to go in here, they have to approve it.
So once they approve, then this automation like when they click on the map widget, the address will sync in here.
And on this map widget if their address mentioned is not correct or if they feel it is not correct, they can just drag and drop the marker and they can update it.
So what like when they update it, it will not really change in the address, but it only changes the latitude and longitude in the system because we are not changing the address, only they have asked us to change the latitude and longitude.
So at the moment we have only this, but for a few addresses in you, not just UK, everywhere, it just shows multiple markers.
Maybe if it is in the same street or something like that, it shows multiple markers.
So in that they have to select the right marker.
So we have to select it here and they have to update.
So once they update these fields like latitude and longitude data will be stored in these fields.
Initially it will be not like stored.
Okay.
So once they have it, you once they get this latitude and longitude and this, this that is all they do in the premises module.
Basically they don't do any other part here.
They might had the details of licensing authority, if they have not filled in the initial stage, they might add it and if they add it here everywhere it updates across the system.
Okay.
So wherever it's mapped like in the creator or like in the instructions because we where instructions, Yeah.
Wherever we have this fields, right?
It just gets updated Okay.
Because we will have look up, Right?
So for example in the instruction will be having a lookup, so it doesn't affect anything, Right?
If you click on the lookup, it will be coming here and you can see the updated changes.
But what I'm asking, like there'duplicate fields, like analysing authority field is in any other module also, so anything is updated here, will be updated there Also, it's something like that or yes, whatever we update here, like for example licensing authority field, we have it in premises instructions and license checks.
So if I update anything here, it updates in every other modules as well as in creator report as well.
Okay, can you go to instruction?
Show me where is its map in instructions or license check?
Okay, Yeah.
So here you can see this premises instructions information, licensing authority, these fields, all three fields we have here and in the license check also we have these three fields.
Okay.
So that duplicate fields.
Right.
So all of them are carrying the all the premises value.
You, but not sure why you are showing it here.
Sorry, we already having those values in the premises.
Yeah, but they want all the details in every other modules that is their requirement.
I mean the ID queries required.
So even though it's premises, they want to show it in all the.
Yeah.
Correct.
We have told them like we, we already have the lookup for every other modules.
Like here we have premises instruction for both.
We have the lookup, but no, they want the detail like the data should be displayed in every other module.
Okay, maybe we have something called lookup field so it will automatically pref those value from the premises.
I have solved it somewhere.
I'm not sure about it.
But while you are creating the field, you can have a lookup field so you can drop the premises look up field into the instruction module so that whenever any updates in the premises will be automatically updated here, not update that.
It's like like a look up.
It will take the value from the premises and show it in the instruction module rather than we we are doing this manually.
Right.
Yeah.
Okay.
Okay.
Then I got it.
I thought like then duplicate fuse or something like that.
Okay.
I, I understood what needs please carry on.
Yeah.
Okay.
So if it was that whatever, I update here,
I got it automation where it updates everywhere across the system.
So it's vice versa. Right. So whenever updating the inspections module also it will be updated. Yeah. Correct. Correct.
A to Z cloud, it just updates everywhere.
And yeah.
Here, I think that is the end of this premises module and they don't later check this.
So once this is done they go to license checks and yeah, anyways it is open here.
So here they will come and they'll have, they may have to send some emails which are not automated.
It's all manual emails they send,
they send a email like there are some.
Two emails which are templates are created email to council and this one.
So these are all manual, no automation in this license checks and they if they want to fill in something they fill in and they just change the status from new to closed once all that license formalities are done.
So closed.
Okay.
Closed complete.
So this is about the premises and license checks module and now coming back to instructions once the premises checks is done, once that all that license checks formalities are done they'll mark the stage it even here this is manual like till completed checks like they'll change it to completed checks stage manually from here afterwards it's all automated.
On hold is not automated but from there it is all automated.
Now when they manually change the stage to completed checks, email will again triggered to the client.
I think not the client. I think it's
your yeah. Email will be triggered to client saying is their instruction. The request is accepted and
assignment record gets created here in the map paget
think this one.
Yeah.
So when they mark the stage has completed checks here and ready for allocation.
So the ID Enquiries team has to allocate the investigator for this particular record.
So that will be done by ID Enquiries team.
So what they have to do is they should and we also have they have asked for access directly to the portal.
So here we have added a button.
So when they they can go to portal and there they have to allocate the investigator for that particular
record.
So what they do is they come here they go to map widget.
Here we have three things in this map widget.
One is instructions allocated which is on red instructions ready for allocation and investigators location.
So here they will check for the instruction which is ready for allocation.
Then select this and we can also select multiple values.
I think you have suggested this.
Right, if I'm not wrong, Lele Karthik and
hello.
Yes, Yes, sorry, I wasn't mute, I forgot to un-mute it.
Yeah.
Actually getting this within me and Karthi was having discussion.
Yeah,
Yeah, So that part only here.
So they can select multiple jobs here and they can allocate the investigators.
So when they selected it, they have like we are changing that colour to green and we'assign that to investigator.
So when we assign to investigator the ID in queries person can also give an instructions to the investigator if he wants to give any instructions.
You can give that here visit
in the
07:00 P.M., something like this and this field we have added in the instructions module.
So whatever the ID queries team person enters the data here for the investigator instructions.
So that gets updated in the creator portal as well as in the CRM.
Okay.
So now that turns red.
So here on the map widget, we are only asked to show the instructions allocated, ready for allocation and investigators location.
So once this Barbean Cafe completes its job, like once that job is closed, that disappears from this.
I mean once the site visit is completed, that disappears from this map.
So that was the requirement.
And now once it is allocated, the stage gets changed to instructions allocated.
So all your VS code is pushed to Jitter repository, UC Cloud repository.
I'm not really sure Karthik has actually asked with me and I, I asked him to check with Tega and yeah, I, I'm not sure about it. I'll have to check with Karthik once in case as in module to the VT.
It's good to have those code in the JA Correct.
Correct.
That's right.
Okay.
This stage also one digit write, one in the CRM and one in the creator.
Yeah.
Okay.
So that stage updates everywhere across the system.
And now the instruction is allocated.
So once the instruction is allocated an email like as you have, like I have allocated this to Matthew.
So now Matthew will receive an email saying new new music instruction allocated with the site visit link.
So these details, even the instructions to the investigator visit in the evening around 07:00 P.M..
So all the details will be here with the site visit link.
So this is Investigator portal.
So we have two portals, custom client portal and Investigator portal.
So this one is Investigator portal and they'll be having access only to site visits and invoices, whereas client will have the access only to instructions.
So yeah they he'll come here and this is the record. So he'll have to check
why are you so slow?
Okay.
So here an investigator can accept it or reject it for like their own reason.
So here we have accept investigation if he accepts.
So there are some mandatory fields and details he has to fill in if he rejects, so you just have to write the reason.
Even that's not mandatory, you just have to update.
And then when he update the stage here then again go back to completed like the previous one, completed checks.
If he rejects it it get back to completed checks again and if he accepts he or she may have to fill in all these details.
Visit date and
outside would be taken approximate. There are some fields, no time entered premises
7 pm
PM and if they have identified any music tracks they may have to add the details here.
Okay.
And here they have two things.
If there is any audio visual files, if they have captured any video during the visit, or if they have any sketch plan images, they'll have to upload here.
And it is again
public link where everyone, even the client and everyone can access it.
So this is where they can upload it the audio visual files and sketch plan images.
So both are public links which I link to that button
while it says MO.
And so once he completes everything he may save as like if you want to save a staff if he can do it or if it is all complete he can mark this visit report completed and update and here submitting invoice is mandatory like it's not mandatory and like it will be stored in their next report but it just notifies there.
Thank you for completing the site is kindly use the invoice tab to submit your invoice and they've also asked to show how many files they have uploaded.
So here it says one audio visual files uploaded and one sketch plan images uploaded.
So this is how they get them notified.
And Since he has not uploaded the invoice that calls in here like under site visits which no invoice and also in the report in ID and queries, I just switch back to IDN queries.
So this is ID enquiries portal.
I mean the main ID and queries portal it is.
So here
the first thing is awaiting initial review.
It comes here but the invoice is not submitted to this.
So before if they want to proceed with anything the submission like invoice submission is required.
So what he can do is he can go here Invoices.
Go to the invoices form.
We have to select the respective job complete at the invoice date.
Here there are a few categories like ours, mileage and expenses.
So I'll when I explain this, I'll show.
I also explain one of the point in the feedback sheet
M is 100
and expense, expense, I 100 fold and parking.
So here I have, Okay, I have added mile.
I thought like oh yeah.
So here I have selected as expense which is like food and parking.
In the feedback sheet, they have asked for us to make some changes.
Miscellaneous expenses.
This red one which is not done.
So what they have asked is miscellaneous expenses in invoice in the portal.
They're just adding the values like quantity is like 150 and they're just directing the description.
But they also want a button or an upload file where they can upload the receipt of that expenses.
Okay, this 150 if they are saying they should upload that expenses receipt.
So but that is not done, I think it's still under pending or something.
Yeah, that is the requirement here.
They just say here that food and parking they have charged like 150, but we should have a field or like upload field where they can upload it.
Yeah, I got it, but my question was if they upload it, should we save it anywhere, maybe in the WorkDrive or anywhere?
But they have not answered for that yet.
But yeah, that is still open.
And here we have the total and they submit.
So once they submit it here, if I go and see that record will not be there, Bikane will not be there because it has pushed to add in queries portal and they will not also see once the job is complete and once they submit everything that will disappear from their list the investigators list.
So this this is where investigator job will be done.
That's the end of investigators profile.
And now coming back to here and this is ID in queries SPN.
So once he completed the report again if I go back to CRMN check this page will be visit complete
also here
the stage will be with it complete. Okay. But why it is saying reinstruction here
the previous moo
No, I don't think we have used it.
It's the live, right?
Because I haven't pushed it.
Go to the live, It's in the development only Okay, Okay, Okay.
I think there's something missing.
Okay.
So here it says it complete and no emails triggers at this moment.
And now the first first thing is there is a veryy called, Who is that Jackie?
I think I'm not sure.
So yeah, some person.
So first initial review, they'll do it, they'll go to reports in progress and they'll go to this awaiting initial review and they'll Review all this and they'll just update this here.
Initial review complete then market.
Yes.
And they just updated it.
So once they do that, the report gets generated in the WorkDrive folder as well as they have added the music identified music tracks so that will be sent to the client.
Okay.
Yeah.
Now the stage is visit under review and if I go to emails, music tracks will be sent to client that which are under identified music tracks.
So whatever is listed so that document as made as a PDF document and will send that to client.
I can just download it.
Yeah. So this details will be sent to client. Okay.
One more thing happens at this stage that is report gets generated and get saved in the
folder.
So one, this one is the music tax document with the SAR and the other one is the report report.
Okay.
So here I'll again get back to the page because there is something and regarding that, some names something, it's naming format.
So naming formats for reports and invoices.
Can this be changed from having dashes in between it must.
So previously what I did was like Barbean Kee is a premises name.
I've added an_or like a iPhone between the premises name and this post code and the name report.
But they have asked us to remove that.
So I've just removed, removed it and just without any underscores or without any icons here.
So this was the change which was asked here.
So this is the report once ID enquiries team like Jackie completes this initial review.
Next there's a guy called John, so that person will do the actual review, the site visit review.
So once it is done here, it moves to site visit, review that record.
So what he do is first thing he'll review this and he check this report, go through the details and he'll also check if there is any audio visual files they have uploaded.
If there are any files, they will check this audio visual files if there is any video uploaded here, and if there anything where they have to capture like for example here we have outline photo taken.
If it is yes, then what John has to do is he has to capture that picture from this video audio visual file and he has to paste it here in the document.
Okay.
So that job, he'll do it and he'll have to download it once everything, all the changes are added or whatever the data is added, we have to download it as a PDF and then
review everything.
If there is any audio visual files, if there are any audio files, then what he has to do is he has to check this check box.
Audio files, check this box only if audio files are available.
We have added the description there and we do the site review complete and we have to upload this.
So once this is checked, this report upload field is mandatory.
They have to upload the report.
Okay.
Something is broken, something is broken,
something looks broken. So this is this was mandatory at that time. Okay, I'll checks.
So he has to add this and update.
So when audio files are like this particular check box is checked, a task created and if he updates that, a task should be created in the CRM and gets assigned to there is a person called Matthew so that should get assigned to that person.
Open activities.
So here Okay send audio files to client
query the task.
Yeah.
So here send audio files to client.
So he has to review this and here they have the access to that audio visual files or audio visual files folder.
So you have to capture the audio file, separate that video audio like only this, he has to separate that audio files from that the whole audio visual file and he has to send it to the client once that job is done, you have to mark this task as closed.
Once you mark this as closed and email will be triggered to there are two ladies, Alison and Melissa.
So for them an email will be triggered to them saying you can send the invoice the next stage they can like continue if that if there is no audio files in it and if John has not marked it then this part of the work is not there.
I mean the no task gets created and like the other next process it is not there.
It is directly the those two ladies takes over the job,
got it
and
where am I?
There is one more thing here once John completes it and once he updates the data and he uploads the report, the stage becomes report complete or available and the stage the report will also be added here.
Since I have not uploaded in the initially it is not coming up here.
I have to check so this button gets enabled.
The client on client portl where they can download it both the reports and the music tracks.
Also also here
an email will be triggered to client saying Instruction complete.
The report is now available.
The link is not visible because it has not generated Since I missed uploading it.
Link link.
Yeah, this is empty.
If this is empty we don't get the link there.
Okay.
So this is about it and the next stage in this is we also have to review the Aing Johns review.
You should also review the invoice
that comes under invoice review.
There's a report like name invoice review.
So there you should come in here, you have to approve it.
Basically job will only approve this if you say yes, the data gets updated and if in case if you say no and then this this field pops up and here you have to enter the values like for example, you know, and then and I 80 and that other details gets updated.
Expenses say yes here if you see client amount here it says 200 and why it is 10,000.
The calculation is like 200 into 50.
I'm not wrong.
So yeah, there is some calculation which is added for clients, we have to multip, for us we have to multiply with this value, for mileage we have to multiply with this value.
And for investigators it is it has to be multiplied with some value.
So that's why you see the difference here, it says 200 here, but when we approve it here it says 5000 per investigator and 10,000 per client.
Okay.
Some value added in.
And here we have this.
So once you approve everything, he has to do this initial review, complete check and update.
So that's when job John's job is complete.
Now that Alison and Melissa comes into picture and they do here awaiting invoice,
edit, edit, they'll review everything.
They just say, I think not wait, wait, wait, not addition in Mear.
If there is any audio files, what they do is they come here that Matthew, the one who close the task comes here and he'll add the audio files here and they have added a file audio files URL here.
So what they have to do it to add the audio files is they'll have they should have to create a new folder under their records WorkDrive folder.
They have to create a new folder audio files or something and then they have to generate this is they have not automated it because this is not an actual case.
If there is only audio files only then this part of the work comes into picture.
If there is no audio files present then we don't need this in the setup.
That's why this is manual process at the moment.
They have to create the external share link,
they create copy and that file, that link, they have to add it here.
Okay.
Updates.
So once he updates this,
that also this button download audio files button gets enabled. Once that is filled and
Okay, the client have the access to that
again, I'm back to ALA's task.
Okay.
That last thing here is they have to upload.
Okay.
Okay.
First thing.
Okay.
Here
initial review of the invoice is done now Alison or Melissa will do this final review.
So here what they do is they review the details and they'll check this checkbox Admin review complete and they'll update.
So when they do this invoice final review, an invoice gets generated and saved in the WorkDrive.
The client invoice as well as investigators invoice.
Both the invoices will be generated and saved in the WorkDrive.
So that is here.
But like invoice just says inverse is the client invoice.
The other one is a investigator invoice.
It gets it takes some time, takes some time
too much. Right? Don't you think it's too much what? Yeah.
The thing is like if it's like in one go, if they give all those requirements, it's Okay.
But if you're doing something, they come back and say, Okay, it's not like that, do this.
So if you're going the mind like already complex and like adding more complex to
Yeah. Actually,
because to understand this path itself take some time
also, the client also exactly know the requirements so they will use it and again come back and say like no it's not either.
We need to do like this, then we have to change it.
Yeah. Wrap it up in next week. Yeah.
Okay. I just take another 2 min and not bore you anymore.
You can carry.
No, it's almost done.
This is the last stage.
So invoice, they have generated the client invoice and other one is investigator invoice.
Okay.
So here is the values that 10,000 and the 5000 values.
So that is only the difference between these two invoices that will be sent to client and this will be sent to investigator.
Has HY been on this?
Sorry?
Has HY been on this?
Like some of these templates? anything?
No.
I worked on this.
Okay.
I think Hybin was asking some issues on some project like a few months back.
Okay.
It was this look, something like this.
Okay, Okay, Okay.
Okay.
So this is done now only the client invoice.
We have to upload in the portal so they'll download it and they'll come in here awaiting invoice.
So everywhere where I check the checkbox, right?
That every time that state gets updated everywhere like first is initial review and then site with it complete and then audio files available and yeah, like that, send invoice to client, I'll check this checkbox, I'll upload that file and I'll update.
So it's a manual field, right?
So whenever search check the box.
Yes, that F.
So now that disappears from here and it will move to ID completed instructions here we get it and if we see the clients portal that download invoice button gets enabled and the stage will be instructions complete.
Okay. Now both that buttons are enabled and now we get back here.
Yeah.
Now the last stage is instruction complete.
So by that time every other email will be sent like all reports, invoice and everything will be sent to the client.
Okay.
I think, I think we are done.
The job is done.
So Yeah, that's what like whatever the changes here we have made that clients that is located.
Yeah, I think I have covered most of it.
The whole process explains what this white part of the package.
Okay.
Like I have one more thing like can you go to the row number eleven small down
disappearing from the system?
Like do you know what they mean?
Yeah.
So what they are saying is email to client.
We have noted that when an email sent a client is as AO and the comment request to us using the note section to mark it for the same and there are more the stages on the email appears from the system.
So what they are saying is I said you about the premises checks, right?
So here we send some manual emails. I'll send this
Yeah. Just give me a minute someone at the door. Just give me yeah, yeah, yeah,
yeah, sorry.
I'm back.
Yeah, Okay, yeah.
So what they're saying is now they'll send us email to the client, Okay?
And so that will be recorded here and once they reply back is what I've sent once when the client replies to us, we are using the notation to there after both the stages.
Okay.
So what they're saying is I'll show you.
So the email which I have sent it in here and I'll reply back,
but that will not really good open recorded in CRM at the moment.
I think because they have not completed the email configuration,
they have not completed the email configuration and they are not linked to like Outlook or anything.
So until and unless they do it, that received email will not be recorded here.
Correct.
Okay.
So they have the IMAP, Yeah.
That IMAP configuration, they do it, they have to do it.
So until and unless they do it, whatever they received, then that will not be recorded here.
But I'm what I'saying is once they send in, once there is a reply, this email was actually disappearing from this email section, it seems, but I couldn't replicate it.
It is still there.
I have replied to it and yeah, but the images, I'm still able to see that email here and email section it is not disappearing and that's what I have written here.
Try to replicate, they should report it, but couldn't replicate.
The client replace to note section to mark A and is on this email disable you prefer one.
Yeah, I need to have a look.
I'm not sure how it goes disappeared because if it's come, it's entered means it cannot be disappeared.
No, if if we could, if you don't see the received email, that is fine.
It is fine still because the IMAP is not done.
But whatever we have sent will not get disappeared.
Yeah.
So yeah, she do know that the reply email won't come.
So she has a copy pacing into the note section.
That's fine.
She understood that part.
So I think he's saying like this email getting disappeared, but yeah, the email we have sent can't like that.
It should be Zoho issue if not in our hand.
But yeah, we can just yeah, we can just say them or we need to have some in such line check ID something like in which record you have faced the issue so you can keep and say like, Okay, you have sent this mail but it disappeared because we do have the timeline, right?
So any email is sent from any correct then correct.
That should record, right.
They have tried for this SP still, I think if I'm not wrong
still
or they have sent a email from some other
like a general email instead of like going to record and making that email see like all it will be recorded on a timeline like whatever the email I sent, but in there like what she reported, she clearly mentioned about this pot still job, but that pot still doesn't have any email sent.
No idea what she actually trying to say.
Okay.
Code.
Yeah, Yeah.
Have a
this is all ID
Okay.
Then maybe the last one.
I think so.
Like can I go to the 1313 comments?
Yeah, I told you right.
Initially, I've added that underscores and iphones between the names.
It's like for all the reports or for specific reports in the invoices.
No, at the moment they have only these things like this report invoice, but one more thing
I wanted to check with you.
So this one, these two things are recording here.
The one which we upload, the one which we upload also gets recorded here.
But for that we are still getting this underscores.
I mean now where we are mentioning about the name convention, so this should this should be the name in the script, but automatically it is taking this underscores.
And I don't know how do we get rid of this underscores from the uploaded files.
Can you go to the logic like it's happening the creator workflow or CRM flow creator flow.
Right?
No creator creator can you go to the workflow
want to check like how the naming is constructed
has used used_index.
Okay.
This_index we have and that's why you are trying to get the the value from like split by_and trying to get the index of the
sub string.
Before that you will be creating the up file file name. So where the file name comes from file here.
Okay. Okay. Fold 95 UR
Okay, it's like you're according to the creator attachments.
Right?
Yes.
So it's like maybe it's default creators, the naming convention.
So you trying to download the file from creator and once you get the download file, they have this naming convention like they will save the file as and this file name or when you uploading the file you will be having the file name is like this No, the one which we uploaded, like I have uploaded this one download, so this doesn't have any barbc like wherever we have the space, right?
So that space is filling with underscores in that uploaded files.
Yeah.
So it's like a creator naming convention.
Like whenever you upload something file in the creator in the background creator is having_because they don't allow the spaces for the encoding.
Okay?
In order to avoid the encoding thing, they are trying to remove the spaces and have_got it.
What when whenever have you seen those name in the URL, it will be like a percentage be something like this, right?
So avoid underscore.
So it's like create a navig.
Okay.
I think that is not really a big thing.
I think they can ignore this because that, but what you can do is like manually replace the_of the spaces after like when you uploading the file in the WorkDrive, so you are do creator then you getting the file name out of that and if you can go to the workflow like create workflow.
Yeah, Yeah, that can be done.
Yeah.
I think we have
so maybe we can do that to avoid the_in the work file name.
Yeah, Yeah, That's about this 13th and yeah. So I think I go
one is fine.
Yeah, I think it's yeah, done more than what I expected.
Like I was asking for two or three things.
I have said more than ten things.
I think we have covered actually.
Why I insisted like it's good to know the overall thing because I carried it.
Yeah.
That's why even I wanted to have this call before only like when you took over that client part because only when you know the whole journey then you will be able to, you know, understand and analyse and do things.
Yeah, because I, I can see the in thing.
I'm not sure how the hierarchy of FE and everything because I've going to invoice, I can see the invoice thing but when it happen.
So what's before the invoice?
What's after invoice?
So I don't know about it so didn't know about it.
Like it's good to know.
Thank you Na so much. Hope you have a good weekend. Yeah, Yeah, Thank you
Weeken. Yeah, I just go through and will disturb you if I have any more doubts. Yeah, sure.
Thank you Rak You bye.