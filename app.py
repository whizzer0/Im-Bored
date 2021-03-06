from flask import Flask, render_template, request
from api import lookUpEventFul
from ticketmaster import lookUpTicketmaster
from cinema import lookUpCinema
app = Flask(__name__)
app.debug = True

@app.route("/example", methods=["GET"])
def example():
    return render_template("example.html", data=None)

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html", data=None)
    
@app.route("/form-alt", methods=["GET"])
def formAlt():
    return render_template("form-alt.html", data=None)

@app.route("/results", methods=["POST"])
def results():
#	results = lookUpEventFul(request.form["town"])
    
    results = lookUpTicketmaster(request.form["town"],request.form["datefrom"],request.form["dateto"],request.form["price"])
#	output = ""

 #	for event in results.iter('events'):
#		for node in event:
#			output += str(node.tag) + " - " + str(node.attrib) + " - " + str(node.find('title').text)


    return render_template("results.html", data=results)
    
@app.route("/results-alt", methods=["GET"])
def resultsAlt():
    #results = lookUpTicketmaster(request.form["town"],request.form["datefrom"],request.form["dateto"],request.form["price"],request.form["sortby"])
    #if not request.form["postcode"] == "":
        #cinemas = lookUpCinema(request.form["postcode"],True)
        #listings = lookUpCinema(request.form["postcode"],False)
        #return render_template("results-alt.html", data=results, dataCinema=cinemas, dataListing=listings)
    #else:
        return render_template("results-alt.html")
	
if __name__ == "__main__":
    app.run()
