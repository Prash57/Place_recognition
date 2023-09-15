import os
#import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from ai_api import detect_image


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        detectedClasses = detect_image(filename)
        image_classified = detectedClasses["images"][0]["classifiers"][0]["classes"]
        images = [obj["class"] for obj in image_classified]
    # return redirect('/')
    sites = {"Pashupatinath": {
        "Name": "Pashupatinath",
        "URL": "/static/Pashupatinath1.jpg",
        "visiters": "one million",
        "Coordinates": "27°42′35″N 85°20′55″E",
        "discription":
        "The Pashupatinath Temple (Nepali: पशुपतिनाथ मन्दिर) is a famous and sacred Hindu\
        temple complex that is located on the banks of the Bagmati River,approximately 5 km\
        north-east of Kathmandu in the eastern part of Kathmandu Valley, the capital of Nepal.\
        This temple complex was inscribed on the UNESCO World Heritage Sites's list in 1979.\
        The temple was created in the 5th century by Licchavi King Prachanda Dev.",
        "History": "It is a popular temple. The temple was created in the 5th century \
            by Licchavi King Prachanda Dev after the previous building was consumed by \
            termites.[5] Over time, many more temples have been erected around this \
            two -storied temple. These include the Vaishnava temple complex with a \
            Rama temple from the 14th century and the Guhyeshwari Temple mentioned\
            in an 11th-century manuscript."

    }, "Hanuman_Dhoka": {
        "Name": "Hanuman_Dhoka",
        "URL": "/static/s.jpg",
        "visiters": "two million",
        "Coordinates": "27°42′35″N 85°20′55″E",
        "discription": "Hanuman Dhoka is a complex of structures with the Royal \
        Palace of the Malla kings and also of the Shah dynasty in the Durbar \
        Square of central Kathmandu, Nepal. It is spread over five acres. \
        The Hanuman Dhoka Palace (Hanuman Dhoka Darbar in Nepali) gets \
        its name from the stone image of Hanuman, the Hindu deity, \
        that sits near the main entryway. 'Dhoka' means door or \
        gate in Nepali.",
        "History": "The eastern wing with ten courtyards is the \
        oldest part dated to the mid 16th century. It was \
        expanded by King Pratap Malla in the 17th century with \
        many temples. Sundari Chok and Mohan Chok in the north \
        part of the palace are both closed. In 1768, in the \
        southeast part of the palace, four lookout towers were \
        added by Prithvi Narayan Shah. The royal family lived \
        in this palace till 1886, where after they shifted to Narayanhiti \
        Palace. The stone inscription outside is in fifteen languages and \
        legend states that if all the 15 are read milk would spring \
        from the middle of stone tablet.[3]"

    }, "Janakpur_Dham": {
        "Name": "Janakpur_Dham",
        "URL": "/static/cv.jpg",
        "visiters": "three million",
        "Coordinates": "27°42′35″N 85°20′55″E",
        "discription": "Janakpur जनकपुर is a sub-metropolitan city in Dhanusa \
        District of Province No. 2 of Nepal.The site was designated as a \
        UNESCO tentative site in 2008.The city is a centre for religious \
        and cultural tourism. It has been declared as the temporary \
        capital for Province no. 2 until Province Assembly votes for \
        a permanent capital.",
        "History": "The temple is popularly known as the Nau Lakha Mandir \
        (meaning \"nine lakhs\").The cost for the construction of the \
        temple was about the same amount of money: rupees nine lakhs \
        or nine hundred thousand. "
    }, "Lumbini": {
        "Name": "Lumbini",
        "URL": "/static/lumbini.jpg",
        "visiters": "four million",
        "Coordinates": "27°42′35″N 85°20′55″E",
        "discription": "Lumbini लुम्बिनी (Sanskrit for \"the lovely\") is a Buddhist \
            pilgrimage site located at the Nepalese town of Kapilavastu, Rupandehi \
            District of Province No. 5 in Nepal, near the Indian border.\
            Lumbini is one of four Buddhist pilgrimage sites based on major events in the life \
            of Gautama Buddha. Interestingly, all of the events occurred under trees.\
            The other three sites are in India: Bodh Gaya (enlightenment), Sarnath (first discourse), \
            and Kushinagar (death).It is the place where, according to Buddhist tradition, Queen \
            Mahamayadevi gave birth to Siddhartha Gautama in 563 BCE.",
        "History": "In the Buddha's time, Lumbini was situated in east of Kapilavastu and southwest \
            Devadaha of Shakya, an oligarchic republic.[8][9] According to Buddhist tradition, it was \
            there, that the Buddha was born.[10] A pillar discovered at Rupandehi in 1896 is \
            believed to mark the spot of Ashoka's visit to Lumbini. The site was not known \
            as Lumbini before the pillar was discovered.[11] The translation of Inscription \
            reads:[12] \"When King Devanampriya Priyadarsin had been anointed twenty years, \
            he came himself and worshipped (this spot) because the Buddha Shakyamuni was born \
            here. (He) both caused to be made a stone bearing a horse (?) and caused a stone \
            pillar to be set up, (in order to show) that the Blessed One was born here. \
            (He) made the village of Lummini free of taxes, and paying (only) an eighth share \
            (of the produce).\" [13] The park was previously known as Rupandehi, 2 mi (2 mi (3.2 km)) \
            north of Bhagavanpura."


    }, "Swayambhunath": {
        "Name": "Swayambhunath",
        "URL": "/static/swambhunath.jpeg",
        "visiters": "two million",
        "Coordinates": "27°42′35″N 85°20′55″E",
        "discription": "Find peace and prayers on the little hillock of Swaymbhunath \
            in the northwest of Kathmandu Valley. Visitors for whom the name was a \
            tongue twister have called it \"Monkey Temple\" from the 1970s. Swayambhu, \
            overlooks most parts of the valley giving visitors a panoramic view of \
            the city. The stupa has stood as a hallmark of faith and harmony for \
            centuries with Hindu temples and deities incorporated in this \
            Buddhist site.The glory of Kathmandu Valley is said to have started from this point. ",
        "History": "Swayambhunath is among the oldest religious sites in Nepal. According to \
            the Gopālarājavaṃśāvalī, it was founded by the great-grandfather of King Mānadeva \
            (464-505 CE), King Vṛsadeva, about the beginning of the 5th century CE. This seems \
            to be confirmed by a damaged stone inscription found at the site, which indicates \
            that King Vrsadeva ordered work done in 640 CE.[3]However, Emperor Ashoka is \
            said to have visited the site in the third century BCE and built a temple \
            on the hill which was later destroyed."
    }
    }
    for image in images:
        if image in sites.keys():
            return render_template("sites.html", sites=sites[image])
        else:
            return render_template("info.html", error="CANNOT PROCESS")

        return redirect('/')

    print(image)


if __name__ == "__main__":
    app.run()
