export class MoviePoster{
  public id: number;
  public name: string;
  public poster_path: string;

  constructor(id: number, title: string, poster_path: string) {
    this.id = id;
    this.name = title;
    this.poster_path = poster_path;
  }
}
