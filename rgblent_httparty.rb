require "httparty"
require "json"
require "json"

class RGBlent
  include HTTParty
  base_uri "localhost:8000"

  def initialize(token)
    headers = token ? { "Authorization": "Token #{token}" } : {}
    @options = { headers: headers }
  end

  def color(pk)
    if pk
      response = self.class.get("/colors/" + pk, @options)
      response.parsed_response
    else
      response = self.class.get("/colors", @options)
      response.parsed_response
    end
  end

  def info(rgb_hex)
    response = self.class.post("/colorinfo", :headers => @options[:headers], :body => { "rgb_hex": rgb_hex }).parsed_response
  end

  def get(path)
    response = self.class.get(path, @options).parsed_response
  end

  def post(path, body)
    response = self.class.post(path, :headers => @options[:headers], :body => body).parsed_response
  end

  def login(username, password)
    response = self.class.post(
      "/login",
      :headers => @options[:headers],
      :body => { "username": username, "password": password },
    ).parsed_response

    if response["success"]
      puts response
      return RGBlent.new(response["token"])
    else
      puts "failed to log in"
    end
  end
end

$nobody = RGBlent.new(nil)
$joe = RGBlent.new("9ba45f09651c5b0c404f37a2d2572c026c146694")
