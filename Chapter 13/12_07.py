from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''// Functions first
@import "../node_modules/bootstrap/scss/functions";

// Variable overrides second
$primary: #900;
$enable-shadows: true;
$prefix: "mo-";

// Required Bootstrap imports
@import "../node_modules/bootstrap/scss/variables";
@import "../node_modules/bootstrap/scss/maps";
@import "../node_modules/bootstrap/scss/mixins";
@import "../node_modules/bootstrap/scss/root";

// Optional components
@import "../node_modules/bootstrap/scss/utilities";
@import "../node_modules/bootstrap/scss/reboot";
@import "../node_modules/bootstrap/scss/containers";
@import "../node_modules/bootstrap/scss/grid";
@import "../node_modules/bootstrap/scss/helpers";
@import "../node_modules/bootstrap/scss/utilities/api";'''

if __name__ == '__main__':
    app.run(debug=True)