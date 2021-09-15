require "httparty"
require "json"
require "json"

class RGBlent
  include HTTParty
  base_uri "localhost:8000"

  def initialize(token)
    @options = { headers: { "Authorization": "Token #{token}" } }
  end

  def color()
    response = self.class.get("/colors", @options)
    response.parsed_response
  end

  def get(path)
    response = self.class.get(path, @options).parsed_response
  end
end

$joe = RGBlent.new("9ba45f09651c5b0c404f37a2d2572c026c146694")
