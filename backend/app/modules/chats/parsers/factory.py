from app.modules.chats.parsers.pdfParser import PDFParser
from app.modules.chats.parsers.imageParser import ImageParser
from app.modules.chats.parsers.interfaces import IFileParser

class ParserFactory:
    @staticmethod
    def get_parser(file_name: str) -> IFileParser:
        extension = file_name.split('.')[-1].lower()
        
        if extension == "pdf":
            return PDFParser()
        elif extension in ["jpg", "jpeg", "png", "webp"]:
            return ImageParser()
        else:
            raise ValueError(f"Avbodh AI currently does not support .{extension} files.")