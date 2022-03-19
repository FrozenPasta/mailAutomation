# This file was used when I was a Business Developer for the student association of my engineering school, Telecom SudParis.
# This was used for sending brochure and slide presentation to the partners

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import information #File containing credentials

#Connection parameters to the email server. We will use the SMTP connection
smtp = smtplib.SMTP_SSL("server_address")
smtp.ehlo()
smtp.login(information.email, information.password_cas) #Email and password are contained in the information.py file


# Creation of the MIMEMultipart Object, which is the message content
msg = MIMEMultipart()


def send_to_specific_company(unFichier):
    """
    Send mail to a specific company. Here, we will send two files, a partnership proposal and a presentation brochure.
    The presentation brochure was named Plaquette_OpportunityDay.pdf whereas the partnership proposal followed the following typo : Presentation_XXX.pdf
    with XXX the name of the company.
    
    Args:
        unFichier (String): the file name we want to send to the company.
    """
    unFichierOrigine = unFichier.split('_')[-1]
    nomEntreprise = unFichierOrigine[:-4] #Retrieve the company name from the file name

    combinaison = [unFichier, r"Plaquette_OpportunityDay.pdf"]

    #Mail object
    subject = "Proposition de partenariat " + nomEntreprise + " - BDE IT SUD PARIS"
    msg['Subject'] = subject
    textPart = MIMEText(texte, "html")
    msg.attach(textPart)

def send_to_multiple_companies(chemin):
    """
    Similar to send_to_specific_company method but will send several mails.
    It walks through a given directory and gets a list of files.
    It then creates the subject and email.

    Args:
        chemin (String): path to the directory.
    """
    fichiers=[]

    #Creates a tuple containing the : root, directory path and the file name
    for root, dirs, files in os.walk(chemin):
        # check the extension of files
        for i in files: 
            if i.endswith('.pdf'):
                # print whole path of files
                fichiers.append(i)

    companyName = []    #Company name
    listeFichiersPresentation = []
    for f in fichiers:
        if (f.startswith("Presentation")):
            listeFichiersPresentation.append(f)
            mot = f.split('_')
            print(mot)
            companyName.append(mot[-1].strip("^.pdf"))
    

    for fi in range(len(listeFichiersPresentation)):
        combinaison = [listeFichiersPresentation[fi], r"Plaquette_OpportunityDay.pdf"]

        #Mail object
        subject = "Proposition de partenariat " + companyName[fi] + " - BDE IT SUD PARIS"
        msg['Subject'] = subject

        attachment = MIMEApplication(open(r"directory_path_containing_partnership_proposal" + listeFichiersPresentation[fi], "rb").read())
        attachment.add_header('Content-Disposition','attachment', filename=listeFichiersPresentation[fi])
        msg.attach(attachment)

    textPart = MIMEText(texte)
    msg.attach(textPart)

    attachment = MIMEApplication(open(r"directory_path_containing_partnership_proposal" + listeFichiersPresentation[fi], "rb").read())
    attachment.add_header('Content-Disposition','attachment', filename=listeFichiersPresentation[fi])
    msg.attach(attachment)
    textPart = MIMEText(texte, "html")
    msg.attach(textPart)

texte = """

"""
texte2 = """
"""

send_to_specific_company(r"partnership_proposal.pdf")
#send_to_multiple_companies(r'directory_path_containing_partnership_proposal.pdf')


# Make a list of emails, where the mail will be sent
# to = ["...", "..."]
# Print to the terminal the current email sent
# print("Envoi de mail à " + to[0] + " ...")
# Provide some data to the sendmail function!
# smtp.sendmail(from_addr="email",
#               to_addrs=to, msg = msg.as_string())
# Close the connection
# smtp.quit()