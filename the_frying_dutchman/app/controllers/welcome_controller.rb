class WelcomeController < ApplicationController
  def index
    @num_bins = 0
    @busboy_status = 'Idle'
  end
end
