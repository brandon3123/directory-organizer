from aenum import Enum, NoAlias


class Extension(Enum, settings=NoAlias):
    """
        File extensions handled and there associated folder names.
    """

    # Document extensions
    PDF = 'pdf'
    TXT = 'text'
    DOCX = 'word'

    # Script extensions
    SH = 'scripts'

    # Zipped extensions
    ZIP = 'zipped'
    GZ = 'zipped'
    TGZ = 'zipped'

    # excel/csv extensions
    CSV = 'csv-excel'
    XLSX = 'csv-excel'
    XLSM = 'csv-excel'

    # Web page extensions
    HTML = 'web-page'

    # Data extensions
    JSON = 'json'
    XML = 'xml'

    # Application Extensions
    EXE = 'applications'
    APP = 'applications'
    DMG = 'applications'
    PKG = 'applications'

    # Image extensions
    ISO = 'iso-image'
    OVA = 'os-image'

    # Code extensions
    JS = 'java-script'
    JAVA = 'java'
    CLASS = 'java'
    PYC = 'python'

    # Certificate extensions
    CER = 'certificates'
    CERT = 'certificates'
    CRT = 'certificates'
    PEM = 'certificates'
    KEY = 'certificate-keys'
    P12 = 'key-pairs'

    # Media extensions
    SVG = 'vectors'
    GIF = 'gifs'
    PNG = 'images'
    JPG = 'images'

    # Uncommon extensions
    JKS = 'jks'
    RLC = 'rhapsody'
    UNKNOWN = 'misc'
