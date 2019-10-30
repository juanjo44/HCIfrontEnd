using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace ProyectoHci
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class Peliculas : ContentPage
    {
        public Peliculas()
        {
            InitializeComponent();
        }

        private async void intPeliculas(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new IntPeliculas());
        }

        private async void volver(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new Inicio());
        }

        private async void irGeneros(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new Generos());
        }
    }
}