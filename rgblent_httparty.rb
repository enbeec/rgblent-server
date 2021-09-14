require "httparty"
require "json"
require "json"

class RGBlent
  include HTTParty
  base_uri "localhost:8000"

  def initialize(token)
    @options = { headers: { "Authorization": "Token #{token}" } }
  end

  def color(pk: nil)
    self.class.get("/colors#{pk.class == 1.class ? "/" + pk.to_str : ""}", @options)
  end
end

$tokens = { "joe": "9ba45f09651c5b0c404f37a2d2572c026c146694" }