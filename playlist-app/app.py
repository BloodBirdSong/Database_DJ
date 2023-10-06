from flask import Flask, redirect, render_template, flash, request
from flask_debugtoolbar import DebugToolbarExtension
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm
from models import db, connect_db, Playlist, Song, PlaylistSong
import logging

app = Flask(__name__)

app.debug = True
logging.basicConfig(level=logging.DEBUG)
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
debug = DebugToolbarExtension(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2728@localhost:5432/playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)
# db.create_all()



# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist.html", playlist=playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    
    if form.validate_on_submit():
        input_name = request.form["name"]
        input_description = request.form["description"]
        new = Playlist(name = input_name, description = input_description)
        db.session.add(new)
        db.session.commit()
        return redirect(f"/playlists/{new.id}")
        
    return render_template("new_playlist.html", form=form)

##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    song = Song.query.get_or_404(song_id)
    return render_template("song.html", song=song)


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()

    if form.validate_on_submit():

        input_title = request.form["title"]
        input_artist = request.form["artist"]
        new = Song(title=input_title, artist=input_artist)
        db.session.add(new)
        db.session.commit()
        return redirect(f"/songs",)

    return render_template("new_song.html", form=form)


@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""
    app.logger.info("HERE")
    playlist = Playlist.query.get_or_404(playlist_id)
    
    # app.logger.info(type(playlist))
    # app.logger.info(playlist)
    # app.logger.info(playlist.name)
    # app.logger.info(playlist.description)
    
    app.logger.info("HERE2")

    form = NewSongForPlaylistForm()
    playlist_songs = PlaylistSong.query.all()   
    songs = Song.query.all()    
    # for song in songs:
    #     app.logger.info(type(song))
    #     app.logger.info(song)
    #     app.logger.info(song.id)
    #     app.logger.info(song.title)
    #     app.logger.info(song.artist)

    app.logger.info("HERE3")

    # Restrict form to songs not already on this playlist

    curr_on_playlist = []
    
    app.logger.info(curr_on_playlist)
    form.song.choices = (db.session.query(Song.id, Song.title).filter(Song.id.notin_(curr_on_playlist)).all())

    if form.is_submitted():
        selected_song_id = request.form["songs"]
        app.logger.info(selected_song_id)
        app.logger.info(selected_song_id.title)
        app.logger.info("FORLOOP")
        # check for doops
        for playlist_song in playlist_songs:
            app.logger.info(selected_song_id)
            app.logger.info(playlist_song.song_id)
            app.logger.info(type(int(selected_song_id)))
            app.logger.info(type(playlist_song.song_id))
            
            app.logger.info(playlist_id)
            app.logger.info(playlist_song.playlist_id)
            app.logger.info("LOOP")

            if (playlist_song.playlist_id == playlist_id) and (playlist_song.song_id == int(selected_song_id)):
                app.logger.info("MATCH")
                return render_template("add_song_to_playlist.html", playlist=playlist, songs=songs,form=form)
                # curr_on_playlist.append(song)
        new = PlaylistSong(song_id=selected_song_id, playlist_id=playlist_id)
        app.logger.info("NEW SONG")
        app.logger.info(new)
        db.session.add(new)
        db.session.commit()
        
        # return redirect(f"/playlists/{playlist_id}")



    return render_template("add_song_to_playlist.html", playlist=playlist, songs=songs,form=form)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
