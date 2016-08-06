import os

from dcard.cli import parser, main, download


class TestCli:

    def test_verbose_log(self):
        argv = 'download -f funny -n 15 -v'.split()
        args = parser.parse_args(argv)

        main(args)
        assert os.path.exists('dcard.log')

    def test_download_basic(self):
        argv = 'download -f funny -n 15'.split()
        args = parser.parse_args(argv)
        assert args.forum == 'funny'
        assert args.number == 15

    def test_download_params_likes(self):
        argv = 'download -f funny -n 15 -likes 50'.split()
        args = parser.parse_args(argv)
        assert args.likes_threshold
        assert args.likes_threshold == 50

    def test_download_params_folder(self):
        argv = 'download -f funny -n 15 -o ./downloads/test -F'.split()
        args = parser.parse_args(argv)
        assert args.flatten
        assert download(args)
