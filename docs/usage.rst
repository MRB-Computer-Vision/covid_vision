=====
Usage
=====

To use Covid Vision in a project::

    from covid_vision.ml.models.covid_cxr import CovidCXR
    clf = CovidCXR()
    img = clf.read_image(PATH_TO_IMAGE)
    result = clf.predict(img)

