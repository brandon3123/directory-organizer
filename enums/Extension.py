from aenum import Enum, NoAlias


class Extension(Enum, settings=NoAlias):
    """
        File extensions handled and there associated folder names.
    """

    # Document extensions
    PDF = 'pdf'
    TXT = 'text'
    DOCX = 'word'
    PPTX = 'power-point'

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
    XLS = 'csv-excel'

    # Web page extensions
    HTML = 'web-page'

    # Data extensions
    JSON = 'json'
    XML = 'xml'
    YML = 'yaml'
    YAML = 'yaml'

    # Application Extensions
    EXE = 'applications'
    APP = 'applications'
    DMG = 'applications'
    PKG = 'applications'

    # Image extensions
    ISO = 'iso-image'
    RDP = 'iso-image'
    OVA = 'os-image'

    # Code extensions
    JS = 'java-script'
    JAVA = 'java'
    JAR = 'java'
    CLASS = 'java'
    PYC = 'python'
    SQL = 'sql-scripts'

    # Certificate extensions
    CER = 'certificates'
    CERT = 'certificates'
    CRT = 'certificates'
    P7B = 'certificates'
    PEM = 'certificates'
    KEY = 'certificate-keys'
    PUB = 'certificate-keys'
    P12 = 'key-pairs'

    # Media extensions
    SVG = 'vectors'
    GIF = 'gifs'
    PNG = 'images'
    JPG = 'images'
    JPEG = 'images'
    MP4 = 'videos'
    M4A = 'music'
    MID = 'music'

    # Font extensions
    TTF = 'fonts'

    # Log extensions
    LOG = 'logs'

    # Uncommon extensions
    JKS = 'jks'
    RLC = 'rhapsody'
    UNKNOWN = 'misc'
