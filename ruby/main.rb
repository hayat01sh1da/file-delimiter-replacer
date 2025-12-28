require_relative './lib/application'

puts 'Provide the target extension of files whose delimiter you would like to make chances to:'
extension = gets.chomp.strip

puts 'Provide the delimiter you would like to replace the original one with(Default: `_`):'
delimiter = gets.chomp.strip

puts 'Provide d(dry_run: default) to make sure what directories and files are to be delete first. Then, provide e(execution) if you would truly like to delete the files. This operation is cannot be undone, so be alert to your operation!'
mode = gets.chomp.strip

params = { extension:, delimiter:, mode: }.reject { |_, value| value.empty? }

Application.run(**params)
