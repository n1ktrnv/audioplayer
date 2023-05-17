import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from app.videos.service import get_audio_stream, AudioStream


class TestGetAudioStream(unittest.TestCase):
    def test_get_audio_stream(self):
        video_id = "test_video"
        start = 0
        end = 1024
        path = Path("app/resources/audios") / video_id
        expected_data = b"audio data"
        expected_filesize = 2048

        # Создание фиктивного объекта Path для проверки вызова функции _read_audio_bytes
        path_mock = MagicMock(spec=Path)
        path_mock.stat.return_value.st_size = expected_filesize

        # Создание фиктивного файлового объекта с методом read
        file_mock = MagicMock(spec=open)
        file_mock.return_value.__enter__.return_value.read.return_value = expected_data

        # Мокирование вызова open и его контекстного менеджера
        with patch("builtins.open", file_mock) as open_mock:
            # Вызов функции get_audio_stream
            audio_stream = get_audio_stream(video_id, start, end)

            # Проверка, что функция open вызывается с правильными аргументами
            open_mock.assert_called_once_with(path, 'rb')

        # Проверка, что возвращается ожидаемый объект AudioStream
        self.assertIsInstance(audio_stream, AudioStream)
        self.assertEqual(audio_stream.start, start)
        self.assertEqual(audio_stream.end, end)
        self.assertEqual(audio_stream.data, expected_data)
        self.assertEqual(audio_stream.filesize, expected_filesize)


if __name__ == "__main__":
    unittest.main()
