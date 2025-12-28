require 'minitest/autorun'
require 'fileutils'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup
    @extension = '.m4a'
    @base_dir  = File.join('.', 'test', 'Artist')
    [
      File.join(base_dir, 'Album1', "1-01 Title#{extension}"),
      File.join(base_dir, 'Album1', "2-01 Title#{extension}"),
      File.join(base_dir, 'Album2', "01 Title#{extension}"),
      File.join(base_dir, 'Album2', "02 Title#{extension}"),
      File.join(base_dir, 'Album3', '01 Title.mp3')
    ].each { |path|
      FileUtils.mkdir_p(File.dirname(path))
      FileUtils.touch(path)
    }
  end

  def teardown
    FileUtils.rm_rf(File.join(base_dir)) if Dir.exist?(File.join(base_dir))
  end

  def test_invalid_mode
    error = assert_raises Application::InvalidModeError do
      Application.run(extension:, mode: 'a')
    end
    assert_equal('a is invalid mode. Provide either `d`(default) or `e`.', error.message)
  end

  def test_replace_space_with_underscore_in_dry_run_mode
    Application.run(extension:)
    assert_equal [
      './test/Artist/Album1/1-01 Title.m4a',
      './test/Artist/Album1/2-01 Title.m4a',
      './test/Artist/Album2/01 Title.m4a',
      './test/Artist/Album2/02 Title.m4a',
      # This path should remain unchanged since the target extension is .m4a
      './test/Artist/Album3/01 Title.mp3'
    ], Dir[File.join(base_dir, '**', '*.*')].sort
  end

  def test_replace_space_with_underscore_in_execution_mode
    Application.run(extension:, mode: 'e')
    assert_equal [
      './test/Artist/Album1/Disc1/01_Title.m4a',
      './test/Artist/Album1/Disc2/01_Title.m4a',
      './test/Artist/Album2/01_Title.m4a',
      './test/Artist/Album2/02_Title.m4a',
      # This path should remain unchanged since the target extension is .m4a
      './test/Artist/Album3/01 Title.mp3'
    ], Dir[File.join(base_dir, '**', '*.*')].sort
  end

  def test_replace_space_with_specific_delimiter_in_execution_mode
    Application.run(extension:, delimiter: '-', mode: 'e')
    assert_equal [
      './test/Artist/Album1/Disc1/01-Title.m4a',
      './test/Artist/Album1/Disc2/01-Title.m4a',
      './test/Artist/Album2/01-Title.m4a',
      './test/Artist/Album2/02-Title.m4a',
      # This path should remain unchanged since the target extension is .m4a
      './test/Artist/Album3/01 Title.mp3'
    ], Dir[File.join(base_dir, '**', '*.*')].sort
  end

  private

  attr_reader :extension, :base_dir
end
